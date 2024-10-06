import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io
import cleaner


load_dotenv()
host = os.environ.get("host_name")  
user = os.environ.get("user_name")  
password = os.environ.get("password") 
database = os.environ.get("database")

scope = ["https://www.googleapis.com/auth/drive"]

# Load credentials from the downloaded JSON key file
credentials = ServiceAccountCredentials.from_json_keyfile_name('adventure-works.json', scope)

# Build the Google Drive service
drive_service = build('drive', 'v3', credentials=credentials)

# Define your folder ID from Google Drive (You can get it from the folder URL)
folder_id = '1dLWjlJ_f8SYclUN8fPrciCVksddwJnHZ'

# Fetch the list of CSV files in the folder
results = drive_service.files().list(q=f"'{folder_id}' in parents and mimeType='text/csv'",
                                     spaces='drive',
                                     fields='files(id, name)').execute()

files = results.get('files', [])

# Check if the folder contains files
if not files:
    print('No files found in the folder.')
else:
    print(f"Found {len(files)} files in the folder.")
    
    # Store dataframes from each CSV file
    dataframes = {}
    
    # Loop through each file and download the CSV data
    for file in files:
        print(f"Fetching file: {file['name']}")
        
        # Request the file and download it as binary content
        request = drive_service.files().get_media(fileId=file['id'])
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while not done:
            status, done = downloader.next_chunk()
            print(f"Download {int(status.progress() * 100)}%.")
        
        # Reset the file handle position to the start
        fh.seek(0)
        
        # delimiter = delimiter_mapping.get(file['name'])
        
        # Read the CSV into a pandas DataFrame
        df = pd.read_csv(fh, delimiter='\t')
        dataframes[file['name']]=df

    
    df_products = cleaner.products(dataframes["Product.csv"])
    df_sales = cleaner.sales(dataframes["Sales.csv"])
    df_targets = cleaner.target(dataframes["Targets.csv"])
    df_region = dataframes["Region.csv"]
    df_reseller = dataframes["Reseller.csv"]
    df_salesPerson = dataframes["Salesperson.csv"]
    df_salesPersonRegion = dataframes["SalespersonRegion.csv"]

    connection = mysql.connector.connect(
        host = host,
        user= user,  
        password= password,  
        database= database  
    )

    cursor = connection.cursor()

    tables = {
        'sales': df_sales,
        'sales_person_region': df_salesPersonRegion,
        'products': df_products,
        'targets': df_targets,
        'region': df_region,
        'reseller': df_reseller,
        'sales_person': df_salesPerson
    }

    engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{database}")

    for table_name, df in tables.items():
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    
    print("succesfully exported to MySQL")

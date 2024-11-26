
# **Adventure Works: Dynamic Sales Dashboard Project**

![Adventure Works Dashboard](https://github.com/Atulsahoo333/Adventure-Works/blob/main/Dashboard)

## **Project Objective**

The goal of this project is to build a dynamic, real-time dashboard in Power BI that connects to an SQL database. The dashboard visualizes key insights such as sales performance, regional analysis, and targets using the Adventure Works dataset. The project integrates data processing using Python, data storage in MySQL, and real-time data updates in Power BI.

---

## **Project Structure**

This project follows a structured approach with the following key steps:

1. **Data Processing**:  
   - Load and clean the Adventure Works dataset using Python and pandas.
   - Handle missing data, normalize formats, and ensure data consistency.

2. **SQL Database Setup**:  
   - Create a MySQL database with appropriate tables for each dataset (Product, Sales, Region, etc.).
   - Load cleaned data into the MySQL tables.

3. **Power BI Dashboard**:  
   - Connect Power BI to the MySQL database.
   - Design an interactive dashboard that reflects key sales metrics and updates in real-time.

4. **Real-Time Data Updates**:  
   - Configure Power BI to automatically refresh data at intervals or trigger updates based on SQL changes.

---

## **Project Steps**

### 1. Dataset Processing

- **Python Script**: `data_processing.py`  
  The `data_processing.py` script handles reading, cleaning, and preprocessing CSV files using the pandas library. This step ensures data consistency before loading into the SQL database.

- **Cleaning Tasks**:
  - Drop missing or irrelevant values.
  - Normalize column names and formats (dates, currency, etc.).
  - Handle outliers and inconsistencies.

**Example:**
```python
import pandas as pd

# Load Sales data
sales_df = pd.read_csv('Sales.csv')

# Clean and preprocess Sales data
sales_df.dropna(subset=['Sales'], inplace=True)
sales_df['Order Date'] = pd.to_datetime(sales_df['Order Date'])
sales_df['Sales'] = sales_df['Sales'].apply(lambda x: round(x, 2))

# Export cleaned data
sales_df.to_csv('cleaned_sales.csv', index=False)
```

---

### 2. SQL Database Integration

- **SQL Setup Script**: `database_setup.sql`  
  This script creates the necessary tables in MySQL for storing the cleaned data. Ensure you have MySQL Workbench or an equivalent setup.

**Example SQL Schema:**
```sql
CREATE DATABASE adventure_works;

USE adventure_works;

CREATE TABLE Sales (
    SalesID INT PRIMARY KEY AUTO_INCREMENT,
    OrderID INT,
    Sales FLOAT,
    OrderDate DATE,
    ProductID INT,
    SalespersonID INT,
    RegionID INT
);

-- Load cleaned data into the tables
LOAD DATA INFILE '/path/to/cleaned_sales.csv' 
INTO TABLE Sales 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
```

---

### 3. Power BI Dashboard

- **Power BI File**: `adventure_works_dashboard.pbix`  
  This file contains an interactive, real-time dashboard built in Power BI. The dashboard includes visualizations like:

  - **Total Sales by Region**: A bar chart showing sales performance across different regions.
  - **Salesperson Performance**: A line chart tracking sales performance over time for individual salespeople.
  - **Target vs. Actual Sales**: A KPI card comparing actual sales to targets for each quarter.

**Power BI Setup**:
1. Connect Power BI to the MySQL database:
   - Go to "Get Data" > "MySQL Database".
   - Enter your database connection details and load the tables.
2. Create dynamic visualizations using sales and product data.
3. Enable automatic refresh to update the dashboard in real-time.

<img src="https://github.com/Atulsahoo333/Adventure-Works/blob/main/BI_dashboard" width="900" height="600">

<img src="https://github.com/Atulsahoo333/Adventure-Works/blob/main/BI_dashboard_1" width="900" height="600">


---

### 4. Real-Time Data Updates

Configure Power BI to refresh the data either at scheduled intervals or based on SQL triggers.

- **Auto Refresh**:
  - Set a refresh interval in Power BI (e.g., every 15 minutes).
  - Use SQL triggers to push updates when significant changes occur in the data.

---

## **Folder Structure**

```
Adventure-Works-Project/
│
├── data/
│   ├── Product.csv
│   ├── Region.csv
│   ├── Reseller.csv
│   ├── Sales.csv
│   ├── Salesperson.csv
│   ├── SalespersonRegion.csv
│   ├── Targets.csv
│
├── scripts/
│   ├── data_processing.py
│   ├── database_setup.sql
│
├── dashboard/
│   ├── adventure_works_dashboard.pbix
│
├── README.md
├── Screenshot.png
```

---

## **Prerequisites**

- **Python**: Install pandas and MySQL connector (`pip install pandas mysql-connector-python`).
- **MySQL Database**: Install and configure MySQL Workbench.
- **Power BI**: Download and install Power BI Desktop.

---

## **How to Run the Project**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/adventure-works-project.git
   ```

2. **Data Cleaning**:
   - Navigate to the `scripts/` folder and run the `data_processing.py` script to clean the dataset.
   ```bash
   python data_processing.py
   ```

3. **Set Up MySQL Database**:
   - Run the `database_setup.sql` script to create the database and tables.
   ```bash
   mysql -u username -p < database_setup.sql
   ```

4. **Load Data into SQL**:
   - Load the cleaned data into the SQL database using MySQL Workbench or command line.

5. **Power BI Dashboard**:
   - Open `adventure_works_dashboard.pbix` in Power BI Desktop.
   - Ensure the data connection is configured to your SQL database.
   - Set up automatic refresh for real-time data updates.

---

## **Contributing**

Feel free to submit issues or contribute to the project by creating pull requests. Check the `CONTRIBUTING.md` for guidelines.

---
**Thank You**




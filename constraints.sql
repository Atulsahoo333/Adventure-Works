USE adventure_works;

ALTER TABLE Products
ADD PRIMARY KEY (ProductKey);

ALTER TABLE Region
ADD PRIMARY KEY (SalesTerritoryKey);

ALTER TABLE Sales_person
ADD PRIMARY KEY (EmployeeKey);

ALTER TABLE Reseller
ADD PRIMARY KEY (ResellerKey);


ALTER TABLE Sales
ADD CONSTRAINT FK_Sales_Product FOREIGN KEY (ProductKey) REFERENCES Products(ProductKey),
ADD CONSTRAINT FK_Sales_Reseller FOREIGN KEY (ResellerKey) REFERENCES Reseller(ResellerKey),
ADD CONSTRAINT FK_Sales_Region FOREIGN KEY (SalesTerritoryKey) REFERENCES Region(SalesTerritoryKey),
ADD CONSTRAINT FK_Sales_Salesperson FOREIGN KEY (EmployeeKey) REFERENCES Sales_person(EmployeeKey);

ALTER TABLE Sales_person_Region
ADD CONSTRAINT FK_SalespersonRegion_Salesperson FOREIGN KEY (EmployeeKey) REFERENCES Sales_person(EmployeeKey),
ADD CONSTRAINT FK_SalespersonRegion_Region FOREIGN KEY (SalesTerritoryKey) REFERENCES Region(SalesTerritoryKey);

ALTER TABLE targets
ADD CONSTRAINT FK_Targets_Salesperson FOREIGN KEY (EmployeeID) REFERENCES Sales_person(EmployeeID);






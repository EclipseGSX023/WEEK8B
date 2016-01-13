import mysql.connector
import csv

class Orders:

    def __init__(self, row):
        self.OrderID = row['OrderID']
        self.CustomerID = row['CustomerID']
        self.EmployeeID = row['EmployeeID']
        self.OrderDate = row['OrderDate']
        self.RequiredDate = row['RequiredDate']
        self.ShippedDate = row['ShippedDate']
        self.ShipVia = row['ShipVia']
        self.Freight = row['Freight']
        self.ShipName = row['ShipName']
        self.ShipAddress = row['ShipAddress']
        self.ShipCity = row['ShipCity']
        self.ShipRegion = row['ShipRegion']
        self.ShipPostalCode = row['ShipPostalCode']
        self.ShipCountry = row['ShipCountry']
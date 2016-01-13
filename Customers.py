import mysql.connector
import csv

class Customers:

    def __init__(self, row):
        self.CustomerID = row['CustomerID']
        self.CompanyName = row['CompanyName']
        self.ContactName = row['ContactName']
        self.ContactTitle = row['ContactTitle']
        self.Address = row['Address']
        self.City = row['City']
        self.Region = row['Region']
        self.PostalCode = row['PostalCode']
        self.Country = row['Country']
        self.Phone = row['Phone']
        self.Fax = row['Fax']


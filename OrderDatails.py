import mysql.connector
import csv

class OrderDatails:

    def __init__(self, row):
        self.OrderID = row['OrderID']
        self.ProductID = row['ProductID']
        self.UnitPrice = row['UnitPrice']
        self.Quantity = row['Quantity']
        self.Discount = row['Discount']

import mysql.connector
import csv

class Employees:

    def __init__(self, row):
        self.EmpoyeeID = row['EmployeeID']
        self.LastName = row['LastName']
        self.FirstName = row['FristName']
        self.Title = row['Title']
        self.TitleOfCounrtesy = row['TitleOfCounrtesy']
        self.BirthDate = row['BirthDate']
        self.HireDate = row['HireDate']
        self.Address = row['Address']
        self.City = row['City']
        self.Region = row['Region']
        self.PostalCode = row['PostalCode']
        self.Country = row['Country']
        self.HomePhone = row['HomePhone']
        self.Extension = row['Extension']
        self.Photo = row['Photo']
        self.Notes = row['Notes']
        self.ReportsTo = row['ReportsTo']
        self.PhotoPath = row['PhotoPath']
        self.Salary = row['Salary']

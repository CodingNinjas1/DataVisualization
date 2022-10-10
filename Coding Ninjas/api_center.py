from urllib import response
import api_center 
import json
import mysql.connector
from fastapi import FastAPI
app= FastAPI()

# CONNECTing to DB
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
)
mycursor = mydb.cursor()
d=[]
class Api:
    def sum_of_small_bags(self):
        query = "SELECT FLOOR(SUM(`Small Bags`)) from avacado.avocado"
        mycursor.execute(query)
        for x in mycursor:
            d.append(x)
        response={'message':x}
        return response
    def sum_of_big_bags(self):
        query = "SELECT FLOOR(SUM(`Large Bags`)) from avacado.avocado"
        mycursor.execute(query)
        for x in mycursor:
            d.append(x)
        response={'message':x}
        return response    
    def sum_of_xl_bags(self):
        query = "SELECT FLOOR(SUM(`XLarge Bags`)) from avacado.avocado"
        mycursor.execute(query)
        for x in mycursor:
            d.append(x)
        response={'message':x}
        return response   
    def get_date(self):
        query = "select date from avacado.avocado"
        mycursor.execute(query)
        for x in mycursor:
            d.append(x)
        response={'message':d}
        return response 
    def get_data(self):
        query = """  SELECT YEAR(date) as SalesYear,
         MONTH(date) as SalesMonth,
         SUM(`Total Volume`) AS TotalSales
        FROM avacado.avocado a WHERE  YEAR(date) = "2015"
        GROUP BY YEAR(date), MONTH(date)
        ORDER BY YEAR(date), MONTH(date)"""
        mycursor.execute(query)
        for x in mycursor:
            d.append(x)
        response={'message':d}
        return response                      


     


# x = Api.sum_of_sm_bags()
# x.sum_of_sm_bags()       
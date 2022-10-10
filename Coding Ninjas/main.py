# import api_center 
from api_center import Api
from fastapi import FastAPI
app= FastAPI()

# CONNECTing to DB
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="admin",
# )
# mycursor = mydb.cursor()
# query = "SELECT FLOOR(SUM(`Small Bags`)) from avacado.avocado"
# X= mycursor.execute(query)
# query = "SELECT FLOOR(SUM(`Small Bags`)) from avacado.avocado"
# for x in mycursor:
#   print(x)

@app.get("/")
async def root():
    obj=Api()
    # print("hey",obj.sum_of_sm_bags)
    return  obj.sum_of_small_bags()
    # return  api_center.Api.sum_of_sm_bags()





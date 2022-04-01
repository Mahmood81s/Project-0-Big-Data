import json
import json
import pprint
from pymongo import MongoClient
import pandas as pd
import pymongo
#read file
#myjsonfile = open("jsonfile.json", 'r')

#jsondata = myjsonfile.read()

#parse

#obj=json.loads(jsondata)
myclient = MongoClient("mongodb://localhost:27017")
db = myclient["Project_0_db"]  #database
Collection = db["col_movie_3"]
#print(str(obj["firstName"]))

with open(r"C:\Users\mahmo\project_zero_cli\col_movie_3.json") as f:
    data = json.load(f)
     
    
print("----------------------------------------------")    
for doc in db.col_movie_3.find({"movieName" : "Dog"}):
    print(doc)    


import pymongo
import pandas as pd


connection = pymongo.MongoClient('localhost', 27017)
database = connection['Project_0_db']
collection = database['col_movie_3']
print(" Database connected.....")
# data = {'name':"mahmood"}
# collection.insert_one(data)
#print(database)

 







from pymongo import MongoClient

client  = MongoClient()
db = client.Project_0_db   #db = client["Project_0_db"]

collection = db.col_movie_3
doc = print(int(input("rate the movie: ")))

#doc = {"rating" : 5, "genre": "action"}
print(f"inserting the following data.......")
print(doc)
doc_id = collection.insert_one(doc).inserted_id
print(f"document successfully inserted with id {doc_id}")


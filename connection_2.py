from pymongo import MongoClient

def connection():
    client = MongoClient()   #connecto to the server
    db = client.Project_0_db  #return an object pointing to the db named project_0_db
    collections = db.list_collection_names()    
    for i in range(len(collections)):
        aCollection = collections[i]
        print(f"Collection name: {aCollection}")
        collObject = db.get_collection(aCollection)
    #for doc in collObject.find({"rating": 9}):
    #    print(doc)
    
    for doc in collObject.find({}):
        print(doc)
        
connection()        
    


    
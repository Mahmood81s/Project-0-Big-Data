import json
import pprint
from pymongo import MongoClient
import pandas as pd
import pymongo
import collections
from collections import Counter


myclient = MongoClient("mongodb://localhost:27017")
db = myclient["Project_0_db"]  #database
Collection = db["col_movie_3"]


# = open(r'C:\Users\mahmo\project_zero_cli\col_movie_3.json')  # opening JSON file

#returns JSONobject as a dictionary
#data = json.load(f)

# iterating through the json list 
#for i in data['col_movie_3']:
#    print(i)
    
#closing file 
#f.close()   

#with open(r"C:\Users\mahmo\project_zero_cli\col_movie_3.json") as f:
 #   data = json.load(f)
       
a = '{"name":"Scream", "genre":"Horror"}'

y = json.loads(a)
print("JSON string =", y)
print()
f = open (r'C:\Users\mahmo\project_zero_cli\col_movie_3.json', "r")
data = json.loads(f.read())

for i in data['col_movie_3']:
    print(i)     
"""if isinstance(data, list):
    Collection.insert_many(data)
else:
    Collection.insert_one(data) """       

df = pd.DataFrame(columns=["movieName", "Genre", "Rating"])  

df.loc[0] = ["Titanic", "Drama", 9]  
df.loc[1] = ["Toy Story", "Kids", 8] 
df.loc[2] = ["Mission Impossible", "Action", 9] 
df.loc[3] = ["Turning Red", "Kids", 6] 
df.loc[4] = ["Spy Game", "Action", 8] 
df.loc[5] = ["Cliff", "Advanture", 7] 
df.loc[6] = ["Bable", "History", 5] 
df.loc[7] = ["Batman", "Action", 8] 
df.loc[8] = ["Batman 2", "Action", 9]
df.loc[9] = ["The Endless", "Drama", 6] 
df.loc[10] = ["Luci", "Action", 7] 
df.loc[11] = ["Cheaper by the dozen", "Drama", 5] 
df.loc[12] = ["Master", "Drama", 5] 
df.loc[13] = ["The Weekend Away", "Horror", 8] 
df.loc[14] = ["No Exit", "Horror", 6] 
df.loc[15] = ["Joker", "Crime", 8] 
df.loc[16] = ["Good Time", "Drama", 6] 
df.loc[17] = ["InterStellar", "Advanture", 7]  



def mainMenu():
    print("\n  ---------Welcome to Micro Movie Menu-----------\n")
    print("0. movie list [Pandas]")
    print("1. movie list [JSON]")
    print("2. Rate your movies")
    print("3. Edit your movie list")
    print("4. Best and worst movies")
    print("5. Look up/ Filter between movie")
    print("6. Exit the app\n") 
    
    while True:

        try:
                selection = int(input("--Choose one of the options above: \n"))
                
                if selection == 0:
                    PandaList()
                    break
                
                elif selection == 1:
                    movieList()
                    break
                
            
                elif selection == 2:
                    rating()
                    #mainMenu()
                    break
            
                elif selection == 3:
                    favoriteMovies()
                    break
                
                elif selection == 4:
                    BeWor()
                    break
                elif selection ==5:
                    LookUp()
                    break
        
                elif selection == 6:
                    print("see you later!")
                    exit()    
                
                else:
                    print(" ---___----___---___Out of range___---___---___ <Enter 1-5>\n")
                    mainMenu()    
        except ValueError:
            print("\n-_-_-_-_-_-_-_Invalid entry_-_-_-_-_-_-. Please try again! :\n")
            mainMenu()

    exit    
         
       


def PandaList():
    print(df)
    anykey = input("\n--Enter anykey to return to Main Menu: \n") 
    mainMenu() 
    
def movieList():
        print("-----------Your Movie list-------------\n")
        #for i in data['col_movie_3']:
        #    print(i)
            
        for i in data['col_movie_3']:
            print(i)    
        #client = MongoClient()   #connecto to the server
        #db = client.Project_0_db  #return an object pointing to the db named project_0_db
        #collections = db.list_collection_names()    
        #for i in range(len(collections)):
        #    aCollection = collections[i]
            #print(f"Collection name: {aCollection}")
        #    collObject = db.get_collection(aCollection)
        
        
        #with open(r"C:\Users\mahmo\project_zero_cli\col_movie_3.json") as f:
        #    data = json.load(f)
        
         

        #for doc in db.col_movie_3.find({}):
        #    print(f"{doc['movieName']} | {doc['genre']} | Rating: {doc['rating']}")  
            
        
        anykey = input("\n--Enter anykey to return to Main Menu........... \n") 
        mainMenu()   

def rating():
        print("----------Edit Rating---------\n")
        client = MongoClient()   #connecto to the server
        db = client.Project_0_db  #return an object pointing to the db named project_0_db
        collections = db.list_collection_names()    
        
        pickMovie = input("--Which movie from the list you would like to update the rating?\n")
        
        for doc in db.col_movie_3.find({"movieName":pickMovie}):
            print (f"-------The current rating for {doc['movieName']} is {doc['rating']}--------- \n")
        
        rateMovie = int(input(f"--What do you rate the movie '{pickMovie}': \n"))
            
        
        db.col_movie_3.update_one(
            {"movieName": pickMovie}, 
            { "$set" : { "rating" : rateMovie}})
        print(f"\n {pickMovie}  | updated rating to :  {rateMovie}") 
            
        print(f"\n+++ You successfully updated the rating to '{rateMovie}' for the movie '{pickMovie}' +++\n")
        
        
        anykey = input("\n--Press Enter to return to Main Menu: ") 
        mainMenu() 


def favoriteMovies():
    while True:
        try:
            
            print("------------Update your movie list----------\n")
            print("--You can add/remove a movie from your list here \n") 
            client = MongoClient()   #connecto to the server
            db = client.Project_0_db  #return an object pointing to the db named project_0_db
            
            pickOp = int(input("--Would you like to\n1.add\n2.remove\n3.replace\n "))
            if pickOp == 1:
                pickOp_2 = int(input("\nWould you like to add\n1.only one\n2.two movies\n"))
                if pickOp_2 == 1:
                    pickOp_I = int(input("---Pick a unique id for your new added movie: \n"))
                        
                            
                    pickOp_N = input("---Enter the name of the new movie you want to add: \n")
                    pickOp_G = input("---Enter the genre of the new added movie: \n ") 
                    pickOp_R = int(input("---Enter the rating of the new added movie: \n")) 
                    records = {"_id" :pickOp_I,
                                "movieName" : pickOp_N,
                                "genre": pickOp_G,
                                "rating" : pickOp_R}
                    db.col_movie_3.insert_one(records) #for doc in documents:client.update_one({'_id': doc['_id']}, doc, upsert=True)
                    print(f"\n ***You have successfully added '{pickOp_N}' to your movie list***\n ")
                elif pickOp_2 == 2:
                    pickOp_I2 = int(input("--Pick a unique id for your second added movie: \n"))
                    pickOp_N2 = input("--Enter the name of the second movie you want to add: \n")
                    pickOp_G2 = input("--Enter the genre of the second added movie: \n ") 
                    pickOp_R2 = int(input(" Enter the rating of the new added movie: \n")) 
                    records2 = {"_id" :pickOp_I2,
                                "movieName" : pickOp_N2,
                                "genre": pickOp_G2,
                                "rating" : pickOp_R2}
                    db.col_movie_3.insert_one(records2)
                    print(f"\n+++ You have successfully added <{pickOp_N2}> to your movie list as well +++\n ")
            elif pickOp == 2:
                removeOp= input(" Which one your existing movies you would like to remove? \n")
                db.col_movie_3.delete_one({"movieName" : removeOp}) 
                print(f"++ You have successfully deleted the movie {removeOp} from your movie list ++ \n") 
            elif pickOp == 3:
                replaceOp = input(" Which movie name you want to change? \n")
                replaceOp2 = input(" With what movie name? \n")
                db.col_movie_3.update_one(
                {"movieName": replaceOp}, 
                { "$set" : { "movieName" : replaceOp2}})
                print(f"+++ You have successfully has changed {replaceOp} to {replaceOp2} +++ ")
            else:
                print("\nInvalid entry! enter 1-3")    
                
                
        except pymongo.errors.DuplicateKeyError:
            print("          ++++++ This id already exists ++++++ ")
            print(" ------ Please choose another id for the new movie ------\n")
        anykey = input("\n--Enter any key to return to the Main Menu........... \n") 
        mainMenu()     
def BeWor():
    client = MongoClient()
    db = client.Project_0_db
      
    
    pickBeWor = int(input(f"\n1.Popular movies\n2.Unpopular movies\n"))
    if pickBeWor == 1:
        a = db.col_movie_3.count_documents({"rating":{"$gte" :7}})
        y = json.loads(a)
        print("JSON string =", y)
        print()
        f = open (r'C:\Users\mahmo\project_zero_cli\col_movie_3.json', "r")
        data = json.loads(f.read())

        for i in data['col_movie_3']:
            print(i)
        countDoc = db.col_movie_3.count_documents({"rating":{"$gte" :7}})
        print(f"\n +++++There are {countDoc} popular movies in your list with the rating above 7  +++++\n")
        #print("\n---These are movies with the rating above 7---\n")
        for doc in db.col_movie_3.find({"rating":{"$gte":7}}): 
            print(f"{doc['movieName']} | Rating:{doc['rating']}")
            
    elif pickBeWor ==2:
        countDoc = db.col_movie_3.count_documents({"rating":{"$lte" :5}})
        print(f"\n +++++There are {countDoc} unpopular movies in your list with the rating below 5  +++++\n")
        #print("\n---These are movies with the rating below 5---\n")
        for doc in db.col_movie_3.find({"rating" :{"$lte":5}}):
            print(f"{doc['movieName']} | Rating:{doc['rating']}") 
            
    else:
        print("Invalid entry! enter 1 or 2") 
        
    anykey = input("\n--Press Enter to return to Main Menu........... \n") 
    mainMenu()                   

def LookUp():
    client = MongoClient()   #connecto to the server
    db = client.Project_0_db  #return an object pointing to the db named project_0_db
    collections = db.list_collection_names() 
    FilterNM = input(" Enter the genre of the movie you are looking for: \n")
    FilterRM= int(input(" Enter the rating you are looking for: \n"))
    for doc in db.col_movie_3.find({"$and":[{"genre" : FilterNM},{"rating" : FilterRM}]}):
        
        
        print(f"{doc['_id']} | Movie Name: {doc['movieName']}")

    anykey = input("\n--Press Enter to return to Main Menu........... \n") 
    mainMenu()    

mainMenu()
    

# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = username 
        PASS = password 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
      
        if data is not None:           
            successfulInsert = self.database.animals.insert_one(data)  # data should be dictionary             
            return(successfulInsert) #return true or false based on insert success

        else: 
            raise Exception("Nothing to save, because data parameter is empty") 

    # Create method to implement the R in CRUD.
    def read(self, query):

      if query is not None:
        mongoCursor = self.database.animals.find(query)
        return (list(mongoCursor)) #list will be empty if invalid

      else:
        raise Exception("Nothing to read, because query parameter is empty") 
        
    #Update function
    def update(self, searchFor, updateThis):
        #searchFor should be in format {"id":"1234"}
        #updateThis should be dictionary for what to update like {"$set": {"age: 1}}
        
        if searchFor is not None and updateThis is not None:
            successfulUpdate = self.database.animals.update_one(searchFor, updateThis)
            return(successfulUpdate)
        else:
            raise Exception("Nothing to update, because item to update is empty")

    #Delete function
    def delete(self, query):
        #use a query like {"id": 1} to delete item
        if query is not None:
            successfulDelete = self.database.animals.delete_one(query)
            return(successfulDelete)
            
        else:
            raise Exception("Nothing to delete, because item to delete is empty")

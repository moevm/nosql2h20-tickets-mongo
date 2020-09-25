import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.example
db.example.insert({"name":"Hello World!"})
print(db.list_collection_names())
print(db.example.find_one())
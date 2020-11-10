import pymongo

client = pymongo.MongoClient("mongodb://db:27017/")
db = client.example
db.example.insert({"name":"Hello World!"})
for db in client.list_databases():
    print(db)
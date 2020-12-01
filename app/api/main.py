import pymongo
from backend import backend
from frontend import frontend
import datetime


backend.clear_data()
backend.import_data()

backend.import_kind_of_transport('data/kind_of_transport.json')

db = pymongo.MongoClient("mongodb://db:27017/").example
print(list(db.kind_of_transport.find({})))
print(list(db.transport.find({})))

frontend.start()

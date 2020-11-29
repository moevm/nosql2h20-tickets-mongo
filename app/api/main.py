import pymongo
from backend import backend
from frontend import frontend
import datetime


backend.clear_data()
backend.import_data()

frontend.start()

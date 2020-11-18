import pymongo
from api.backend import backend
import datetime


backend.add_new_user("ddd", "ddd", "ddd", "ddd", "ddd")
backend.add_new_ticket("pes")
d = datetime.datetime.strptime("2017-10-13T10:53:53.000Z", "%Y-%m-%dT%H:%M:%S.000Z")
backend.add_new_trip("ddd", "ddd", d, "ddd", "pes", "ddd", "ddd", "pes")

print(backend.find_trip("ddd", "ddd", d, "pes"))


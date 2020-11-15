import pymongo


def add_new_user(email, pass_, ph_num, fio, passp):
    db = pymongo.MongoClient("mongodb://db:27017/").example
    db.user.insert([{"email": email,
                     "password": pass_, "phone_num": ph_num, "fio": fio, "passport": passp, "tickets": []}])


def add_new_trip(from_, to, depar_date, arrival_date, transport_id, distance, price, name):
    db = pymongo.MongoClient("mongodb://db:27017/").example
    id = db.ticket.find_one({"name": name}).get('_id')
    db.trip.insert([{"from": from_, "to": to, "depar_date": depar_date, "arrival_date": arrival_date,
                     "transport_id": transport_id, "ticket_id": id, "distance": distance,
                     "price": price}])


def add_trip_to_user(user_id, trip_id):
    db = pymongo.MongoClient("mongodb://db:27017/").example
    db.user.update_one({'_id': user_id}, {"$push": {"tickets": trip_id}})


def add_new_ticket(name):
    db = pymongo.MongoClient("mongodb://db:27017/").example
    db.ticket.insert([{"name": name}])


def add_new_transport(name, kind_of_transport, number_of_seats):
    db = pymongo.MongoClient("mongodb://db:27017/").example
    db.transport.insert([{"name": name, "kind_of_transport": kind_of_transport, "number_of_seats": number_of_seats}])

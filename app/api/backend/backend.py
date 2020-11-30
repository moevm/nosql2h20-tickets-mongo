import pymongo
import datetime
import json
from bson.objectid import ObjectId


def clear_data():
    db = pymongo.MongoClient("mongodb://db:27017/").example
    db.user.remove()
    db.trip.remove()
    db.ticket.remove()
    db.transport.remove()
    db.cities.remove()


def import_data():
    import_cities('data/cities.json')
    import_trans('data/transport.json')
    import_ticket('data/tickets.json')
    import_trip('data/trip.json')


def add_new_user(email, pass_, ph_num, fio, passp):
    db = pymongo.MongoClient("mongodb://db:27017/").example
    e = list(db.user.find({"email": email}))
    p = list(db.user.find({"password": pass_}))
    if len(e) > 0 or len(p) > 0:
        return "user has already exist"
    else:
        db.user.insert([{"email": email,
                         "password": pass_, "phone_num": ph_num, "fio": fio, "passport": passp, "tickets": []}])


def add_new_trip(from_, to, depar_date, arrival_date, tran_name, distance, price, ticket_name):
    db = pymongo.MongoClient("mongodb://db:27017/").example
    db.trip.insert([{"from": from_, "to": to, "depar_date": depar_date, "arrival_date": arrival_date,
                     "transport_id": get_transport_type_id(tran_name), "ticket_id": get_ticket_type_id(ticket_name),
                     "distance": distance,
                     "price": price}])


def authorization(email, password):
    db = pymongo.MongoClient("mongodb://db:27017/").example
    u = list(db.user.find({"email": email, 'password': password}))
    return len(u) > 0


def get_cities():
    db = pymongo.MongoClient("mongodb://db:27017/").example
    cities = db.cities.find({})
    cities_ = []
    for x in cities:
        cities_.append(x["city"])
    return cities_


def get_transport():
    db = pymongo.MongoClient("mongodb://db:27017/").example
    transport = db.transport.find({})
    transport_ = []
    for x in transport:
        transport_.append(x["name"])
    return transport_


def get_tickets():
    db = pymongo.MongoClient("mongodb://db:27017/").example
    trip = db.trip.find({})
    trip_ = []
    for x in trip:
        trip_.append(x["name"])
    return trip_


def add_city(city):
    db = pymongo.MongoClient("mongodb://db:27017/").example
    cities = get_cities()
    if not city in cities:
        db.cities.insert([{"city": city}])


def export_cities(outfile):
    db = pymongo.MongoClient("mongodb://db:27017/").example
    cities_list = list(db.cities.find({}))
    for x in cities_list:
        x.pop('_id')
    with open(outfile, 'w') as outfile:
        print(cities_list)
        json.dump(cities_list, outfile)


def import_cities(outfile):
    with open(outfile) as json_file:
        cities = json.load(json_file)
        for x in cities:
            add_city(x['city'])


def find_trip(from_, to, depar_date, name):
    db = pymongo.MongoClient("mongodb://db:27017/").example
    trips = db.trip.find({"depar_date": {"$gte": depar_date}, "from": from_, "to": to})
    mas1 = db.trip.find({"depar_date": {"$gte": depar_date}, "from": from_})
    mas2 = list()
    for x in mas1:
        e = list(db.trip.find({"from": x.get('to'), "to": to}))
        if len(e):
            if (e[0]['depar_date'] > x.get('arrival_date')):
                mas2.append([x, e])
    return [trips, mas2]


def get_ticket_type_id(name):
    db = pymongo.MongoClient("mongodb://db:27017/").example
    return db.ticket.find_one({"name": name}).get('_id')


def get_ticket_type_name(id):
    db = pymongo.MongoClient("mongodb://db:27017/").example
    return db.ticket.find_one({'_id': ObjectId(str(id))}).get('name')


def get_transport_type_id(name):
    db = pymongo.MongoClient("mongodb://db:27017/").example
    return db.transport.find_one({"name": name}).get('_id')


def get_transport_type_name(id):
    db = pymongo.MongoClient("mongodb://db:27017/").example
    return db.transport.find_one({'_id': ObjectId(str(id))}).get('name')


def add_trip_to_user(user_id, trip_id):
    db = pymongo.MongoClient("mongodb://db:27017/").example
    db.user.update_one({'_id': user_id}, {"$push": {"tickets": trip_id}})


def add_new_ticket(name):
    db = pymongo.MongoClient("mongodb://db:27017/").example
    db.ticket.insert([{"name": name}])


def add_new_transport(name, kind_of_transport, number_of_seats):
    db = pymongo.MongoClient("mongodb://db:27017/").example
    db.transport.insert([{"name": name, "kind_of_transport": kind_of_transport, "number_of_seats": number_of_seats}])


def export_trans(outfile):
    db = pymongo.MongoClient("mongodb://db:27017/").example
    trans_list = list(db.transport.find({}))
    for x in trans_list:
        x.pop('_id')
    with open(outfile, 'w') as outfile:
        json.dump(trans_list, outfile)


def import_trans(outfile):
    with open(outfile) as json_file:
        trans = json.load(json_file)
        for x in trans:
            add_new_transport(x['name'], x['kind_of_transport'], x['number_of_seats'])


def export_ticket(outfile):
    db = pymongo.MongoClient("mongodb://db:27017/").example
    tickets_list = list(db.ticket.find({}))
    for x in tickets_list:
        x.pop('_id')
    with open(outfile, 'w') as outfile:
        json.dump(tickets_list, outfile)


def import_ticket(outfile):
    with open(outfile) as json_file:
        ticket = json.load(json_file)
        for x in ticket:
            add_new_ticket(x['name'])


def export_trip(outfile):
    db = pymongo.MongoClient("mongodb://db:27017/").example
    trip_list = list(db.trip.find({}))
    for x in trip_list:
        x.pop('_id')
        x['transport_name'] = x.pop('transport_id')
        x["transport_name"] = get_transport_type_name(x['transport_name'])
        x['ticket_name'] = x.pop('ticket_id')
        x["ticket_name"] = get_ticket_type_name(x['ticket_name'])
        x["depar_date"] = x["depar_date"].strftime("%Y-%m-%dT%H:%M:%S.000Z")
        x["arrival_date"] = x["arrival_date"].strftime("%Y-%m-%dT%H:%M:%S.000Z")
    with open(outfile, 'w') as outfile:
        json.dump(trip_list, outfile)


def import_trip(outfile):
    with open(outfile) as json_file:
        trip_list = json.load(json_file)
        for x in trip_list:
            d1 = datetime.datetime.strptime(x['depar_date'], "%Y-%m-%dT%H:%M:%S.000Z")
            d2 = datetime.datetime.strptime(x['arrival_date'], "%Y-%m-%dT%H:%M:%S.000Z")
            add_new_trip(x['from'], x['to'], d1, d2, x['transport_name'],
                         x['distance'], x['price'], x['ticket_name'])

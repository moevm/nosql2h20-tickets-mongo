import pymongo
import datetime
import json
from bson.objectid import ObjectId
from pymongo import MongoClient


def clear_data():
    client = MongoClient()
    db = client.example

    #db = pymongo.MongoClient("mongodb://db:27017/").example
    db.user.remove()
    db.trip.remove()
    db.ticket.remove()
    db.transport.remove()
    db.cities.remove()
    db.kind_of_transport.remove()


def import_data():
    import_cities('data/cities.json')
    import_kind_of_transport('data/kind_of_transport.json')
    import_trans('data/transport.json')
    import_ticket('data/tickets.json')
    import_trip('data/trip.json')


def add_new_user(email, pass_, ph_num, fio, passp, tickets):
    client = MongoClient()
    db = client.example
    e = list(db.user.find({"email": email}))
    p = list(db.user.find({"password": pass_}))
    if len(e) > 0 or len(p) > 0:
        return "user has already exist"
    else:
        db.user.insert([{"email": email,
                         "password": pass_, "phone_num": ph_num, "fio": fio, "passport": passp, "tickets": tickets}])


def add_new_trip(from_, to, depar_date, arrival_date, tran_name, distance, price, ticket_name):
    client = MongoClient()
    db = client.example
    cities = get_cities()
    if from_ not in cities:
        add_city(from_)
    if to not in cities:
        add_city(to)
    db.trip.insert([{"from": from_, "to": to, "depar_date": depar_date, "arrival_date": arrival_date,
                     "transport_id": get_transport_type_id(tran_name), "ticket_id": get_ticket_type_id(ticket_name),
                     "distance": distance,
                     "price": price}])


def get_user_by_id(user_id):
    client = MongoClient()
    db = client.example
    u = list(db.user.find({"_id": ObjectId(str(user_id))}))
    return u[0]


def get_user_trips_by_email_pass(email, password):
    client = MongoClient()
    db = client.example
    u = list(db.user.find({"email": email, 'password': password}))
    return u[0]["tickets"]


def get_user_id(email, password):
    client = MongoClient()
    db = client.example
    u = list(db.user.find({"email": email, 'password': password}))
    return u[0]['_id']


def authorization(email, password):
    client = MongoClient()
    db = client.example
    u = list(db.user.find({"email": email, 'password': password}))
    return len(u) > 0


def get_cities():
    client = MongoClient()
    db = client.example
    cities = db.cities.find({})
    cities_ = []
    for x in cities:
        cities_.append(x["city"])
    return cities_


def get_transport():
    client = MongoClient()
    db = client.example
    transport = db.transport.find({})
    transport_ = []
    for x in transport:
        transport_.append(x["name"])
    return transport_


def get_kind_of_transport(id):
    client = MongoClient()
    db = client.example
    return db.transport.find_one({'_id': ObjectId(str(id))}).get('kind_of_transport')


def get_trips():
    client = MongoClient()
    db = client.example
    return list(db.trip.find({}))


def get_tickets():
    client = MongoClient()
    db = client.example
    ticket = db.ticket.find({})
    ticket_ = []
    for x in ticket:
        ticket_.append(x["name"])
    return ticket_


def add_city(city):
    client = MongoClient()
    db = client.example
    cities = get_cities()
    if not city in cities:
        db.cities.insert([{"city": city}])


def export_cities(outfile):
    client = MongoClient()
    db = client.example
    cities_list = list(db.cities.find({}))
    for x in cities_list:
        x.pop('_id')
    with open(outfile, 'w') as outfile:
        json.dump(cities_list, outfile)


def import_cities(outfile):
    with open(outfile) as json_file:
        cities = json.load(json_file)
        for x in cities:
            add_city(x['city'])


def add_kind_of_transport(name):
    client = MongoClient()
    db = client.example
    db.kind_of_transport.insert([{"name": name}])


def get_kind_of_transport_list():
    client = MongoClient()
    db = client.example
    transport = db.kind_of_transport.find({})
    transport_ = []
    for x in transport:
        transport_.append(x["name"])
    return transport_

def get_user_data():
    client = MongoClient()
    db = client.example
    user_list = list(db.user.find({}))
    trip_list = list(db.trip.find({}))
    user = []
    trip_indixes = []
    keys = list(db.user.find_one({}))
    keys.remove('_id')
    keys[keys.index('tickets')] = 'trips'

    for i, x in enumerate(trip_list, start=1):
        trip_indixes.append([i, x['_id']])
    for x in user_list:
        x.pop('_id')
        tickets = []
        for y in x['tickets']:
            for z in trip_indixes:
                if z[1] == y:
                    tickets.append(z[0])
        str_ = ''
        if len(tickets):
            for i in tickets:
                str_ = str_ + ' ' + str(i)
        else:
            str_ = 'No trips'
        #x['tickets'] = tickets
        user.append([x['email'],x['password'],x['phone_num'],x['fio'],x['passport'],str(str_)])
    return {"keys": keys, "data": user}


def get_ticket_data():
    client = MongoClient()
    db = client.example
    tickets_list = list(db.ticket.find({}))
    ticket = []
    keys = list(db.ticket.find_one({}))
    keys.remove('_id')
    for x in tickets_list:
        x.pop('_id')
        ticket.append([x["name"]])
    return {"keys": keys, "data": ticket}


def get_kind_of_transport_data():
    client = MongoClient()
    db = client.example
    tr_list = list(db.kind_of_transport.find({}))
    tr = []
    keys = list(db.kind_of_transport.find_one({}))
    keys.remove('_id')
    for x in tr_list:
        x.pop('_id')
        tr.append([x['name']])
    return {"keys": keys, "data": tr}


def get_transp_data():
    client = MongoClient()
    db = client.example
    trans_list = list(db.transport.find({}))
    transp = []
    keys = list(db.transport.find_one({}))
    keys.remove('_id')
    for x in trans_list:
        x["kind_of_transport"] = get_kind_of_transport_name(x["kind_of_transport"])
        x.pop('_id')
        transp.append([x["name"], x["kind_of_transport"], x["number_of_seats"]])
    return {"keys": keys, "data": transp}


def get_trip_keys():
    client = MongoClient()
    db = client.example
    keys = list(db.trip.find_one({}))
    keys.remove('_id')
    keys[4] = 'transport name'
    keys[5] = 'ticket name'
    return keys


def get_ticket_list(id_list):
    client = MongoClient()
    db = client.example
    trip_list = []
    if id_list is not None:
        trip_list = []
        for x in id_list:
            temp = list(db.trip.find({"_id": ObjectId(str(x))}))[0]
            trip_list.append(temp)

    else:
        trip_list = list(db.trip.find({}))

    trips = []
    keys = list(db.trip.find_one({}))
    keys.remove('_id')
    keys[keys.index('transport_id')] = 'transport name'
    keys[keys.index('ticket_id')] = 'ticket name'

    for x in trip_list:
        x.pop('_id')
        x['transport_name'] = x.pop('transport_id')
        x["transport_name"] = get_transport_type_name(x['transport_name'])
        x['ticket_name'] = x.pop('ticket_id')
        x["ticket_name"] = get_ticket_type_name(x['ticket_name'])
        x["depar_date"] = x["depar_date"].strftime("%Y-%m-%d %H:%M:%S")
        x["arrival_date"] = x["arrival_date"].strftime("%Y-%m-%d %H:%M:%S")
        trips.append(
            [x['from'], x['to'], x['depar_date'], x['arrival_date'], x['transport_name'],
             x['ticket_name'], x['distance'], x['price']])
    print("trip", trips)

    return {"keys": keys, "trip": trips}


def get_kind_of_transport_id(name):
    client = MongoClient()
    db = client.example
    return db.kind_of_transport.find_one({"name": name}).get('_id')


def get_kind_of_transport_name(id):
    client = MongoClient()
    db = client.example
    return db.kind_of_transport.find_one({"_id": id}).get('name')


def find_trip(from_, to, depar_date, tickets_names):
    client = MongoClient()
    db = client.example
    depar_date_1 = datetime.datetime.strptime(depar_date, "%Y-%m-%dT%H:%M:%S.000Z") + datetime.timedelta(hours=23,
                                                                                                         minutes=59)

    print("++++++++++++++", depar_date, depar_date_1.strftime("%Y-%m-%dT%H:%M:%S.000Z"))

    # trips = db.trip.find({
    #     "depar_date": {"$gte": datetime.datetime.strptime(depar_date, "%Y-%m-%dT%H:%M:%S.000Z"),
    #     "$lte": depar_date_1.strftime("%Y-%m-%dT%H:%M:%S.000Z")}, "from": from_, "to": to
    # })

    # mas1 = db.trip.find({
    #     "depar_date": {"$gte": datetime.datetime.strptime(depar_date, "%Y-%m-%dT%H:%M:%S.000Z"),
    #             "$lt":depar_date_1.strftime("%Y-%m-%dT%H:%M:%S.000Z")}, "from": from_
    # })

    trips = db.trip.find(
        {"depar_date": {"$gte": datetime.datetime.strptime(depar_date, "%Y-%m-%dT%H:%M:%S.000Z")}, "from": from_,
         "to": to})
    mas1 = db.trip.find(
        {"depar_date": {"$gte": datetime.datetime.strptime(depar_date, "%Y-%m-%dT%H:%M:%S.000Z")}, "from": from_})
    data = []
    for x in mas1:
        if x["depar_date"].strftime("%Y-%m-%dT%H:%M:%S.000Z") > depar_date_1.strftime("%Y-%m-%dT%H:%M:%S.000Z") \
                or x["depar_date"].strftime("%Y-%m-%dT%H:%M:%S.000Z") < depar_date:
            continue
        e = list(db.trip.find({"from": x.get('to'), "to": to}))
        if len(e):
            if (e[0]['depar_date'] > x.get('arrival_date')):
                e[0]['transport_name'] = e[0].pop('transport_id')
                trans_seats_e = db.transport.find_one({'_id': ObjectId(str(e[0]['transport_name']))}).get(
                    'number_of_seats')
                e[0]["transport_name"] = get_transport_type_name(e[0]['transport_name'])
                e[0]['ticket_name'] = e[0].pop('ticket_id')
                e[0]["ticket_name"] = get_ticket_type_name(e[0]['ticket_name'])
                e[0]["depar_date"] = e[0]["depar_date"].strftime("%Y-%m-%d %H:%M:%S")
                e[0]["arrival_date"] = e[0]["arrival_date"].strftime("%Y-%m-%d %H:%M:%S")
                x['transport_name'] = x.pop('transport_id')
                trans_seats_x = db.transport.find_one({'_id': ObjectId(str(x['transport_name']))}).get(
                    'number_of_seats')
                x["transport_name"] = get_transport_type_name(x['transport_name'])
                x['ticket_name'] = x.pop('ticket_id')
                x["ticket_name"] = get_ticket_type_name(x['ticket_name'])
                x["depar_date"] = x["depar_date"].strftime("%Y-%m-%d %H:%M:%S")
                x["arrival_date"] = x["arrival_date"].strftime("%Y-%m-%d %H:%M:%S")
                if trans_seats_e <= 0 or trans_seats_x <= 0:
                    continue
                if len(tickets_names):
                    if x['ticket_name'] in tickets_names and e[0]["ticket_name"] in tickets_names:
                        data.append([[x['_id'], x['from'], x['to'], x['depar_date'], x['arrival_date'],
                                      x['transport_name'], x['ticket_name'],
                                      x['distance'], x['price']],
                                     [e[0]['_id'], e[0]['from'], e[0]['to'], e[0]['depar_date'], e[0]['arrival_date'],
                                      e[0]['transport_name'], e[0]['ticket_name'], e[0]['distance'], e[0]['price']]])
                else:
                    data.append([[x['_id'], x['from'], x['to'], x['depar_date'], x['arrival_date'], x['transport_name'],
                                  x['ticket_name'],
                                  x['distance'], x['price']],
                                 [e[0]['_id'], e[0]['from'], e[0]['to'], e[0]['depar_date'], e[0]['arrival_date'],
                                  e[0]['transport_name'], e[0]['ticket_name'], e[0]['distance'], e[0]['price']]])
    for x in trips:
        x['transport_name'] = x.pop('transport_id')
        trans_seats_x = db.transport.find_one({'_id': ObjectId(str(x['transport_name']))}).get('number_of_seats')
        print("COMPARE", x["depar_date"].strftime("%Y-%m-%dT%H:%M:%S.000Z"),
              depar_date_1.strftime("%Y-%m-%dT%H:%M:%S.000Z"), depar_date)
        if trans_seats_x <= 0 or x["depar_date"].strftime("%Y-%m-%dT%H:%M:%S.000Z") > depar_date_1.strftime(
                "%Y-%m-%dT%H:%M:%S.000Z") \
                or x["depar_date"].strftime("%Y-%m-%dT%H:%M:%S.000Z") < depar_date:
            continue
        x["transport_name"] = get_transport_type_name(x['transport_name'])
        x['ticket_name'] = x.pop('ticket_id')
        x["ticket_name"] = get_ticket_type_name(x['ticket_name'])
        x["depar_date"] = x["depar_date"].strftime("%Y-%m-%d %H:%M:%S")
        x["arrival_date"] = x["arrival_date"].strftime("%Y-%m-%d %H:%M:%S")
        if len(tickets_names):
            if x['ticket_name'] in tickets_names:
                data.append([x['_id'], x['from'], x['to'], x['depar_date'], x['arrival_date'], x['transport_name'],
                             x['ticket_name'],
                             x['distance'], x['price']])
        else:
            data.append([x['_id'], x['from'], x['to'], x['depar_date'], x['arrival_date'], x['transport_name'],
                         x['ticket_name'],
                         x['distance'], x['price']])
    return data


def stat(depar_date_1, depar_date_2):
    client = MongoClient()
    db = client.example
    if depar_date_1 == None and depar_date_2 == None:
        trips = db.trip.find({})
    else:
        trips = db.trip.find({"depar_date": {"$gte": depar_date_1, "$lt": depar_date_2}})
    return list(trips)


def get_ticket_type_id(name):
    client = MongoClient()
    db = client.example
    return db.ticket.find_one({"name": name}).get('_id')


def get_ticket_type_name(id):
    client = MongoClient()
    db = client.example
    return db.ticket.find_one({'_id': ObjectId(str(id))}).get('name')


def get_transport_type_id(name):
    client = MongoClient()
    db = client.example
    return db.transport.find_one({"name": name}).get('_id')


def get_transport_type_name(id):
    client = MongoClient()
    db = client.example
    return db.transport.find_one({'_id': ObjectId(str(id))}).get('name')


def add_trip_to_user(user_id, trip_id):
    client = MongoClient()
    db = client.example
    trans_id = db.trip.find_one({'_id': ObjectId(str(trip_id))}).get('transport_id')
    trans_seats = db.transport.find_one({'_id': ObjectId(str(trans_id))}).get('number_of_seats')
    db.user.update_one({'_id': ObjectId(str(user_id))}, {"$push": {"tickets": ObjectId(str(trip_id))}})
    db.transport.update_one({'_id': ObjectId(str(trans_id))}, {'$set': {'number_of_seats': trans_seats - 1}},
                            upsert=False)


def add_new_ticket(name):
    client = MongoClient()
    db = client.example
    db.ticket.insert([{"name": name}])


def add_new_transport(name, kind_of_transport, number_of_seats):
    client = MongoClient()
    db = client.example
    k_trans = get_kind_of_transport_list()
    if kind_of_transport not in k_trans:
        add_kind_of_transport(kind_of_transport)
    db.transport.insert([{"name": name, "kind_of_transport": get_kind_of_transport_id(kind_of_transport),
                          "number_of_seats": number_of_seats}])


def export_trans(outfile):
    client = MongoClient()
    db = client.example
    trans_list = list(db.transport.find({}))
    for x in trans_list:
        x["kind_of_transport"] = get_kind_of_transport_name(x["kind_of_transport"])
        x.pop('_id')
    with open(outfile, 'w') as outfile:
        json.dump(trans_list, outfile)


def import_trans(outfile):
    with open(outfile) as json_file:
        trans = json.load(json_file)
        for x in trans:
            add_new_transport(x['name'], x['kind_of_transport'], x['number_of_seats'])


def export_ticket(outfile):
    client = MongoClient()
    db = client.example
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


def export_kind_of_transport(outfile):
    client = MongoClient()
    db = client.example
    tr_list = list(db.kind_of_transport.find({}))
    for x in tr_list:
        x.pop('_id')
    with open(outfile, 'w') as outfile:
        json.dump(tr_list, outfile)


def import_kind_of_transport(outfile):
    with open(outfile) as json_file:
        k_trans = json.load(json_file)
        for x in k_trans:
            add_kind_of_transport(x['name'])


def import_database(outfile):
    client = MongoClient()
    db = client.example
    data = []
    trip_indixes = []
    with open(outfile) as json_file:
        data = json.load(json_file)
    print(data)

    for x in data['cities']:
        add_city(x['city'])

    for x in data['kind_of_transport']:
        print(x['name'])
        add_kind_of_transport(x['name'])

    for x in data['transport']:
        add_new_transport(x['name'], x['kind_of_transport'], x['number_of_seats'])

    for x in data['ticket']:
        add_new_ticket(x['name'])

    for x in data['trip']:
        d1 = datetime.datetime.strptime(x['depar_date'], "%Y-%m-%dT%H:%M:%S.000Z")
        d2 = datetime.datetime.strptime(x['arrival_date'], "%Y-%m-%dT%H:%M:%S.000Z")
        add_new_trip(x['from'], x['to'], d1, d2, x['transport_name'],
                     x['distance'], x['price'], x['ticket_name'])
        last_ins = list(db.trip.find({}))
        trip_indixes.append([x['index'],last_ins[len(last_ins)-1]['_id']])

    for x in data['user']:
        tickets = []
        for y in x['tickets']:
            for z in trip_indixes:
                if z[0] == y:
                    tickets.append(z[1])
        x['tickets'] = tickets
        add_new_user(x['email'], x['password'], x['phone_num'], x['fio'], x['passport'], x['tickets'])


def export_database(outfile):
    client = MongoClient()
    db = client.example
    cities_list = list(db.cities.find({}))
    tr_list = list(db.kind_of_transport.find({}))
    trans_list = list(db.transport.find({}))
    tickets_list = list(db.ticket.find({}))
    trip_list = list(db.trip.find({}))
    user_list = list(db.user.find({}))
    trip_indixes = []

    for x in cities_list:
        x.pop('_id')
    for x in tr_list:
        x.pop('_id')
    for x in trans_list:
        x["kind_of_transport"] = get_kind_of_transport_name(x["kind_of_transport"])
        x.pop('_id')
    for x in tickets_list:
        x.pop('_id')
    for i, x in enumerate(trip_list, start=1):
        trip_indixes.append([i, x.pop('_id')])
        x['index'] = i
        x['transport_name'] = x.pop('transport_id')
        x["transport_name"] = get_transport_type_name(x['transport_name'])
        x['ticket_name'] = x.pop('ticket_id')
        x["ticket_name"] = get_ticket_type_name(x['ticket_name'])
        x["depar_date"] = x["depar_date"].strftime("%Y-%m-%dT%H:%M:%S.000Z")
        x["arrival_date"] = x["arrival_date"].strftime("%Y-%m-%dT%H:%M:%S.000Z")
    for x in user_list:
        x.pop('_id')
        tickets = []
        for y in x['tickets']:
            for z in trip_indixes:
                if z[1] == y:
                    tickets.append(z[0])
        x['tickets'] = tickets

    with open(outfile, 'w') as outfile:
        json.dump({"cities": cities_list, "kind_of_transport": tr_list, "transport": trans_list,
                   "ticket": tickets_list, "trip": trip_list, "user": user_list}, outfile)


def export_trip(outfile):
    client = MongoClient()
    db = client.example
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

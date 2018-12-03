import pymongo
import json
import re


def db_connection(mongodb_url):
    client = pymongo.MongoClient(mongodb_url,
                                 connectTimeoutMS=30000,
                                 socketTimeoutMS=None,
                                 socketKeepAlive=True)
    return client


def insert_data(client, collection, data):
    db = client.get_default_database()
    db[collection].insert_one(data)



def get_all_data_from_collection(client, collection_name):
    db = client.get_default_database()
    cursor = db[collection_name].find()
    ret_list = []
    for doc in cursor:
        ret_list.append(doc)
    return ret_list



def get_name_list_from_collection(client, collection_name):
    db = client.get_default_database()
    cursor = db[collection_name].find({'num':{'$gt':0}}).sort([('num',1)])
    ret_list = []
    for doc in cursor:
        ret_list.append(doc['user'])
    return ret_list



def get_user_from_collection_by_name(client, collection_name, name):
    db = client.get_default_database()
    cursor = db[collection_name].find({'user':re.compile(name)}).sort([('num', 1)])
    ret_list = []
    for doc in cursor:
        if doc['num']>0:
            ret_list.append(doc)
    return ret_list



def get_user_detail_by_name(client, collection_name, name):
    db = client.get_default_database()
    cursor = db[collection_name].find({'user':name})
    ret_list = []
    for doc in cursor:
        ret_list.append(doc)
    print(ret_list)
    return ret_list



def edit_user_detail_by_name(client, collection_name, name, set_json):
    db = client.get_default_database()
    db[collection_name].update(
        {"user": name},
        {"$set": set_json}
    )



def edit_fee_list(client, collection_name, insert_json):
    db = client.get_default_database()
    db[collection_name].insert(insert_json)



def get_feeList_from_collection_by_name(client, collection_name, name):
    db = client.get_default_database()
    cursor = db[collection_name].find({"user":name}).sort([('date', -1)])
    ret_list = []
    for doc in cursor:
        ret_list.append(doc)
    return ret_list



def get_data_from_collection_by_country(client, collection_name, country):
    db = client.get_default_database()
    cursor = db[collection_name].find({"country":country})
    ret_list = []
    for doc in cursor:
        ret_list.append(doc)
    return ret_list
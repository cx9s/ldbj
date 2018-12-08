import pymongo
from script.config import MONGODB_URI

def connectDB():
    client = pymongo.MongoClient(MONGODB_URI,
                                 connectTimeoutMS = 30000,
                                 socketTimeoutMS = None,
                                 socketKeepAlive = True)
    db = client.get_default_database()
    return  db


#player model
"""
{
    "_id": {
        "$oid": "5b151ad7f8f1d01911d487e4"
    },
    "name": "马熙",
    "num": 81,
    "dob": "1983-08-01",
    "position": [],
    "phone": 13401135828,
    "addr": ""
}
"""

class Player:
    def __init__(self):
        self.db = connectDB()
        self.collection = self.db['player']

    def insertOne(self, insExp):
        self.collection.insert_one(insExp)
        insExp.__delitem__('_id')
        return insExp

    def getItems(self, itemName, sortExp):
        cursor = self.collection.find({'num':{'$gt':0}}).sort(sortExp)
        res_list = []
        for item in cursor:
            res_list.append(item[itemName])
        return res_list

    def get(self, queryExp):
        cursor = self.collection.find(queryExp)
        res_list = []
        for item in cursor:
            res_list.append(item)
        return res_list

    def getAndSort(self, queryExp, sortExp):
        cursor = self.collection.find(queryExp).sort(sortExp)
        res_list = []
        for item in cursor:
            res_list.append(item)
        return res_list

    def update(self, queryExp, setExp):
        self.collection.update(queryExp,{'$set': setExp})

    def delete(self, queryExp):
        self.collection.remove(queryExp)


#fee model
"""
{
    "_id": {
        "$oid": "5b15574c2ee2031d58849e51"
    },
    "name": "陈譞",
    "date": "2012-03-10",
    "loc": "奥林匹克森林公园",
    "amount": 100
}
"""

class Fee:
    def __init__(self):
        self.db = connectDB()
        self.collection = self.db['fee']

    def insert(self, insExp):
        self.collection.insert(insExp)
        for row in insExp:
            row.__delitem__('_id')
        return insExp

    def getAndSort(self, queryExp, sortExp):
        cursor = self.collection.find(queryExp).sort(sortExp)
        res_list = []
        for item in cursor:
            res_list.append(item)
        return res_list

    def update(self, queryExp, setExp):
        self.collection.update(queryExp,{'$set': setExp})

    def delete(self, queryExp):
        self.collection.remove(queryExp)
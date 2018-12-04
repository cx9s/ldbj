import pymongo
from script.config import MONGODB_URI

def connectDB():
    client = pymongo.MongoClient(MONGODB_URI,
                                 connectTimeoutMS = 30000,
                                 socketTimeoutMS = None,
                                 socketKeepAlive = True)
    db = client.get_default_database()
    return  db


#user model
"""
{
    "_id": {
        "$oid": "5b151ad7f8f1d01911d487e4"
    },
    "user": "马熙",
    "num": 81,
    "dob": "1983-08-01",
    "position": [],
    "phone": 13401135828,
    "addr": ""
}
"""

class User:
    def __init__(self):
        self.db = connectDB()
        self.collection = self.db['users']

    def getItems(self, itemName, sortExp):
        cursor = self.collection.find({'num':{'$gt':0}}).sort(sortExp)
        res_list = []
        for item in cursor:
            res_list.append(item[itemName])
        return res_list

    def get(self, queryExp, sortExp):
        cursor = self.collection.find(queryExp).sort(sortExp)
        res_list = []
        for item in cursor:
            res_list.append(item)
        return res_list

    def update(self, queryExp, setExp):
        self.collection.update(queryExp,setExp)


#fee model
"""
{
    "_id": {
        "$oid": "5b15574c2ee2031d58849e51"
    },
    "user": "陈譞",
    "date": "2012-03-10",
    "loc": "奥林匹克森林公园",
    "amount": 100
}
"""

class Fee:
    def __init__(self):
        self.db = connectDB()
        self.collection = self.db['fee']

    def insert(self, insExt):
        self.collection.insert(insExt)

    def get(self, queryExp, sortExp):
        cursor = self.collection.find(queryExp).sort(sortExp)
        res_list = []
        for item in cursor:
            res_list.append(item)
        return res_list
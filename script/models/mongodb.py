import pymongo
from script.config import MONGODB_URI
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_login import UserMixin
import json
import uuid


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


#user model
"""
{
    "_id": {
        "$oid": "5b15574c2ee2031d58849e51"
    },
    "username": "admin",
    "password": "XXXXXXXXXX",
    "id": "XXXXXXXXX"
}
"""
# save user name and password_hash

class User(UserMixin):
    def __init__(self, username):
        self.db = connectDB()
        self.collection = self.db['user']
        self.username = username
        self.password_hash = self.get_password_hash()
        self.id = self.get_id()

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    #set password and insert user in db
    @password.setter
    def password(self, password):
        """save user name, id and password hash to db"""
        self.password_hash = generate_password_hash(password)
        if self.exist():
            return self.username + ' has existed.'
        else:
            insExp = {
                "id": self.id,
                "username": self.username,
                "password": self.password_hash
            }
            self.collection.insert_one(insExp)
            return self.username + ' create successfully.'

    def exist(self):
        cursor = self.collection.find({'username':self.username})
        res_list = []
        for item in cursor:
            res_list.append(item)
        if len(res_list) != 0:
            return True
        else:
            return False

    def verify_password(self, password):
        if self.password_hash is None:
            return False
        return check_password_hash(self.password_hash, password)

    def get_password_hash(self):
        """try to get password hash from db.

        :return password_hash: if the there is corresponding user in
                the db, return password hash.
                None: if there is no corresponding user, return None.
        """
        cursor = self.collection.find({'username': self.username})
        res_list = []
        for item in cursor:
            res_list.append(item)
        if len(res_list) != 0:
            return res_list[0]['password']
        else:
            return None

    def get_id(self):
        """get user id from profile file, if not exist, it will
        generate a uuid for the user.
        """
        if not self.username:
            return None
        cursor = self.collection.find({'username': self.username})
        res_list = []
        for item in cursor:
            res_list.append(item)
        if len(res_list) != 0:
            return res_list[0]['id']
        else:
            return str(uuid.uuid4())


    #@staticmethod
    def get(self, user_id):
        """try to return user_id corresponding User object.
        This method is used by load_user callback function
        """
        if not user_id:
            return None
        cursor = self.collection.find({'id': user_id})
        res_list = []
        for item in cursor:
            res_list.append(item)
        if len(res_list) != 0:
            uname = res_list[0]['username']
            return User(uname)
        return None
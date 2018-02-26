'''
Created on Feb 19, 2018

@author: Eric
'''

import datetime
import pymongo
from pymongo import MongoClient


client = MongoClient()
db = client.mydb
Users = db.users

current_date = datetime.datetime.now()

print (current_date)

olddate = datetime.datetime(2009, 8, 11)
#uid = Users.insert({"username" : "newdude", "password":"newpass", "date" : current_date})

print(Users.find({"username" : {"$ne" : "newdude"}}).count())

Users.create_index([("username", pymongo.ASCENDING)])
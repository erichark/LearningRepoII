'''
Created on Feb 5, 2018

@author: Eric
'''
import json 
import os


if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size !=0:
    old_file = open("./ages.json", "r+")
    data = json.loads(old_file.read())
    print("Current age is", data["age"], "---adding a year.")
    data["age"] = int(data["age"]) + 1
    data["age"] = str(data["age"])
    print("New age is", data["age"])
else:
    old_file = open("./ages.json", "w+")
    data = {"name": "Eric", "age":"42"}
    print ("No file found. Creating file with default data. Age set to", data["age"])
    
old_file.seek(0)
old_file.write(json.dumps(data))
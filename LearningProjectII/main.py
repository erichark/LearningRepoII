'''
Created on Jan 16, 2019

@author: root
'''
import simplejson as json
import os

if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size != 0:
    old_file = open("./ages.json", "r+")
    data = json.loads(old_file.read())
    print("Current age is", data["age"]+". Adding a year.")
    data["age"] += 1
    print("New age is", data["age"])
else:
    old_file = open("./ages.json", "r+")
    data = {"name":"Eric", "age": 43}
    print("No file found, setting default data in ages.json")
        
old_file.seek(0)      
old_file.write(json.dumps[data])
                   

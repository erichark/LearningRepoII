'''
Created on Feb 9, 2018

@author: Eric
'''

import requests
import os

params = {"q":"pizza"}
r = requests.get("https://www.bing.com/search", params = params)

print("Status:", r.status_code)
print(r.url)
print(r.text)


f = open("./index.html", "w+")
f.seek(0)
f.write(r.text)

print("Data dumped to file")
    
    
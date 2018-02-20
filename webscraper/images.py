'''
Created on Feb 16, 2018

@author: Eric
'''

from io import BytesIO
from bs4 import BeautifulSoup
from PIL import Image
import requests
import os


#search_term = input("Input Image Search Term:")
search_term = input("Input search term:")
params = {"q" : search_term}
dir_name = search_term.replace(" ", "_").lower()

if not os.path.isdir(dir_name):
    os.makedirs(dir_name)
    
r = requests.get("https://www.bing.com/images/search", params = params)
print(r)
soup = BeautifulSoup(r.text, "html.parser")
links = soup.findAll("a", {"class":"thumb"})
print(links)

for item in links:
    try:
        img_obj = requests.get(item.attrs["href"])
        print("Getting:", item.attrs["href"])
        title = item.attrs["href"].split("/")[-1]
        try:
            img = Image.open(BytesIO(img_obj.content))
            img.save("./" + dir_name + "/" + title, img.format)
        except:
            print("Could not save image.")
    except:
        print("could not request image")
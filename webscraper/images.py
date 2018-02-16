'''
Created on Feb 16, 2018

@author: Eric
'''

from io import BytesIO
from bs4 import BeautifulSoup
from PIL import Image
import requests


#search_term = input("Input Image Search Term:")
search_term = "pizza"
params = {"q" : search_term}
r = requests.get("https://www.bing.com/images/search", params = params)
print(r)

soup = BeautifulSoup(r.text, "html.parser")
links = soup.findAll("a", {"class":"thumbs"})
print(links)

for item in links:
    img_obj = requests.get(item.attrs["href"])
    print("Getting:", item.attrs["href"])
    title = item.attrs.split("/")[-1]
    img = Image.open(BytesIO(img_obj.content))
    img.save("./scraped_images" + title, img.format)
    
    
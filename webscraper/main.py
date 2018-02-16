'''
Created on Feb 16, 2018

@author: Eric
'''

from bs4 import BeautifulSoup
import requests


search_term = "pizza"
param = {"q" : search_term}
r = requests.get("http://www.bing.com", params = param)

soup = BeautifulSoup(r.text, "html.parser")
results = soup.find("ol", {"id":"b_results"})
links = results.findAll("li", {"class": "b_algo"})

for item in links:
    item_text = item.find("a").text
    item_link = item.find("a").attrs["href"]
    
    if item_text and item_link:
        print(item_text)
        print(item_link)
        print("Summary:", item.find("a").parent.parent.find("p").text)
        
        children = item.find("h2")
        print("Next Sibling of the h2 is:" , children.next_sibling)
        
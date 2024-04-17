import requests


BaseURL = 'https://fakestoreapi.com'
params = {"limit" : 3}
response = requests.get(f"{BaseURL}/products/", params = params)
print(response.json())
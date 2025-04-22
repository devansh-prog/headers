'''import requests

url="https://jsonplaceholder.typicode.com/posts"
headers={
    "Accept":"application/json",
    "User-agent":"my-app/1.0"
}
response =requests.get(url,headers=headers)
print(response.status_code)
print(response.json())'''
#query parameter
'''
import requests
url="https://jsonplaceholder.typicode.com/users/?key="sfesfefesfese"

params = {
    'id': 1,
    'limit': 10,
    'sort': 'desc'
}
response = requests.get(url, params=params)
print("Requested URL:", response.url)
print("Response:", response.json())'''
#body 
import requests

url = "https://jsonplaceholder.typicode.com/users"
data = {
    'id':11,
    "name": "Dev",
    "email": "dev@example.com"
}

response = requests.post(url, json=data)
print(response.json())

import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "name": "Anuj",
    "role": "Data Science"
}

response = requests.post(url, json=data)

print(response.json())
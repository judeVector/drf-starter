import requests

# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

response = requests.post(endpoint, json={"title": "Hello World"})
# print(response.status_code)
# print(response.text)
print(response.json())

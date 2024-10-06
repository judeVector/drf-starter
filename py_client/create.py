import requests

endpoint = "http://localhost:8000/api/products/"

response = requests.post(
    endpoint,
    data={"title": "New Product", "content": "This is a new content", "price": 32.99},
)
print(response.json())

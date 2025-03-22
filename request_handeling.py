### System

### Request  -->  API   --> Request Cycle


### Get Request
import requests
response = requests.get('https://jsonplaceholder.typicode.com/posts')
print(response)
print(response.status_code)
print(response.json())


### Post Request
data = {
    "userId": 100,
    "title": "Test Post",
    "body": "This is a test post."
}
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)
print(response)
print(response.status_code)
print(response.json())

### Update request
data = {
    "userId": 100,
    "id": 1,
    "title": "Updated Test Post",
    "body": "This is an updated test post."
}
response = requests.put('https://jsonplaceholder.typicode.com/posts/1', json=data)
print(response)
print(response.status_code)
print(response.json())

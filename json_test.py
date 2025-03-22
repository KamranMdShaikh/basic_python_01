import json

data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "is_logged_in": True,   
}


#### sirialization : Pythn --- > Json

json_string = json.dumps(data, indent=4)
print(json_string)
print(type(json_string))

print("--------------------------")


#### Deserialization : Json --- > Python

data_dict = json.loads(json_string)
print(data_dict)
print(type(data_dict))

print("--------------------------")

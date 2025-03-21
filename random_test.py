import random 
# help(random)
# print(dir(random))
# print(random.__doc__)

fruits =  ['apple', 'orange', 'cherry', 'banana']
print(random.choice(fruits))
random.shuffle(fruits)
print(fruits)

def pin_generation():
    return random.randint(1000,9999)

print(f"4 digit pin is: {pin_generation()}")
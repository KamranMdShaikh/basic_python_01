import collections
# print(collections.__doc__)

fruits =  ['apple', 'orange', 'cherry', 'banana', 'orange', 'orange', 'orange', 'orange', 'apple']
print(collections.Counter(fruits))
print(collections.Counter(fruits).most_common(3))

# random.shuffle(fruits)
# print(fruits)

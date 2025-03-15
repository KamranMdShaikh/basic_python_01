a = {'ranim': 12, 'karim': 14, 'fahim': 78, 1:[1,23,4,5,6,7,8], 2:[2,334,534,44]}

print("data type" ,type(a))


print("--------------------------")

for i in a:
    print(i)
    
print("--------------------------")

for i in a.values():
    print(i)
    
print("--------------------------")
for i in a:
    print("Key : ", i, "Value : ", a[i])

square_f = lambda x: x**2
print(square_f(5))

print("--------------------------")

numbers= [1,2,3,4,5,6,7,8]
squared_numbers = list(map(square_f, numbers))
print(squared_numbers)

print("--------------------------")

is_even = lambda x: x%2 == 0
even_numbers_m = list(map(is_even, numbers))
even_numbers_f = list(filter(is_even, numbers))
print(even_numbers_m)
print(even_numbers_f)
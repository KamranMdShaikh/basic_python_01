def sum_num(a,b):
    z = a+b
    return z

def subtract_num(a,b):
    z = a-b
    return z
print(sum_num(4,5))
print(subtract_num(4,5))


print("--------------------------")



def list_of_arge (*args):
    print(args)
    return sum(args)

print(list_of_arge(1,2,3,4,5))

    

print("--------------------------")

def my_prof(f_name, l_name, age):
    print(f"My name is {f_name} {l_name} and my age is {age}.")

my_prof("John", "Doe", 30)
my_prof("John", 30 ,"Doe")
my_prof(f_name ="Shaikh", age =30,l_name ="Kamran")


print("--------------------------")

def my_prof_kwargs(**kwargs):
    print(f"My name is {kwargs['f_name_k']} {kwargs['l_name_k']} and my age is {kwargs['age_k']}.")

my_prof_kwargs(f_name_k ="Shaikh", age_k =30,l_name_k ="Kamran")

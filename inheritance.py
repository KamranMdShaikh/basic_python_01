class GrandFather:
    def __init__(self, color, first_name):
        self.color = color
        self.first_name = first_name
    
    def gf_method_set(self):
        print(f"Grandfather {self.first_name} is of color {self.color}")
        print("Grandfather's method")


class Father(GrandFather):
    def __init__(self, color, first_name, hobbies):
        super().__init__(color, first_name)  # Initialize GrandFather properly
        self.hobbies = hobbies  # Assign hobbies
    
    def fa_method_get(self):
        print(f"Father's hobbies are {self.hobbies}")
        print("Father's method")


class Child(Father):
    def __init__(self, age, color, first_name, hobbies):
        super().__init__(color, first_name, hobbies)  # Initialize Father (which also initializes GrandFather)
        self.age = age  # Assign child's age


# Create an instance of Child
c1 = Child("21", "Red", "John", "Cricket")

# Call methods and print attributes
c1.gf_method_set()  # Grandfather's method
c1.fa_method_get()  # Father's method
print(f"Child's age is {c1.age}")
print(f"Child's color is {c1.color}")





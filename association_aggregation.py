###### Association

class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

class Student:
    def __init__(self, name, laptop_obj):
        self.name = name
        self.laptop_v = laptop_obj
    
    def display_laptop(self):
        print(f"{self.name}'s laptop: {self.laptop_v.brand}, {self.laptop_v.model}, ${self.laptop_v.price}")
        
    
lp1 = Laptop("Asus", "ABCD", "2000")
st1 = Student("John Doe", lp1)
st1.display_laptop()
    
    

###### Aggregation

class Department:
    def __init__(self, name):
        self.name = name
    
    class University:
        def __init__(self, name):
            self.name = name
            self.departments = []
        
        def add_department(self, department):
            self.departments.append(department)
        
        def show_department(self):
            print(f"{self.name} university:")
            for dept in self.departments:
                print(f"- {dept.name}")


uni = Department.University("XYZ University")
dept1 = Department("Computer Science")
dept2 = Department("EEE")
uni.add_department(dept1)
uni.add_department(dept2)
uni.show_department()

            
            
            
#### Car Class
### Brand, model

###  __init__():  Dunder menthothe (Double Underscore, Cosntructor methode- they create object )  
###  3 types of condtructor  (No returen constructor) ( Default, Paramenerized, Default )

class Car: 
    def __init__(self):  #self indicates object of car class
        self.brand =""
        self.model = ""
        
        
car1= Car()       
print(car1.brand)
print(car1.model)

car1.brand= "Lamborghini"
car1.model = "Aventador"

print(car1.brand)
print(car1.model)



car2= Car()     
car2.brand= "BMW"
car2.model = "X7"

print(car2.brand)
print(car2.model)
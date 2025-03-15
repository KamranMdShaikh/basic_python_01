#### Car Class
### Brand, model

###  __init__():  Dunder menthothe (Double Underscore, Cosntructor methode- they create object )  
###  3 types of condtructor  (No returen constructor) ( Default, Paramenerized, Default )

class Car: 
    # def __init__(self):  #self indicates object of car class
    #     self.brand =""
    #     self.model = ""
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
        
car1= Car("Lamborghini", "Aviator")       
print(car1.brand)
print(car1.model)
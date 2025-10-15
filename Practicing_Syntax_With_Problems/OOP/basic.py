# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class. 

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


myCar = Car("honda", "civic")
print(myCar.brand)
print(myCar.model)
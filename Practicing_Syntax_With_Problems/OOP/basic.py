# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class. 

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

# Problem: Add a method to the Car class that displays the full name of the car (brand and model). 
    def GetFullName(self):
        return f"brand: {self.brand} and model: {self.model}"


# Problem: Create an ElectricCar class that inherits from the Car class 
# and has an additional attribute battery_size. 
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


myCar = Car("honda", "civic")
print(myCar.brand)
print(myCar.model)

print(myCar.GetFullName())

electicCar = ElectricCar("tesla", "model s", "100Kwh")
print(electicCar.GetFullName())

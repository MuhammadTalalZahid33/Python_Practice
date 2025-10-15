# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class. 

class Car:
# Problem: Add a class variable to Car that keeps track of the number of cars created. 
    total_car = 0
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1

# Problem: Add a method to the Car class that displays the full name of the car (brand and model). 
    def GetFullName(self):
        return f"brand: {self.__brand} and model: {self.model}"

# Problem: Modify the Car class to encapsulate the brand attribute, making it private,
# and provide a getter method for it. 
    def get_brand(self):
        return self.__brand

# Problem: Create an ElectricCar class that inherits from the Car class 
# and has an additional attribute battery_size. 
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


myCar = Car("honda", "civic")
# print(myCar.brand)
print(myCar.model)
print(myCar.GetFullName())

electicCar = ElectricCar("tesla", "model s", "100Kwh")
print(electicCar.GetFullName())

print(myCar.get_brand())
print(electicCar.get_brand())

print(Car.total_car)
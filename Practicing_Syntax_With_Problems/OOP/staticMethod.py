class Circle:
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.pi * self.radius ** 2

    @staticmethod
    def describe():
        print("hello i am a static method fo Circle class...")


# Another example of the static method
# Circle.describe()


# class MathUtils:
#     @staticmethod
#     def add(a, b):
#         return a + b

# # You can call it using the class name
# result = MathUtils.add(5, 3)
# print(result)   # Output: 8

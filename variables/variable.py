"""
Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it.
"""

x = 7
y = "talal"

x = 3

print("x:", x)
print("y:", y)

# Casting
# If you want to specify the data type of a variable, this can be done with casting.

x = str(3)    # x will be '3'
y = int(3)    # y will be 3


# Get the Type
# You can get the data type of a variable with the type() function
x = 5
y = "John"
print(type(x))
print(type(y)) 


# Single or Double Quotes?
x = "John"
# is the same as
x = 'John'


# Variable names are case-sensitive.
a = 4
A = "Sally"
#A will not overwrite a 



# Declaring multiple variables together...
x , y , z = 2 , "talal" , 5.4

print(x, y, z)
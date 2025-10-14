# Problem: Recommend a type of pet food based on the pet's species and age. 
# (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food). 

specie = input("enter your pet specie: ")
age = int(input("enter your pet age: "))

if specie == "dog":
    if age < 2:
        print("puppy food")
    else:
        print("adult dog food")
else:
    if age > 5:
        print("senior cat food")
    else:
        print("junior cat food")
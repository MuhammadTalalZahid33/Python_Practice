age = int(input("enter the age: "))

if(age < 13):      # age < 13
    print("Child")
elif(age < 20):    # age -> 13-19
    print("Teenager")
elif(age < 60):    # age -> 20-59
    print("Adult")
else:              # age >= 60
    print("Senior")
    
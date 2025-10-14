# Problem: Keep asking the user for input until they enter a number between 1 and 10. 

while(True):
    n = int(input("enter input: "))
    if(n > 1 and n < 10):
        print("thanks...")
        break
    else:
        print("invalid number...")
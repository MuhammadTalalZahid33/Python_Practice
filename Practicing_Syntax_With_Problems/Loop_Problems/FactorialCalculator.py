# Problem: Compute the factorial of a number using a while loop. 

num = int(input("enter number to find factorial: "))
fact = num

while(num > 1):
    fact *= (num - 1)
    num -= 1

print(fact)
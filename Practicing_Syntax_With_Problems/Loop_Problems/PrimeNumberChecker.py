# Problem: Check if a number is prime. 

number = 4
rn = int(number/2 + 1)

is_prime = True   

if number > 1:
    for i in range(2, rn):
        if (number % i) == 0:
            is_prime = False
            break

print(is_prime)
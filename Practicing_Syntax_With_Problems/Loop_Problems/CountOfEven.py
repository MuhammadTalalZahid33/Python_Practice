# Problem: Calculate the count of even numbers up to a given number n. 

n = 10
sum = 0

for i in range(1, n+1):
    if i % 2 == 0:
        sum += 1

print("total no. of even digits upto n:", sum)

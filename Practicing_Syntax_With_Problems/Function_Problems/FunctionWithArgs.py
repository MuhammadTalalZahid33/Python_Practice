# Problem: Write a function that takes variable number of arguments and returns their sum. 

def SumAll(*args):
    # print(*args)
    # print(args)
    # for i in args:
    #     print(i)
    return sum(args)

print(SumAll(1, 3, 4, 6))
print(SumAll(1, 3, 4, 6, 43, 24))
print(SumAll(1, 3, 4, 6, 54, 56, 5, 6))

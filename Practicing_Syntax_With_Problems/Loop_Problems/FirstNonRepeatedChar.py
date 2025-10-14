# Problem: Given a string, find the first non-repeated character.

str = "teeteraffa"


#  Method 1
for i in str:
    count = str.count(i)
    if count == 1:
        print("first non-repeated char is:", i)
        break

#  Method 2
# for i, v in enumerate(str):
#     count = 1
#     chari = v
#     for j, w in enumerate(str):
#         if (i != j and v == w):
#             count += 1

#     if(count == 1):
#         print(chari, count)
    
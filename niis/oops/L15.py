
limit = int(input("Enter range: "))

for num in range(1, limit + 1):
    if num == sum(int(d)**len(str(num)) for d in str(num)):
        print(num, "is Armstrong number")


import math

def is_strong(n):
    return n == sum(math.factorial(int(d)) for d in str(n))

num = int(input("Enter number: "))
if is_strong(num):
    print(num, "is Strong number")
else:
    print(num, "is not Strong number")
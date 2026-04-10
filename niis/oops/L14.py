import math

a, b = 6, 24
print("GCD =", math.gcd(a, b))
print("LCM =", a*b // math.gcd(a, b))


def is_armstrong(n):
    p = len(str(n))
    return n == sum(int(digit) ** p for digit in str(n))

# Main
num = int(input("Enter number: "))
if is_armstrong(num):
    print(num, "is Armstrong number")
else:
    print(num, "is not Armstrong number")
n = int(input("Enter number of terms: "))

a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

    a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# GCD
for i in range(min(a, b), 0, -1):
    if a % i == 0 and b % i == 0:
        gcd = i
        break

# LCM
lcm = (a * b) // gcd

print("GCD =", gcd)
print("LCM =", lcm)
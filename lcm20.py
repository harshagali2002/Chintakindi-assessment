import math

def calculate_lcm(a, b):
    lcm = abs(a * b) // math.gcd(a, b)
    return lcm

a = int(input("Enter the first positive number: "))
b = int(input("Enter the second positive number: "))


lcm = calculate_lcm(a, b)

print(f"The LCM of {a} and {b} is: {lcm}")
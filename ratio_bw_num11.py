def calculate_ratio(num1, num2):
    if num2 == 0:
        raise ValueError("The denominator cannot be zero.")
    ratio = num1 / num2
    return ratio

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

try:
    ratio = calculate_ratio(num1, num2)
    print(f"The ratio of {num1} to {num2} is {ratio:.2f}.")
except ValueError as e:
    print(e)
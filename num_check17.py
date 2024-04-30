def check_number(number):
    # Check if the number is positive, negative, or zero
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"

# Prompt the user to enter a number
number = float(input("Enter a number: "))

# Determine whether the number is positive, negative, or zero
result = check_number(number)

# Print the result
print(f"The number {number} is {result}.")
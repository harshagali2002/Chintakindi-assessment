def sort_numbers(numbers):
    sorted_numbers = sorted(numbers)
    return sorted_numbers


print("Enter 5 numbers:")
numbers = []
for i in range(5):
    number = float(input(f"Enter number {i + 1}: "))
    numbers.append(number)

sorted_numbers = sort_numbers(numbers)


print("The 5 numbers in ascending order are:")
print(sorted_numbers)
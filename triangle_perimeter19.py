def calculate_triangle_perimeter(side1, side2, side3):
    # Calculate the perimeter by adding up the lengths of the three sides
    perimeter = side1 + side2 + side3
    return perimeter

# Prompt the user to enter the lengths of the three sides of the triangle
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Calculate the perimeter of the triangle
perimeter = calculate_triangle_perimeter(side1, side2, side3)

# Print the calculated perimeter
print(f"The perimeter of the triangle is: {perimeter}")
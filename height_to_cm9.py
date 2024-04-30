def convert_height_to_centimeters(height, unit):
    if unit == "inches":
        height_in_cm = height * 2.54
    elif unit == "feet":
        height_in_cm = height * 30.48
    elif unit == "meters":
        height_in_cm = height * 100
    else:
        raise ValueError("Invalid unit. Please use 'inches', 'feet', or 'meters'.")
    
    return height_in_cm

height = float(input("Enter your height: "))
unit = input("Enter the unit of your height (inches, feet, or meters): ")


height_in_cm = convert_height_to_centimeters(height, unit)

print(f"Your height in centimeters is: {height_in_cm:.2f} cm")
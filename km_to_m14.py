def convert_kilometers_to_meters(kilometers):
    meters = kilometers * 1000
    return meters


kilometers = float(input("Enter the distance in kilometers: "))

meters = convert_kilometers_to_meters(kilometers)

print(f"The distance in meters is: {meters:.2f} m")
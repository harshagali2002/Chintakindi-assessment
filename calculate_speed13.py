def calculate_speed(distance, time):
    if time == 0:
        raise ValueError("Time cannot be zero. Please provide a non-zero time value.")
    speed = distance / time
    return speed

distance = float(input("Enter the distance traveled (e.g., in kilometers): "))
time = float(input("Enter the time taken (e.g., in hours): "))


try:
    speed = calculate_speed(distance, time)
    print(f"The speed of the vehicle is {speed:.2f} KMPH.")
except ValueError as e:
    print(e)
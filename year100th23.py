from datetime import datetime

def calculate_year_turn_100(name, age):
    current_year = datetime.now().year
    year_turn_100 = current_year + (100 - age)
    print(f"Hello, {name}! You will turn 100 years old in the year {year_turn_100}.")


name = input("Please enter your name: ")
age = int(input(f"Hello, {name}! Please enter your age: "))

calculate_year_turn_100(name, age)
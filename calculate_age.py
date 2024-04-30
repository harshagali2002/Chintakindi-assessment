from datetime import datetime

def calculate_age(birth_date):
    current_date = datetime.today()
    age = current_date.year - birth_date.year
    
    if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
        age -= 1
    
    return age

year = int(input("Enter your birth year (YYYY): "))
month = int(input("Enter your birth month (MM): "))
day = int(input("Enter your birth day (DD): "))

birth_date = datetime(year, month, day)
           
age = calculate_age(birth_date)

print(f"You are {age} years old.")
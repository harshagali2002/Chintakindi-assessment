def is_senior_citizen(age):
    if age > 60 and age < 80:
        return True
    else:
        return False


age = int(input("Enter the age of the person: "))  

if is_senior_citizen(age):
    print(f"A person who is {age} years old is a senior citizen.")
else:
    print(f"A person who is {age} years old is not a senior citizen.")
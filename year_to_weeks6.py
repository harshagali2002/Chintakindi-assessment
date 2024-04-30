def convert_year_to_weeks(years):
    days_in_a_year = 365  # Using 365 days per year
    days_in_a_week = 7  # There are 7 days in a week
    
    total_days = years * days_in_a_year

    weeks = total_days / days_in_a_week
    return weeks

years = float(input("Enter the number of years: "))


weeks = convert_year_to_weeks(years)

print(f"The number of weeks in {years} years is approximately {weeks:.2f}.")
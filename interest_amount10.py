def calculate_interest_amount(principal, rate, time):
    rate_decimal = rate / 100
    interest = principal * rate_decimal * time
    return interest


principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in percentage): "))
time = float(input("Enter the time period (in years): "))


interest = calculate_interest_amount(principal, rate, time)


print(f"The interest amount for a principal of {principal:.2f}, rate of interest of {rate:.2f}%, and time period of {time:.2f} years is {interest:.2f}.")
def is_prime(number):
    # Check if the number is less than 2, if so, it is not prime
    if number < 2:
        return False
    # Check if the number is divisible by any number from 2 to the square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def find_first_five_primes():
    primes = []
    number = 2  # Start checking for prime numbers from 2
    
    while len(primes) < 5:
        # Check if the current number is prime
        if is_prime(number):
            primes.append(number)
        # Move to the next number
        number += 1
    
    return primes

# Find the first five prime numbers
first_five_primes = find_first_five_primes()

# Print the first five prime numbers
print("The first five prime numbers are:", first_five_primes)
def print_fibonacci_series(n):
    fib_1 = 0
    fib_2 = 1
    fibonacci_series = [fib_1, fib_2]
    
    for i in range(2, n):
        next_fib = fib_1 + fib_2
        fibonacci_series.append(next_fib)

        fib_1 = fib_2
        fib_2 = next_fib
    print(f"The first {n} Fibonacci numbers are: {fibonacci_series}")

# Print the first 10 Fibonacci numbers starting with 0 and 1
print_fibonacci_series(10)
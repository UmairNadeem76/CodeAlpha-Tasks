def fibonacci(n):
    # Initialize the first two terms of the Fibonacci series
    fib_sequence = [0, 1]
    
    # Generate the Fibonacci series up to the nth term
    for i in range(2, n):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
        
    return fib_sequence

# Input: number of terms
n = int(input("Enter The Number of Terms: "))

# Generate and print the Fibonacci series
fib_series = fibonacci(n)
print("Fibonacci Series Up To", n, "Terms:")
print(fib_series)
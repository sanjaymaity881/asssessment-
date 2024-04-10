# Function to generate Fibonacci series
def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# Display Fibonacci series of 10 numbers
fibonacci_series = fibonacci(5)
print("Fibonacci series of 5 numbers:")
print(fibonacci_series)

def fibonacci(n):
    # Base cases
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    # Create an array to store Fibonacci numbers up to n
    fib = [0] * (n + 1)
    
    # Initialize base cases
    fib[1] = 0
    fib[2] = 1
    
    # Fill the array in a bottom-up manner
    for i in range(3, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    
    return fib[n]

# Example usage
n = 10
print(f"Fibonacci number at position {n} is: {fibonacci(n)}")

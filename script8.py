def fibonacci(n):
    a, b = 0, 1
    series = []
    while len(series) < n:
        series.append(a)
        a, b = b, a + b
    return series

# Example usage
n = 10  # Number of Fibonacci numbers to generate
print(fibonacci(n))
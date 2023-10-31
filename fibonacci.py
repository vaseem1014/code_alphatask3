def fibonacci_recursive(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        result = n
    else:
        result = fibonacci_recursive(n - 1, memo) + fibonacci_recursive(n - 2, memo)
    memo[n] = result
    return result

# Input the number of Fibonacci numbers you want to generate
n = int(input("Enter the number of Fibonacci numbers to generate: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    fibonacci_series = [fibonacci_recursive(i) for i in range(n)]
    print("Fibonacci Series:")
    print(fibonacci_series)

def get_factorial(n):
    if n == 0:
        return 1
    else:
        return n * get_factorial(n-1)

print(get_factorial(5)) # expected output: 120
print(get_factorial(0)) # expected output: 1
print(get_factorial(-5)) # expected output: ValueError: n must be a non-negative integer

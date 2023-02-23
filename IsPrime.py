# Snippet 1
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(7)) # expected output: True
print(is_prime(12)) # expected output: False
print(is_prime(1)) # expected output: False

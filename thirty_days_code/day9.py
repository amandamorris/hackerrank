
def factorial(n):
    """Recursively calculate the factorial of n"""
    if n == 1:
        return 1
    return n * factorial(n-1)

num = int(raw_input())
print factorial(num)

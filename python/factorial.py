# This function should take a non-negative integer as an input and return the factorial of that number. The factorial of a non-negative integer n is the product of all positive integers less than or equal to n .


def factorial(n: int) -> int:
    # your code here
    result: int = 1
    if n == 0:
        return result

    while n > 0:
        result = result * n
        n = n - 1
    return result

def factorial_1(n, m=1):
    m *= n
    if n == 1 or n == 0:
        return m
    else:
        return factorial_1(n - 1, m)


def factorial(n):
    if n == 1 or n == 0:
        return n
    else:
        return n * factorial(n-1)


print(factorial_1(998))
print(factorial(998))

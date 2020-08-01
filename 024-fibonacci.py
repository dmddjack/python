def f(n):
    if n < 1:
        print('invalid input')
        return -1
    elif n == 1 or n == 2:
        return 1
    elif n > 2:
        return f(n - 1) + f(n - 2)


# f = lambda n: 1 if n == 1 or n == 2 else (f(n - 1) + f(n - 2) if n > 2 else -1)
fibonacci = []
for i in range(1, 10):
    fibonacci.append(f(i))
print(fibonacci)
print(f(20))

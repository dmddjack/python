def hanoi(n, x, y, z):
    if n == 1:
        print(x, '-->', z)
    else:
        hanoi(n - 1, x, z, y)
        hanoi(1, x, y, z)
        hanoi(n - 1, y, x, z)


N = int(input('請輸入輸入漢諾塔層數：'))
hanoi(N, 'X', 'Y', 'Z')

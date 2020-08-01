table = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
index = [6, 2, 4, 8, 5, 9, 3, 7, 1, 0]
constant0 = 177451812
constant1 = 100618342136696320


def av_bv(x):
    r = ''
    x = (int(x) ^ constant0) + constant1
    for i in range(10):
        r += table[x // 58 ** index[i] % 58]
    return 'BV' + r


def bv_av(x):
    r = 0
    for i in range(10):
        r += table.find(x[i]) * 58 ** index[i]
    return 'av' + str(r - constant1 ^ constant0)

def transform():
    while True:
        test = input('input av or BV: ')
        if (test.startswith('BV') or test.startswith('bv')) and len(test) == 12:
            print(bv_av(test[2:]))
            print()
        elif test.startswith('av') or test.startswith('AV'):
            print(av_bv(test[2:]))
            print()
        elif test.isalnum() and len(test) == 10:
            print(bv_av(test))
            print()
        elif test.isdigit():
            print(av_bv(test))
            print()
        else:
            print('invalid input')
            print()
transform()

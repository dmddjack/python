import random


def pi():
    attempt = p = 0
    while True:
        attempt += 1
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if (x ** 2 + y ** 2) <= 1:
            p += 1
        value = p / attempt * 4
        print('attempt # %d' % attempt, '    π ≈ %.10f' % value)


pi()

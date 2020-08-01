import random

table = list(range(1, 37))
random.shuffle(table)
for i in table:
    print(i)
    input()
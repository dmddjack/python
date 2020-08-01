from __future__ import print_function
import random
ans = random.randint(1,10)
print('dmddjack\'s number guess game')
guess = int(input('choose a integer between 1-10 : '))
chance = 5
while chance != 0:
    if not 1 <= guess <= 10:
        print('invalid value')
    else:
        if guess == ans:
            print('correct!')
            break
        else:
            if guess > ans:
                print('too big!')
            else:
                print('too small!')
        chance = chance-1
        print('Chance left: ' + str(chance))
    guess = int(input('choose again: '))
input("game over XD")

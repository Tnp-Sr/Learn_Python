'''
[Problem]
Dice guessing game (have 3 chances and hints)

'''

import random
#### main


print('----Dice guessing game----')
print('>> have 3 chances')
round = 1
result = False
## input
while True:
    if round > 3 or result:
        break
    user = int(input('Input answer(1-6) : '))
    if user < 1 or user > 6:
        print('WRONG Input')
    else:
        print('YOU : ',user)
        if round == 1:
            
            dice = random.randint(1,6) ## random answer
        result = (user == dice) ## compare
        if result :
            print('CORRECT !!')
        else :
            if user > dice:
                print('hint : less than')
            elif user < dice:
                print('hint : more than')
        round += 1

if not result:
    print('Try again next time...')
    print('dice : ',dice)
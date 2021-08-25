import random
a = random.randint(0, 180)
while True:
    num = int(input('please end a number from 0 to 100:'))
    print('\n')
    if num == a:
        print('bingo')
        break
    elif num > a:
        print('guess larger')
    else:
        print('guess smaller')

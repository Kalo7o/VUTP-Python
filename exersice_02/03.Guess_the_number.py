import random

secretNumber = random.randint(1, 10)

global inputNumber

while True:
    try:
        inputNumber = int(input('Guess the number: '))

        if secretNumber == inputNumber:
            print('Correct! :)')
            break
        if secretNumber > inputNumber:
            print('Too low.')
        if secretNumber < inputNumber:
            print('Too high.')
    except:
        print('Please enter a number')

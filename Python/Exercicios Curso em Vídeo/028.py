import random

number = random.randint(0, 5)

guest = int(input('type your guess number: '))

if guest == number:
    print('you win!!')
else:
    print('you lose!')

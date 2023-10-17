import random
dice_computer=random.randint(1,6)
dice_try=int(input('Enter number from 1 to 6:'))
print('You entered correct number: ', bool(dice_computer==dice_try))
#dla sprawdzenia:
print(dice_computer)

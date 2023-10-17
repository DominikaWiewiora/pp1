import random
dice=random.randint(1,6)
print('Dice rolled: ',dice)
print('Special number: ', bool(dice==1 or dice==6))

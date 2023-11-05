import mykeyboard
import mymath


user_number = mykeyboard.number()


computer_number = mymath.generate_number()

print(f'Computer number: {computer_number}')

if user_number == computer_number:
    print('You won the game!')
else:
    print('You lost the game!')


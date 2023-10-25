computer_science_choice=input('Are you interested in computer science? (Y/N): ')
if computer_science_choice=='Y':
    computer_science=True
else:
    computer_science=False
computer_games_choice=input('Do you like playing computer games? (Y/N): ')
if computer_games_choice=='Y':
    computer_games=True
else:
    computer_games=False
Instagram_chocie=input('Do you have an Instagram account? (Y/N): ')
if Instagram_chocie=='Y':
    Instagram=True
else:
    Instagram=False
if computer_science==True:
    print('Interested in computer science: Yes')
else:
    print('Interested in computer science: No')
if computer_games==True:
    print('Playing computer games: Yes')
else:
    print('Playing computer games: No')
if Instagram==True:
    print('Has an Instagram account: Yes')
else:
    print('Has an Instagram account: No')


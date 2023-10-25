number=(input('Enter EAN-13 article number: '))
if len(number)==13:
    print('Article number is correct')
else:
    print('Article number is incorrect')
if number[:3]==str('590'):
    print("Article manufactured in Poland")
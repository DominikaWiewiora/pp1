height=int(input('Enter your height in cm: '))
weight=int(input('Enter your weight in kg: '))
index=weight/(height/100)**2
print('Correct weight: ', bool(index>=18.5 and index<=24.9))
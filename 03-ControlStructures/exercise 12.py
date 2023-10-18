first_person=(input('Enter first person name:'))
first_age=int(input('Enter first person age:'))
second_person=(input('Enter second person name:'))
second_age=int(input('Enter second person age:'))
if first_age>=18 and second_age>=18:
    print(f'Both {first_person} and {second_person} are adults.')
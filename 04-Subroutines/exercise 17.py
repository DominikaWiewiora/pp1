def different(n1,n2,n3):
    return n1!=n2 and n2!=n3 and n3!=n1
n1=int(input('Enter first number: '))
n2=int(input('Enter second number: '))
n3=int(input('Enter third number: '))

if different(n1,n2,n3):
    print(f'Numbers {n1}, {n2} and {n3} are different')
else:
    print(f'Numbers {n1}, {n2} and {n3} are not all different')
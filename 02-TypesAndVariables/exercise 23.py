a=int(input('Enter a: \n'))
b=int(input('Enter b: \n'))
c=int(input('Enter c: \n'))
p=(a+b+c)/2
area=(p*(p-a)*(p-b)*(p-c))**0.5
circumference=a+b+c
print('Triangle area: ', area)
print('Triangle circumference: ', circumference)
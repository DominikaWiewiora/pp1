number1=input('Enter phone number:')
phone_number="{}-{}-{}"
a=(number1[:3])
b=(number1[3:6])
c=(number1[6:9])
print('Phone number:',phone_number.format(a,b,c))
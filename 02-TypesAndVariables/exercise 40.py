number=(input('Enter number:'))
card_number="{} {} {} {}"
a=number[:4]
b=number[4:8]
c=number[8:12]
d=number[12:16]
print('Card number:',card_number.format(a,b,c,d))
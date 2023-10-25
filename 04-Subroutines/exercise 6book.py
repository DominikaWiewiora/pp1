def computepay():
    hours=(int(input('Enter Hours:')))
    rate=int(input('Enter Rate: '))
    pay=hours*rate
    return pay
x=computepay()
print(f'Pay: {x}')
number=1
quantity=0
sum=0
mean=0
while number!=0:
    number=int(input('Enter number: '))
    if number ==0:
        break
    quantity+=1
    sum=sum+number
    mean=sum/quantity
print(f'Quantity={quantity},Sum={sum},Mean={mean}')


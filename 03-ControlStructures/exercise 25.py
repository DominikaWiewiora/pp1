number=int(input('Number of products purchased: '))
price=float(input('Product price: '))
if number<2:
    to_pay=number*price
else:
    to_pay=(2*price)+((price-(price*0.25))*(number-2))
to_pay1="{:.2f}".format(to_pay)
print(f"Amount to pay: {to_pay1}")

current=float(input('Current product price: '))
previous=float(input('Previous product price: '))
price_status=100-((current*100)/previous)
if price_status>0:
    print('Buy the product!!')
    print(f"Product price reduced by {price_status}%")
else:
    print("Don't buy the product!!")


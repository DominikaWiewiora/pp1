price=float(input('Enter price: '))
discount=int(input('Enter discount %: '))
pricediscount=price-((discount/100)*price)
pricediscount1=round(pricediscount, 2)
reduction=price-pricediscount1
reduction1=round(reduction, 2)
print('Price with discount: ',pricediscount1)
print('Reduction: ',reduction1)
a=int(input('a='))
b=int(input('b='))
print('* '*a)
for i in range(b-2):
    print('*'+ "  "*(a-2)+' *')
print('* '*a)

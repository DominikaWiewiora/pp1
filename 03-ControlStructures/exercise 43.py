a=0
b=1
print(a,end=" ")
for number in range(19):
    a, b=b, a+b
    print(a, end=' ')
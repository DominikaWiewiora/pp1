with open('intrange.txt', 'w') as file:
    for num in range(1,11):
        num2_pow=num**2
        num3_pow=num**3
        file.write(str(num)+', '+str(num2_pow)+', '+str(num3_pow)+'\n')
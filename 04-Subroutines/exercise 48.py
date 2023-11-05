def f(product_code):
    codeint=product_code[:-1]
    sum=0
    for i in codeint:
        sum+=int(i)
    first_three=str(sum%7)
    last=product_code[-1]
    if last==first_three:
        return True
    else:
        return False
print(f("7071"))
        


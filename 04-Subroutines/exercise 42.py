def f(number1,number2,number3):
    nmax=max(number1,number2,number3)
    nmin=min(number1,number2,number3)
    return abs(nmax-nmin)
print(f(2,12,8))
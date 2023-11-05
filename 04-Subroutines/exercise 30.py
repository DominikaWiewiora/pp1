def f(number,even):
    digit_sum=0
    while number > 0:
        digit = number % 10
        if even and digit % 2 == 0:
            digit_sum += digit
        elif not even and digit % 2 != 0:
            digit_sum += digit
        number //= 10
    return digit_sum
print(f(3124,True))
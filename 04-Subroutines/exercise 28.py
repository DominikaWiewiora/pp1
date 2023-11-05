def f(binary_number):
    try:
        int(binary_number, 2)
        return True
    except ValueError:
        return False
print(f('10101a1'))

for num in range(1, 31):
    if num % 3 == 0 and num % 5 == 0:
        print('BINGO')
    elif num % 3 == 0:
        print('THREE')
    elif num % 5 == 0:
        print('FIVE')
    else:
        print(num)

    
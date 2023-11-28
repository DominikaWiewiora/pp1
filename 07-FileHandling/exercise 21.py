with open('integers_numbers.txt', 'w') as file:
    for num in range(1, 51):
        file.write(str(num) + '\n')
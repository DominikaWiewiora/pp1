def occurs(number, array):
    if number in array:
        return f'Number {number} appears in the array'
    else:
        return f'Number {number} does not appear in the array'

input_number = int(input('Enter number: '))
given_array = [15, 38, 7, 23, 14]
result=occurs(input_number, given_array)
print(result)

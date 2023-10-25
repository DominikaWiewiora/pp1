decimal_number=int(input('Enter decimal number: '))
binary_result = ""
quotient = decimal_number
while quotient > 0:
    remainder = quotient % 2
    binary_result = str(remainder) + binary_result 
    quotient = quotient // 2 
print(f"{decimal_number}(10) = {binary_result}(2)")
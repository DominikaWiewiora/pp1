#idk bruh
def sum_repeated_digits(number):
    number_str = str(number)
    digit_count = {}
    total = 0

    for digit_char in number_str:
        if digit_char.isdigit():
            digit = int(digit_char)
            if digit in digit_count:
                digit_count[digit] += 1
            else:
                digit_count[digit] = 1

    for digit, count in digit_count.items():
        if count > 1:
            total += digit * count

    return total

# Test the function
print(sum_repeated_digits(1027))       # 0
print(sum_repeated_digits(230335))     # 9
print(sum_repeated_digits(513553007))  # 21

##def sum_repeated_digits(number):
    #return sum(int(digit) * (count - 1) for digit, count in collections.Counter(str(number)).items())##

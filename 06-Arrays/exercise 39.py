numbers = [12, 7, 23, 14, 6, 9, 16]

# Separate even and odd numbers
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

# Arrange even numbers first, followed by odd numbers
result = even_numbers + odd_numbers

# Display the separated even and odd numbers
print("Original Array:", numbers)
print("Separated Even and Odd Numbers:", result)
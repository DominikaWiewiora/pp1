# Sample array of real numbers
numbers = [3.5, 2.8, 4.1, 5.2, 6.0, 1.9, 4.6]

# Get the value from the user
value = float(input("Enter a value: "))

# Count the number of elements greater than the entered value
count = sum(1 for num in numbers if num > value)

# Display the count of elements greater than the entered value
print(f"Number of elements greater than {value}: {count}")
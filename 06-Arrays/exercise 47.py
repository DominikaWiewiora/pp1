arr = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]
]

# Initialize the sum of the last column
last_col = 0

# Calculate the sum of values in the last column
for row in arr:
    last_col += row[-1]  # -1 indexes the last element in each row

# Display the sum of values in the last column
print("Sum of values in the last column:",last_col)
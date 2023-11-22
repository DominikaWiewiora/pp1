array = [
    [-38, 19],
    [5, 40],
    [-7, 11],
    [29, 16]
]

min_value = min(min(row) for row in array)
max_value = max(max(row) for row in array)

min_row, min_col = 0, 0
max_row, max_col = 0, 0

for i in range(len(array)):
    for j in range(len(array[0])):
        if array[i][j] == min_value:
            min_row, min_col = i, j
        if array[i][j] == max_value:
            max_row, max_col = i, j

print(f"Smallest value: {min_value}, located at row {min_row}, column {min_col}")
print(f"Largest value: {max_value}, located at row {max_row}, column {max_col}")

arr = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# Modify the array to create a multiplication table
for i in range(5):
    for j in range(5):
        arr[i][j] = (i + 1) * (j + 1)
for row in arr:
    for value in row:
        print(value,end=" ")
    print()


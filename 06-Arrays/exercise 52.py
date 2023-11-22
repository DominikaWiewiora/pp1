
arr = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]


print("Before swapping:")
for rows in arr:
    print(rows,end="")
    print()

arr[0][0], arr[1][0], arr[2][0]= arr[0][4], arr[1][4], arr[2][4]

print("\nAfter swapping:")
for rows in arr:
    print(rows,end="")
    print()
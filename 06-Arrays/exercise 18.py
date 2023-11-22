arr = [
    [True, False],
    [True, True],
    [False, False]
]

for rows in arr:
    for i in range(len(rows)):
        if rows[i] == True:
            rows[i] = False
        else:
            rows[i] = True

print("Before:", arr)

for row in arr:
    print(row)



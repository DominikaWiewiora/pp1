arr = [2, 3, 2, 5, 8, 1, 9, 8]
unique_elements = []

for num in arr:
    if arr.count(num) == 1:
        unique_elements.append(num)
print(unique_elements)
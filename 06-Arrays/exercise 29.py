arr1 = [4, 36, 12, 28, 9, 44, 5]
arr2 = [5, 1, 36]

num = [num1 for num1 in arr1 if num1 not in arr2]

print(num)
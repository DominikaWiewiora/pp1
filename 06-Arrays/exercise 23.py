arr= [-15, 8, -31, 47, -2, 19]
max_num = arr[0]
min_num = arr[0]
for i in range(1, len(arr)): 
    if arr[i] > max_num:
        max_num = arr[i] 
    elif arr[i] < min_num:
        min_num = arr[i]

print("Maximum number:", max_num)
print("Minimum number:", min_num)
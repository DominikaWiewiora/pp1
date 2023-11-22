array1 = [1, 2, 3]
array2 = [1, 2, 3, 4, 5]

# Check if all elements of array1 are in array2
is_subset = True
for elem in array1:
    if elem not in array2:
        is_subset = False
        break

# Display the result
if is_subset:
    print("The first array is a subset of the second array.")
else:
    print("The first array is not a subset of the second array.")
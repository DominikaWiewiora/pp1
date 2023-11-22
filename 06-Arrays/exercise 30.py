def bubblesort(array):
    n = len(array)
    # Traverse through all elements in the array
    for i in range(n):
        # Last i elements are already in place, so no need to check them
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1 and swap if the element found is greater
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array

# Test the bubble sort function with three arrays
arr1 = [64, 25, 12, 22, 11]
arr2 = [38, 27, 43, 3, 9, 82, 10]
arr3 = [5, 2, 1, 8, 4, 7]

sorted_arr1 = bubblesort(arr1)
sorted_arr2 = bubblesort(arr2)
sorted_arr3 = bubblesort(arr3)

print("Sorted Array 1:", sorted_arr1)
print("Sorted Array 2:", sorted_arr2)
print("Sorted Array 3:", sorted_arr3)
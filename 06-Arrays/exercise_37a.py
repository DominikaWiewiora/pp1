def second_largest(arr):
    return sorted(set(arr))[-2] if len(set(arr)) > 1 else "Array should have at least two different numbers"

def difference_largest_smallest(arr):
    return max(arr) - min(arr)

def find_median(arr):
    sorted_arr = sorted(arr)
    length = len(arr)
    if length % 2 == 0:
        return (sorted_arr[length // 2 - 1] + sorted_arr[length // 2]) / 2
    else:
        return sorted_arr[length // 2]

def smallest_largest(arr):
    return [min(arr), max(arr)]

def array_as_string(arr):
    return '-'.join(map(str, arr))
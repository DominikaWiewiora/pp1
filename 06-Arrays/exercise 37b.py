import exercise_37a

numbers = [7, 3, 8, 5, 2]

print("Numbers:", ', '.join(map(str, numbers)))
print("Second largest number:", exercise_37a.second_largest(numbers))
print("Median:", exercise_37a.find_median(numbers))
print("Smallest and largest number:", ', '.join(map(str, exercise_37a.smallest_largest(numbers))))
print("Numbers as a string:", exercise_37a.array_as_string(numbers))
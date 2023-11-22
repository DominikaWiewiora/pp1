import random
def rand_elem(array):
    return random.choice(array)

# Given array
my_array = [10, 20, 30, 40, 50]

# Display a few randomly selected array elements
for _ in range(3):  # Change 3 to the number of elements you want to display
    random_element = rand_elem(my_array)
    print("Randomly selected element:", random_element)
def create_2d_arr(x, y):
    return [[0] * y for i in range(x)]

# Create a 2D array with dimensions 3 by 5 filled with zeros
two_dimensional_array = create_2d_arr(3, 5)
for row in two_dimensional_array:
    for value in row:
        print(value, end=" ")
    print()

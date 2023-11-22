def identity_matrix(n):
    # Create an identity matrix of size n x n
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def display_2d_array(arr):
    # Display a 2D array in rows and columns
    for row in arr:
        print(row,end="")
        print()

# Display identity matrices with dimensions 3, 5, and 8
for dim in [3, 5, 8]:
    print(f"\nIdentity matrix of dimension {dim}:")
    identity = identity_matrix(dim)
    display_2d_array(identity)
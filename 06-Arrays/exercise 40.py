numbers = [1, 23, 5, 382, 1, 17, 4, 906]

# Function to display the formatted array
def display_array(arr):
    print('-' * 41)
    for num in arr:
        print(f"|{num:4}", end='')
    print("|")
    print('-' * 41)

# Display the formatted array
display_array(numbers)

#For example, if num is 23, {num:4} will display it as ' 23', 
# where spaces are added before the number to make
#  it occupy 4 characters in total.
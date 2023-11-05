def f(dice):
    max_count = 0  # Initialize the maximum count
    current_count = 1  # Initialize the current count
    previous_digit = dice[0]  # Initialize the previous digit as the first digit

    for digit in dice[1:]:  # Start iterating from the second digit
        if digit == previous_digit:
            current_count += 1
        else:
            current_count = 1  # Reset the count if the current digit is different

        if current_count > max_count:
            max_count = current_count  # Update max_count if the current count is higher
        previous_digit = digit  # Update the previous_digit for the next iteration

    return max_count
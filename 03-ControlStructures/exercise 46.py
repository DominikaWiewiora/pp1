num = 1
for row in range(7):
    for col in range(7):
        print(f"{num:2d}", end=" ")
        num += 7
    num -= 48  # Reset the value of num to start a new row
    print()

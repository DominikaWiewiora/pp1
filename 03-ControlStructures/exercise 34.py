amount = int(input("Enter the amount in PLN: "))
coins_5_zl = 0
coins_2_zl = 0
coins_1_zl = 0
while amount > 0:
    if amount >= 5:
        coins_5_zl += 1
        amount -= 5
    elif amount >= 2:
        coins_2_zl += 1
        amount -= 2
    else:
        coins_1_zl += 1
        amount -= 1
print("The amount of PLN", amount, "in coins:")
print("5 zł –", coins_5_zl)
print("2 zł –", coins_2_zl)
print("1 zł –", coins_1_zl)
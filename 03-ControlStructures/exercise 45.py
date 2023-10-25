N = int(input("Enter the value of N: "))
count = 0
number = 2 
prime_numbers = []

while count < N:
    if all(number % i != 0 for i in range(2, int(number ** 0.5) + 1)):
        prime_numbers.append(number)
        count += 1
    number += 1

print("Prime numbers:", prime_numbers)
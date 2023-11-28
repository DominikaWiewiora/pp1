import random
with open('integers_random.txt', 'w') as file:
    for num in range(50):
        numbers=random.randint(100,1000)  
        file.write(str(numbers) + '\n')  
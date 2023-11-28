with open("exercise17text.txt", "r") as f:
    content = f.read()


with open('copy.txt', 'w') as file:
    file.write(content)
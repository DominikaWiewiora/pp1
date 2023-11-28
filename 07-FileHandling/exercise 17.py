with open("exercise17text.txt", "r") as file:
    lines = file.readlines()
    index = 0
    while index < len(lines):
        for line in lines[index:index+5]:
            print(line, end="")
        input("\n")
        index += 5

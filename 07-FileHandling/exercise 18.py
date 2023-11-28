with open("exercise17text.txt", "r") as f:
    file = open('copylines.txt','w')
    for lines in f:
        file.write(lines)

with open("countries.txt","r") as f:
    number_of_lines=0
    for line in f:
        number_of_lines+=1
    print('File name: countries.txt')
    print(f'Number of lines: {number_of_lines}')
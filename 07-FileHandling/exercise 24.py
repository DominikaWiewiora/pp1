import csv
with open('studentlist.txt', 'r') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        if int(row['age']) < 30:
            print(f"{row['first_name']}   {row['last_name']}   {row['email']}")

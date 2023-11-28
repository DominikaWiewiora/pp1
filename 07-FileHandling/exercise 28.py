import re

with open('sample3.txt', 'r') as file:
    text = file.read()
words = re.findall(r'\b\w{6,}\b', text)
for word in words:
    print(word)

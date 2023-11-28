import re

text = "To be, or not to be, that is the question"
words = re.findall(r'\b\w+\b', text)
num_words = len(words)

print(f"The text: '{text}'")
print(f"Number of words: {num_words}")

import re

text = "To be, or not to be, that is the question"

vowels = re.findall(r'[aeiouAEIOU]', text)

num_vowels = len(vowels)

print(f"The text: '{text}'")
print(f"Number of vowels: {num_vowels}")

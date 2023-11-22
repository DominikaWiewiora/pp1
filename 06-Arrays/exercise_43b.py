import exercise_43a

text = "An apple a day keeps the doctor away"

print("Text:", text)

# Number of words
num_words = exercise_43a.count_words(text)
print("Number of words:", num_words)

# Words from longest to shortest
longest_words = exercise_43a.longest_to_shortest(text)
print("Words from the longest:", ','.join(longest_words))

# Words ordered alphabetically
alphabetical_words = exercise_43a.alphabetical_order(text)
print("Words ordered alphabetically:", ','.join(alphabetical_words))
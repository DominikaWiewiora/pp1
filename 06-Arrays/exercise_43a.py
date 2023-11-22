def count_words(text):
    return len(text.split())

def longest_to_shortest(text):
    return sorted(text.split(), key=len, reverse=True)

def alphabetical_order(text):
    return sorted(text.split(), key=str.lower)
def f(palindrome):
    expression = palindrome.replace(" ", "").replace("-", "").lower()
    return expression == expression[::-1]

print(f("radar"))      # True
print(f("12-11-21"))   # True
print(f("book"))       # False
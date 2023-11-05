def f(password):
    if len(password)<6:
      return False
    char_password=set()
    for char in password:
        if char in char_password:
         return False
    return True

    
print(f("A2water3") )
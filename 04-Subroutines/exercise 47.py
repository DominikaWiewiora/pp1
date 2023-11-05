def f(text):
    result = ""
    for i in text:
        result += i + "-"
    if result:
        result = result[:-1] 
    return result
print(f("Univesity") )
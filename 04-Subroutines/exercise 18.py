def numbers(n):
    string='1'
    for i in range(1,n+1):
        string += f' {i}'
    return string
n=int(input('enter number: '))
print(f'Numbers <1,{n}>: {numbers(n)}')
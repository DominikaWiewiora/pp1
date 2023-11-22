arr=['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']
longest = arr[0]

for i in range(1, len(arr)):
    if len(arr[i]) > len(longest):
        longest = arr[i]
print(longest)
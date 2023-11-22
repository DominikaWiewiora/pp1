arr=[34,7,19,4,21,8]
sum_even=0
i=0
while i < len(arr):
    if arr[i]%2==0:
        sum_even+=1
    i+=1
print(sum_even)

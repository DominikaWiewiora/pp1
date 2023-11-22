arr=[[1,3,5],
     [8,7,2]]
#a
number1=arr[0][0]
number2=arr[1][2]
print(number1+number2)
#b
num1=arr[0][len(arr)//2]
num2=arr[len(arr)//2][1]
print(num1+num2)
#c
sum=0
for i in arr[1]:
    sum+=i
print(sum)
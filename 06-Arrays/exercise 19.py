#a	
arr1 = [3,7,1,0,4]
print(arr1)
#b
arr2 = [[2,3],[7,1],[0,4]]
print(arr2)
#c
arr3=[]
for i in range(5):
    arr3.append(7)
print(arr3)
#d
arr4=[]
for i in range(1,10):
    arr4.append(i)
print(arr4)
#e
arr5=[]
for i in range(1,10):
    arr5.append(i*2)
print(arr5)
#f
arr6=[]
import random
for i in range(10):
    arr6.append(random.randint(1,20))
print(arr6)
#g
arr7=[]
for i in range(5):
    arr7.append([])
print(arr7)
#h
arr8 = [[1 for i in range(2)] for j in range(4)]
print(arr8)
#i
arr9=[[random.randint(1,20) for i in range(3)] for j in range(5)]
print(arr9)
#j
arr10=[]
arr10.extend([4, 0, 3])
print(arr10)
#k
arr11=[]
for i in range(15):
    arr11.append(0)
print(arr11)
#l
arr12=[]
for i in range(1,31):
    arr12.append(int(i))
print(arr12)
#m
arr13=[]
for i in range(20):
    arr13.append(random.randint(0,1))
print(arr13)
#n
arr14 = []
for i in range(5):
    i = [False] * 2 
    arr14.append(i)
print(arr14)



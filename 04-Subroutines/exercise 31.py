def f(x,y):
   number=0
   for i in range(x,y+1):
      if i<0 and i%2==0:
        number+=1
   return number
print(f(-1,11))


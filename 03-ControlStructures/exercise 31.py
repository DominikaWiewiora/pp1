x=int(input('x = '))
y=int(input('y = '))
if x>0 and y>0:
    print(f'Point P({x},{y}) is in the first quadrant of the coordinate system')
if x<0 and y>0:
    print(f'Point P({x},{y}) is in the second quadrant of the coordinate system')
if x<0 and y<0:
    print(f'Point P({x},{y}) is in the third quadrant of the coordinate system')
if x>0 and y<0:
    print(f'Point P({x},{y}) is in the fourth quadrant of the coordinate system')
if y==0 and x!=0:
    print(f'Point P({x},{y}) is on horizontal axis')
if y!=0 and x==0:
    print(f'Point P({x},{y}) is on vertical axis')

circumference=int(input('Enter tree circumference: '))
pi=3.14
diameter=circumference/pi
print('Tree can be cut down: ', bool(diameter>=50))
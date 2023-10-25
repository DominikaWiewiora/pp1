attempts=0
for attempt in range(1,4):
    code=input('Enter the PIN code: ')
    if code=='0805':
        print('Correct')
        break
    else:
        print('Incorrect')
        attempts+=1
if attempts==3:
    print('Sorry, your payment card has been blocked.')
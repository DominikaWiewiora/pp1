personal_data='Mr. John May, born on 1998-02-16'
print('Description: ',personal_data)
print('Name:', personal_data[4:9])
print('Surname:',personal_data[9:12])
J=(personal_data[4:5])
M=(personal_data[9:10])
initials='{}{}'
print('Initials:',initials.format(J,M))
print('Born:',personal_data[22:32])
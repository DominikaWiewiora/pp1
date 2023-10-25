time1=(input('Enter time (24-hour format): '))
hours1=int(time1[:2])
if hours1<=12:
    print(f'Time in 12-hour format: {time1}am')
else:
    hours=hours1-12
    minutes=time1[3:]
    print(f'Time in 12-hour format: {hours}:{minutes}pm')

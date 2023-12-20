class Phone():
    def __init__(self,phone_number,battery_level,is_ringing):
        self.phone_number=phone_number
        self.battery_level=battery_level
        self.is_ringing=is_ringing
        self.is_on=True
    def answering(self):
        if self.is_ringing:
            print(f'Incoming call from {self.phone_number}')
            self.is_ringing=False
        else:
            print('No incoming calls')
    def charging(self):
        if self.battery_level<100:
            print(f'phone is on {self.battery_level} can be charged')
        else:
            print('full battery')
    def on_or_off(self):
        if self.is_on:
            print('Do you want to turn off?')
            answer=input('Enter "YES" or "NO"')
            if answer=="YES":
                print('turning off...')
                self.is_on=False
            else:
                self.is_on=True
        else:
            print('TURNING ON...')

phone=Phone(123456789,30,True)
print(f'phone number is {phone.phone_number}.battery level is {phone.battery_level}, the phone is ringing:{phone.is_ringing}')
phone.answering()
phone.charging()
phone.on_or_off()
        

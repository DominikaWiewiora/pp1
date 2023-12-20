class TV():
    def __init__(self,is_on,channel_no):
        self.is_on=is_on
        self.channel_no=channel_no
    def turn_on(self):
        if not self.is_on:
            self.is_on=True

    def turn_off(self):
        if self.is_on:
            self.is_on=False

    def show_status(self):
        if self.is_on:
            print(f'TV is on, channel {self.channel_no}')
        else:
            print('TV is off')
tv=TV(False,1)
tv.turn_on()
tv.show_status()


class TV():
    def __init__(self,is_on,channel_no,channels):
        self.is_on=is_on
        self.channel_no=channel_no
        self.channels=channels
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
    
    def set_channel(self,new_channel_no):
         self.channel_no=new_channel_no

    def set_channels(self,channels_list):
        self.channels=channels_list

    def show_channels(self):
        print(list(self.channels))
        print('available channels: TVP1,TVP2,POLSAT,TVN,FILMBOX,DOSCOVERY ')

tv=TV(False,1,[])
tv.show_status()
tv.turn_on()
tv.show_status()
tv.set_channel(5)
tv.show_channels()
tv.set_channels(['TVP1','TVP2','POLSAT','TVN','FILMBOX','DISCOVERY'])
tv.show_channels()
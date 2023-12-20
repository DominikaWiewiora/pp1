class TV():
    def __init__(self,is_on,channel_no,channels):
        self.is_on=is_on
        self.channel_no=channel_no
        self.channels=channels
        self.volume_level=0
    def turn_on(self):
        if not self.is_on:
            self.is_on=True

    def turn_off(self):
        if self.is_on:
            self.is_on=False

    def show_status(self):
        if self.is_on:
            print(f'TV is on, channel {self.channel_no}, volume:{self.volume_level}')
        else:
            print('TV is off')
    
    def set_channel(self,new_channel_no):
         self.channel_no=new_channel_no

    def set_channels(self,channels_list):
        self.channels=channels_list

    def show_channels(self):
        print(list(self.channels))
        print('available channels: TVP1,TVP2,POLSAT,TVN,FILMBOX,DOSCOVERY ')
    def volume_increas(self):
        if self.is_on and self.volume_level<10:
            self.volume_level+=1
    
    def volume_decreas(self):
        if self.is_on and self.volume_level>0:
            self.volume_level-=1
tv=TV(False,1,[])

tv.turn_on()
tv.show_status()
tv.volume_increas()
tv.show_status()
tv.volume_decreas()
tv.show_status()


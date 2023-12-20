class Music():
    def __init__(self,artist,track_title,album,year):
        self.artist=artist
        self.track_title=track_title
        self.album=album
        self.year=year
    def __str__(self):
        return (f'Performer: {self.artist}\n'
                    f'Song: {self.track_title}\n'
                    f'Album: {self.album}\n'
                    f'Year: {self.year}')
p1=Music("Ed Sheeran","Hearts Don't Break Around Here","Divide",2017 )
print(p1)
p2=Music("Arctic Monkeys","A Certain Romance","Whatever People Say I Am, That's What I'm Not",2006)
print(p2)
    
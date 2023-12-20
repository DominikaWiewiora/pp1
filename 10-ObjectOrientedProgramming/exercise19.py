import random

class Thermometer:
    def __init__(self):
        self.temperature = 0
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def measure_temperature(self):
        if self.is_on:
            self.temperature = random.randint(340, 420) / 10.0

    def display_temperature(self):
        print(f"Temperature: {self.temperature}C", end=' ')
        if self.temperature >= 37.0:
            print("(fever)", end=' ')
        if self.temperature >= 41.0:
            print("CRITICAL TEMPERATURE!!")
        else:
            print()

    def turn_off(self):
        self.is_on = False

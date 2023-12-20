class CellPhone:
    def __init__(self, brand, model, battery_percentage):
        self.brand = brand
        self.model = model
        self.battery_percentage = battery_percentage
        self.is_on = False
        self.current_app = None

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def charge_battery(self, amount):
        self.battery_percentage = min(100, self.battery_percentage + amount)

    def use_app(self, app_name):
        if self.is_on:
            self.current_app = app_name
            print(f"Using {app_name} on {self.brand} {self.model}")

    def __str__(self):
        return f"{self.brand} {self.model} - Battery: {self.battery_percentage}%"
phone1 = CellPhone("Samsung", "Galaxy S21", 70)
phone2 = CellPhone("Apple", "iPhone 13", 85)
print(phone1)
print(phone2)
phone1.turn_on()
phone1.use_app("Maps")
phone2.turn_on()
phone2.use_app("Music")
phone2.charge_battery(10)
print(phone1)
print(phone2)

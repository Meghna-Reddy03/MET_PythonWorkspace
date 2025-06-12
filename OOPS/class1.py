class AC:
    def __init__(self, brand):
        self.brand = brand
    def turn_on(self):
        print(f" {self.brand} Ac turned on")
    def turn_off(self):
        print("Ac turned off")
    def change_temp(self):
        pass

ac = AC("samsung")

class Light:
    def __init__(self,color):
        self.watts = 100
        self.color = color
        self.brand = 'phillips'
        self.shape = 'round'

    def turn_on(self):
        print(f'{self.color} Light turned on')

    def turn_off(self):
        print('light turned off')

    def adjust_intensity(self):
        pass

light = Light('white')

class Room:
    def __init__(self, ac, light):
        self.temp = 24
        self.ac = ac
        self.light = light



room = Room(ac, light)
room.ac.turn_on()
room.light.turn_on()
class AC:
    temp = 0
    brand = 'samsung'
    color = 'white'
    capacity = 4 #tons

    def turn_on(self):
        print('AC turned on')

    def turn_off(self):
        print('AC turned off')

    def chang_temp(self):
        pass

class Light:
    watts = 100
    color = 'yellow'
    brand = 'phillips'
    shape = 'round'

    def turn_on(self):
        print('Light turned on')

    def turn_off(self):
        print('light turned off')

    def adjust_intensity(self):
        pass

class Desk:
    height = 0 #meters
    color = 'black'
    is_wheeled = True

    def change_height(self):
        change = int(input('change the height to:'))
        if change < 0:
            height += change
            print(height)

class Shutter:
    color = 'printed pattern'
    length = 2 #meters
    width = 2 #meters
    can_roll = True

    def roll_shutter(self):
        print('shutter rolled on')

class Fan:
    color = 'white'
    blade = 3 
    brand = 'Havells India'
    watts = 50
    speed = 0
    can_rotate = True

    def change_speed(self):
        pass


ac = AC()
light = Light()
desk = Desk()
shutter = Shutter()
fan = Fan()
print(ac.color)
print(ac.turn_off())
print(light.color)
print(light.turn_on())
print(fan.blade)
print(fan.change_speed())
print(desk.change_height())
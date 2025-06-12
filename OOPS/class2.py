class Vehical:
    def __init__(self):
        pass
    def sound(self):
        print('makes sound')

class Car(Vehical):
    def __init__(self,name):
        self.name = name
    
    def sound(self):
        print(f"engine of the {self.name} doesn't start ")

class Bike(Vehical):
    def __init__(self,color):
        self.color = color

    def sound(self):
        print(f'he rides that {self.color} bike that makes a loud sound')

car = Car()


        
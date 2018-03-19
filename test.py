class Car():
    def __init__(self, name):
        self.name = name
    def fullname(self):
        print(self.name)

class Electcar(Car):
    def __init__(self, name):
        super().__init__(name)

    def fullname(self):
        print('sdfgdg')
mytesla = Electcar('tesla 3')

mytesla.fullname()



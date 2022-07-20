from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.members = [Dinosaur('T Rex U'), Dinosaur('Leoplaridon'), Dinosaur('Spiny')]
        self.is_alive = True

    def check_hp(self):
        if len(self.members) == 0:
            self.is_alive = False
            return
        for x in self.members:
            if x.health <= 0:
                self.members.remove(x)
                print(f'{x.name} was defeated')

    


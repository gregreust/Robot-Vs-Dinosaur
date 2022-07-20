from robot import Robot

class Fleet:
    def __init__(self):
        self.members = [Robot('Optimus Prime'), Robot('Lazerface'), Robot('Alien')]
        self.is_alive = True

    def check_hp(self):
        if len(self.members) == 0:
            self.is_alive = False
            return
        for x in self.members:
            if x.health <= 0:
                self.members.remove(x)
                print(f'{x.name} was defeated')
    



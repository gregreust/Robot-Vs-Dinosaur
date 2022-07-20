class Dinosaur:
    def __init__(self, name):
        self.name = name
        self.health = 80
        self.attack_power = 15

#could I make the attack power randomly different for each attack? 

    def attack(self, robot):
        robot.health -= self.attack_power
        print(f'{self.name} attacked {robot.name} for {self.attack_power} damage.')
        print(f'{robot.name} has {robot.health} HP left.')


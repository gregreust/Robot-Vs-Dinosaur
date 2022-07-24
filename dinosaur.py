from random import choice

class Dinosaur:
    def __init__(self, name):
        self.name = name
        self.health = 80
        self.attack_power = [5, 15, 20, 40]

#could I make the attack power randomly different for each attack? 

    def attack(self, robot):
        random_attack = choice(self.attack_power)
        robot.health -= random_attack
        print('')
        print(f'{self.name} attacked {robot.name} for {random_attack} damage.')
        print(f'{robot.name} has {robot.health} HP left.')


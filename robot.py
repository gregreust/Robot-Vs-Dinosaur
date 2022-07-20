from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapons = [Weapon('lazer gun', 10), Weapon('grenade', 40), Weapon('iron fist', 15)]
        self.active_weapon = self.weapons[0]

    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        print(f'{self.name} attacked {dinosaur.name} with {self.active_weapon.name}.')
        print(f'{dinosaur.name} has {dinosaur.health} HP left.')

    def switch_weapon(self):
        selection = 0
        while selection <= 0 or selection > 3:
            selection = int(input('Enter 1 for lazer gun, 2 for grenade, or 3 for iron fist: '))
            if selection == 1 or selection == 2 or selection == 3:
                self.active_weapon = self.weapons[int(selection) - 1] #user enters 123 but list is 012
                return
            else:
                print('Error')

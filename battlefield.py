from herd import Herd
from fleet import Fleet
from random import choice

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def intro(self):
        print('A fleet of robots: ')
        for x in self.fleet.members:
            print(x.name)
        print('Facing a herd of dinosaurs: ')
        for x in self.herd.members:
            print(x.name)

    def choose_target(self): #user chooses the robots target
        user_choice = 0
        while user_choice <= 0  or user_choice > 3: 
            user_choice = int(input(f'Enter 1 to attack {self.herd.members[0].name} \n 2 to attack {self.herd.members[1].name} \n 3 to attack {self.herd.members[2].name}'))        
            if user_choice == 1:
                return self.herd.members[0]
            elif user_choice == 2:
                return self.herd.members[1]
            elif user_choice == 3:
                return self.herd.members[2]
            else:
                print('Error')

    def random_target(self): #program determines dinosaurs target from fleet list
        return choice(self.fleet.members)

    def run_battle(self):
        print('The battle has begun!')
        while self.fleet.is_alive and self.herd.is_alive:
            for x in range(3):
                #robot at position x in fleet , select weapon and select target
                self.fleet.members[x].switch_weapon()
                target = self.choose_target()
                #robot x .attack (target)
                self.fleet.members[x].attack(target)
                #check herd hp 
                self.herd.check_hp()
                #if hp is 0, return "robots win" and break
                if self.herd.is_alive == False:
                    print('The herd of dinosaurs was defeated! Congratulations')
                    break
                #dinosaur one, random target
                target = self.random_target()
                #dinosaur one.attack(target) 
                self.herd.members[x].attack(target)
                #check target hp
                self.fleet.check_hp()
                #if hp is zero, return "dinosaurs win" and break
                if self.fleet.is_alive == False:
                    print('The robots were defeated by the herd of dinosaurs. Sad')
                    break


  
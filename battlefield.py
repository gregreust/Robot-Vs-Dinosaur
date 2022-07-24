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
        print('')
        print('Facing a herd of dinosaurs: ')
        for x in self.herd.members:
            print(x.name)
        print('')

    def choose_target(self): #user chooses the robots target
        user_choice = 0
        print('')
        while user_choice <= 0  or user_choice > 3: 

            for x in range(len(self.herd.members)):
                print(f'Enter {x+1} to attack {self.herd.members[x].name}')
            user_choice = int(input())
        
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

    def robots_turn(self, x):
        #robot at position x in fleet , select weapon and select target
        self.fleet.members[x].switch_weapon()
        target = self.choose_target()
        #robot x .attack (target)
        self.fleet.members[x].attack(target)
        #check herd hp 
        self.herd.check_hp()
        #if hp is 0, return "robots win" and break
        if self.herd.is_alive == False:
            print('')
            print('The herd of dinosaurs was defeated! Congratulations')
                    

    def dinosaurs_turn(self, x):
        #dinosaur one, random target
        target = self.random_target()
        #dinosaur one.attack(target) 
        self.herd.members[x].attack(target)
        #check target hp
        self.fleet.check_hp()
        #if hp is zero, return "dinosaurs win" and break
        if self.fleet.is_alive == False:
            print('')
            print('The robots were defeated by the herd of dinosaurs. Sad')
                

    def run_battle(self):
        print('The battle has begun!')
        
        fleet_count = 0          #counter to cycle though all members of fleet
        herd_count = 0      

        while self.fleet.is_alive and self.herd.is_alive:
            if len(self.fleet.members) == 2:     #trying to prevent counter being larger than the length of fleet list
                fleet_count = 1
            elif len(self.fleet.members) == 1:
                fleet_count = 0
            elif fleet_count > 2:
                fleet_count = 0
            self.robots_turn(fleet_count)

            if self.herd.is_alive == False:
                break

            if len(self.herd.members) == 2:
                herd_count = 1
            elif len(self.herd.members) == 1:
                herd_count = 0
            elif herd_count > 2:
                herd_count = 0
            self.dinosaurs_turn(herd_count)
            
            fleet_count += 1
            herd_count += 1
  
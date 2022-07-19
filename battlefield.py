from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self, fleet_of_robots, herd_of_dinosaurs):
        self.robots = fleet_of_robots
        self.dinosaurs = herd_of_dinosaurs

    def intro(self):
        print('A fleet of robots: ')
        for x in self.robots:
            print(x.name)
        print('Facing a herd of dinosaurs: ')
        for x in self.dinosaurs:
            print(x.name)


    def run_battle(self):
        print('The battle has begun!')
        self.robots.members[0]

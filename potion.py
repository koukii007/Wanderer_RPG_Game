import random
from IntermediaryForMapCreation import *

map = game_map()
floor_perimeter = map.perimeter
class potion:
    def __init__(self):
        map.coords_check()
        self.img = "potion"
        self.x = random.randint(0, 5)
        self.y = random.randint(0, 6)
        position_check = (self.x, self.y)
        while position_check in map.coords_check():
            self.x = random.randint(0, 5)
            self.y = random.randint(0, 6)
            position_check = (self.x, self.y)
    def receive_position(self,x = 0,y=0):
        self.x = x
        self.y = y

    def reset(self):

        self.x = random.randint(0,5)
        self.y = random.randint(0,6)
        tuple_check = (self.x, self.y)
        while tuple_check in map.coords_check():
            self.x = random.randint(0,5)
            self.y = random.randint(0,6)
            tuple_check = (self.x, self.y)


class blue_potion():
    def __init__(self):
        map.coords_check()
        self.img = "blue_potion"
        self.x = random.randint(4, 9)
        self.y = random.randint(4, 9)
        position_check = (self.x, self.y)
        while position_check in map.coords_check():
            self.x = random.randint(4, 9)
            self.y = random.randint(4, 9)
            position_check = (self.x, self.y)
    def receive_position(self,x = 0,y=0):
        self.x = x
        self.y = y
    def reset(self):

        self.x = random.randint(4, 9)
        self.y = random.randint(4, 9)
        tuple_check = (self.x, self.y)
        while tuple_check in map.coords_check():
            self.x = random.randint(4,9)
            self.y = random.randint(4,9)
            tuple_check = (self.x, self.y)
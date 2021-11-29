import random
from Hero import *
from IntermediaryForMapCreation import *

map_for_skeleton = game_map()
floor_perimeter = map_for_skeleton.perimeter


class skeleton_1(Hero):


    def __init__(self):
        map_for_skeleton.coords_check()
        self.HP = 2 * 1 * random.randint(1, 6)
        self.DP = 1 / 2 * random.randint(1, 6)
        self.SP = 1 * random.randint(1, 6)
        self.maxHP = self.HP
        self.img = "skeleton"
        self.key_holder = random.choice([0,1])
        self.x = random.randint(4, 9)
        self.y = random.randint(0, 4)
        position_check = (self.x, self.y)
        while position_check in map_for_skeleton.coords_check():
            self.x = random.randint(4, 9)
            self.y = random.randint(0, 4)
            position_check = (self.x, self.y)

    def move_skeleton1(self):
        map_for_skeleton.coords_check()
        wall_coords = map_for_skeleton.coords_check()

        top = (self.x, self.y-1)
        right = (self.x+1, self.y)
        left = (self.x-1, self.y)
        bottom = (self.x, self.y+1)
        possibility_array = [top,right,left,bottom ]
        move_to_list =[]
        for item in possibility_array:

            if item  not in map_for_skeleton.coords_check() and item not in floor_perimeter:
                move_to_list.append(item)
                continue

        move_to_these_coords = random.choice(move_to_list)
        self.x = move_to_these_coords[0]
        self.y = move_to_these_coords[1]

    def receive_strike(self, SP_value = 0):

        self.HP -= SP_value
        self.strike_back = self.SP + 2 * random.randint(1, 6)

        if self.HP <0:
            self.HP = 0
            self.img = "ghost"
    def Is_key_holder(self, x= 0):
        self.key_holder = x
    def level_up(self):
        self.img = "skeleton"
        self.HP = 2 * map_for_skeleton.map_number * random.randint(1, 6) + self.maxHP
        self.DP = map_for_skeleton.map_number / 2 * random.randint(1, 6)
        self.SP = map_for_skeleton.map_number * random.randint(1, 6)

    def reset(self):

        self.x = random.randint(4, 9)
        self.y = random.randint(0, 4)
        position_check = (self.x, self.y)
        while position_check in map_for_skeleton.coords_check():
            self.x = random.randint(4, 9)
            self.y = random.randint(0, 4)
            position_check = (self.x, self.y)


class skeleton_2(Hero):

    def __init__(self):
        map_for_skeleton.coords_check()
        self.HP = 2 * 1 * random.randint(1, 6)
        self.DP = 1 / 2 * random.randint(1, 6)
        self.SP = 1 * random.randint(1, 6)
        self.maxHP = self.HP
        self.img = "skeleton"
        self.x = random.randint(7, 9)
        self.y = random.randint(5, 9)
        self.key_holder = random.choice([0, 1])
        position_check = (self.x, self.y)
        while position_check in map_for_skeleton.coords_check():
            self.x = random.randint(7, 9)
            self.y = random.randint(5, 9)
            position_check = (self.x, self.y)

    def move_skeleton2(self):
        map_for_skeleton.coords_check()
        wall_coords = map_for_skeleton.coords_check()
        top = (self.x, self.y-1)
        right = (self.x+1, self.y)
        left = (self.x-1, self.y)
        bottom = (self.x, self.y+1)
        possibility_array = [top,right,left,bottom ]
        move_to_list =[]
        for item in possibility_array:

            if item  not in map_for_skeleton.coords_check() and item not in floor_perimeter:
                move_to_list.append(item)
                continue

        move_to_these_coords = random.choice(move_to_list)
        self.x = move_to_these_coords[0]
        self.y = move_to_these_coords[1]


    def receive_strike(self, SP_value=0):

        self.HP -= SP_value
        self.strike_back = self.SP + 2 * random.randint(1, 6)

        if self.HP < 0:
            self.HP = 0
            self.img = "ghost"
    def Is_key_holder(self, x= 0):
        self.key_holder = x
    def level_up(self):
        self.img = "skeleton"
        self.HP = 2 * map_for_skeleton.map_number * random.randint(1, 6) + self.maxHP
        self.DP = map_for_skeleton.map_number / 2 * random.randint(1, 6)
        self.SP = map_for_skeleton.map_number * random.randint(1, 6)
    def reset(self):

        self.x = random.randint(4, 9)
        self.y = random.randint(0, 4)
        position_check = (self.x, self.y)
        while position_check in map_for_skeleton.coords_check():
            self.x = random.randint(4, 9)
            self.y = random.randint(0, 4)
            position_check = (self.x, self.y)



class skeleton_3(Hero):

    def __init__(self):
        map_for_skeleton.coords_check()
        self.HP = 2 * 1 * random.randint(1, 6)
        self.DP = 1 / 2 * random.randint(1, 6)
        self.SP = 1 * random.randint(1, 6)
        self.maxHP = self.HP
        self.img = "skeleton"
        self.x = random.randint(4, 6)
        self.y = random.randint(5, 9)
        self.key_holder = random.choice([0, 1])
        position_check = (self.x, self.y)
        while position_check in map_for_skeleton.coords_check():
            self.x = random.randint(4, 6)
            self.y = random.randint(5, 9)
            position_check = (self.x, self.y)

    def move_skeleton3(self):
        map_for_skeleton.coords_check()
        wall_coords = map_for_skeleton.coords_check()

        top = (self.x, self.y - 1)
        right = (self.x + 1, self.y)
        left = (self.x - 1, self.y)
        bottom = (self.x, self.y + 1)
        possibility_array = [top, right, left, bottom]
        move_to_list = []
        for item in possibility_array:

            if item not in map_for_skeleton.coords_check() and item not in floor_perimeter:
                move_to_list.append(item)
                continue

        move_to_these_coords = random.choice(move_to_list)
        self.x = move_to_these_coords[0]
        self.y = move_to_these_coords[1]


    def receive_strike(self, SP_value=0):

        self.HP -= SP_value
        self.strike_back = self.SP + 2 * random.randint(1, 6)

        if self.HP < 0:
            self.HP = 0
            self.img = "ghost"
    def Is_key_holder(self, x= 0):
        self.key_holder = x
    def level_up(self):
        self.img = "skeleton"
        self.HP = 2 * map_for_skeleton.map_number * random.randint(1, 6) + self.maxHP
        self.DP = map_for_skeleton.map_number / 2 * random.randint(1, 6)
        self.SP = map_for_skeleton.map_number * random.randint(1, 6)
    def reset(self):

        self.x = random.randint(4, 9)
        self.y = random.randint(0, 4)
        position_check = (self.x, self.y)
        while position_check in map_for_skeleton.coords_check():
            self.x = random.randint(4, 9)
            self.y = random.randint(0, 4)
            position_check = (self.x, self.y)

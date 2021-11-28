import random
from IntermediaryForMapCreation import *

map_for_boss = game_map()
wall_coords = map_for_boss.coords_check()
floor_perimeter = map_for_boss.perimeter


class BOSS:

    def __init__(self):
        self.HP = 2 * 1 * random.randint(1, 6) + random.randint(1, 6)
        self.maxHP = self.HP
        self.DP = 1 / 2 * random.randint(1, 6) + int(random.randint(1, 6) / 2)
        self.SP = 1 * random.randint(1, 6) + 1

        self.x = random.randint(0,4)
        self.y = random.randint(5, 9)
        tuple_check = (self.x, self.y)
        while tuple_check in wall_coords:
            self.x = random.randint(0,4)
            self.y = random.randint(5, 9)
            tuple_check = (self.x, self.y)

    def move(self):

        top = (self.x, self.y - 1)
        right = (self.x + 1, self.y)
        left = (self.x - 1, self.y)
        bottom = (self.x, self.y + 1)
        possibility_array = [top, right, left, bottom]
        move_to_list = []
        for item in possibility_array:

            if item not in wall_coords and item not in floor_perimeter:
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
    def level_up(self):
        self.HP = self.maxHP + 2 * map_for_boss.map_number * random.randint(1, 6) + random.randint(1, 6)

        self.DP = map_for_boss.map_number / 2 * random.randint(1, 6) + int(random.randint(1, 6) / 2)
        self.SP = map_for_boss.map_number * random.randint(1, 6) + map_for_boss.map_number
    def reset(self):

        self.x = random.randint(0, 4)
        self.y = random.randint(5, 9)
        tuple_check = (self.x, self.y)
        while tuple_check in wall_coords:
            self.x = random.randint(0, 4)
            self.y = random.randint(5, 9)
            tuple_check = (self.x, self.y)
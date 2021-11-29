import random
from IntermediaryForMapCreation import *
map = game_map()

class Hero():

    def __init__(self):
        self.x = 0
        self.y = 0
        self.img = "hero_down"

    def move(self, x = 0, y = 0):
        self.x += x
        self.y += y
    def stats(self):
        self.HP = 20 + 3 * random.randint(1,6)
        self.maxHP = self.HP
        self.DP = 2 * random.randint(1,6)
        self.SP = 5 + random.randint(1,6)
    def strike(self):
        self.SP_Value = self.SP + 2* random.randint(1,6)
    def receive_strike(self, strike_back = 0):
        self.HP -= strike_back
        if self.HP <0:
            self.img = "skull"
    def level_up(self):
        self.HP = random.randint(1,6) + self.maxHP
        self.DP += random.randint(1,6)
        self.SP += random.randint(1, 6)
    def reset(self):
        self.x = 0
        self.y = 0
    def heal_up(self):
        self.HP += 5 + map.map_number
    def strike_up(self):
        self.SP += 3 + map.map_number


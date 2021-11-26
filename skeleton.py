import random
from Hero import Hero
def coords_check():
    IMG_SIZE = 72
    with open('first_map.txt', 'r') as map_display:
        map_key = map_display.readlines()
        ending_point = 0
        all_wall_coords = []
        coords = [0, 0]
        for line in range(len(map_key)):
            starting_point = 0
            for i in range(0, len(map_key[line])):
                if map_key[line][i] == "F":
                    starting_point += IMG_SIZE
                elif map_key[line][i] == "W":
                    starting_point += IMG_SIZE
                    coords[0] = int(starting_point / IMG_SIZE) - 1
                    coords[1] = int(ending_point / IMG_SIZE)
                    all_wall_coords.append(tuple(coords))
            ending_point += IMG_SIZE
        return all_wall_coords
wall_coords = coords_check()
floor_perimiter = [(1,-1),(2,-1),(3,-1),(4,-1),(5,-1),(6,-1),(7,-1),(8,-1),(9,-1),
                   (10,1),(10,2),(10,3),(10,4),(10,5),(10,6),(10,7),(10,8),(10,9),
                   (1,10),(2,10),(3,10),(4,10),(5,10),(6,10),(7,10),(8,10),(9,10),
                   (-1,1),(-1,2),(-1,3),(-1,4),(-1,5),(-1,6),(-1,7),(-1,8),(-1,9),(-1,-1),(10,0)]


class skeleton_1(Hero):


    def __init__(self):
        self.img = "skeleton"
        self.key_holder = random.choice([0,1])
        self.x = random.randint(4, 9)
        self.y = random.randint(0, 4)
        position_check = (self.x, self.y)
        while position_check in coords_check():
            self.x = random.randint(4, 9)
            self.y = random.randint(0, 4)
            position_check = (self.x, self.y)

    def move_skeleton1(self):

        top = (self.x, self.y-1)
        right = (self.x+1, self.y)
        left = (self.x-1, self.y)
        bottom = (self.x, self.y+1)
        possibility_array = [top,right,left,bottom ]
        move_to_list =[]
        for item in possibility_array:

            if item  not in wall_coords and item not in floor_perimiter:
                move_to_list.append(item)
                continue

        move_to_these_coords = random.choice(move_to_list)
        self.x = move_to_these_coords[0]
        self.y = move_to_these_coords[1]
    def stats(self, x = 1):
        self.HP = 2 * x * random.randint(1,6)
        self.DP = x/2 * random.randint(1, 6)
        self.SP = x  * random.randint(1,6)

    def receive_strike(self, SP_value = 0):

        self.HP -= SP_value
        self.strike_back = self.SP + 2 * random.randint(1, 6)

        if self.HP <0:
            self.HP = 0
            self.img = "ghost"
    def Is_key_holder(self, x= 0):
        self.key_holder = x
    def Level_up(self):
        pass


class skeleton_2(Hero):

    def __init__(self):
        self.img = "skeleton"
        self.x = random.randint(7, 9)
        self.y = random.randint(5, 9)
        self.key_holder = random.choice([0, 1])
        position_check = (self.x, self.y)
        while position_check in coords_check():
            self.x = random.randint(7, 9)
            self.y = random.randint(5, 9)
            position_check = (self.x, self.y)

    def move_skeleton2(self):

        top = (self.x, self.y-1)
        right = (self.x+1, self.y)
        left = (self.x-1, self.y)
        bottom = (self.x, self.y+1)
        possibility_array = [top,right,left,bottom ]
        move_to_list =[]
        for item in possibility_array:

            if item  not in wall_coords and item not in floor_perimiter:
                move_to_list.append(item)
                continue

        move_to_these_coords = random.choice(move_to_list)
        self.x = move_to_these_coords[0]
        self.y = move_to_these_coords[1]

    def stats(self, x=1):
        self.HP = 2 * x * random.randint(1, 6)
        self.DP = x / 2 * random.randint(1, 6)
        self.SP = x * random.randint(1, 6)

    def receive_strike(self, SP_value=0):

        self.HP -= SP_value
        self.strike_back = self.SP + 2 * random.randint(1, 6)

        if self.HP < 0:
            self.HP = 0
            self.img = "ghost"
    def Is_key_holder(self, x= 0):
        self.key_holder = x
    def Level_up(self):
        pass

class skeleton_3(Hero):

    def __init__(self):
        self.img = "skeleton"
        self.x = random.randint(4, 6)
        self.y = random.randint(5, 9)
        self.key_holder = random.choice([0, 1])
        position_check = (self.x, self.y)
        while position_check in coords_check():
            self.x = random.randint(4, 6)
            self.y = random.randint(5, 9)
            position_check = (self.x, self.y)

    def move_skeleton3(self):

        top = (self.x, self.y - 1)
        right = (self.x + 1, self.y)
        left = (self.x - 1, self.y)
        bottom = (self.x, self.y + 1)
        possibility_array = [top, right, left, bottom]
        move_to_list = []
        for item in possibility_array:

            if item not in wall_coords and item not in floor_perimiter:
                move_to_list.append(item)
                continue

        move_to_these_coords = random.choice(move_to_list)
        self.x = move_to_these_coords[0]
        self.y = move_to_these_coords[1]

    def stats(self, x=1):
        self.HP = 2 * x * random.randint(1, 6)
        self.DP = x / 2 * random.randint(1, 6)
        self.SP = x * random.randint(1, 6)

    def receive_strike(self, SP_value=0):

        self.HP -= SP_value
        self.strike_back = self.SP + 2 * random.randint(1, 6)

        if self.HP < 0:
            self.HP = 0
            self.img = "ghost"
    def Is_key_holder(self, x= 0):
        self.key_holder = x
    def Level_up(self):
        pass
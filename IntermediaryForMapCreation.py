
class game_map():
    def __init__(self):
        self.map_path = "map1.txt"
        self.map_number = 1
        self.perimeter = [(1,-1),(2,-1),(3,-1),(4,-1),(5,-1),(6,-1),(7,-1),(8,-1),(9,-1),
                   (10,1),(10,2),(10,3),(10,4),(10,5),(10,6),(10,7),(10,8),(10,9),
                   (1,10),(2,10),(3,10),(4,10),(5,10),(6,10),(7,10),(8,10),(9,10),
                   (-1,1),(-1,2),(-1,3),(-1,4),(-1,5),(-1,6),(-1,7),(-1,8),(-1,9),(-1,-1),(10,0),(0,10)]
    def go_next_map(self):
        self.map_number += 1
        self.map_path = "map" + str(self.map_number) +".txt"



    def coords_check(self):
        IMG_SIZE = 72
        with open(self.map_path, 'r') as map_display:
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



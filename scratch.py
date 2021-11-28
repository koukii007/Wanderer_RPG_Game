import random
def generate_new_map():
    with open('map.txt', 'w+') as allmapfile:

        for j in range(0,10):
            line = ""
            for i in range(0,10):
                line += random.choice(['F','F','F','F','F','W','F','W','F','W'])

            line += "\n"
            allmapfile.write(line)
class draw:
    def __init__(self):
        self.map_key = None
        self.map_path = "map1.txt"
        self.map_counter = 1
    def update_map(self):
        self.map_counter += 1

        self.map_path = "map" + str(self.map_counter) + ".txt"

map = draw()
print(map.map_counter)
map.update_map()
print(map.map_counter)
print(map.map_path)
map_counter = 1
def update_map():
    map_counter += 1
    file = "map" + str(map_counter) + ".txt"
    return file

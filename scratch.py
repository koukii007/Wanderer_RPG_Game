with open('map.txt', 'r') as map_display:
    map_key = map_display.readlines()
    for line in range(0, len(map_key)):
        for i in range(0,len(map_key[line])):
            if map_key[line][i] == "F":
                print(map_key[line][i])

            elif map_key[line][i] == "W":
                print(map_key[line][i])


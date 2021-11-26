if top in wall_coords and (bottom not in wall_coords and right not in wall_coords and left not in wall_coords):
    print(position_check)
    print(top, right, left, bottom)
    flip_coin = random.choice([0, 1])
    if flip_coin == 0:
        self.xskeleton1 += random.choice([-1, 1])
    else:
        self.yskeleton1 -= 1

elif top in wall_coords and right in wall_coords and (bottom not in wall_coords and left not in wall_coords):
    print(position_check)
    print(top, right, left, bottom)
    flip_coin = random.choice([0, 1])
    if flip_coin == 0:
        self.xskeleton1 -= 1
    else:
        self.yskeleton1 += 1

elif top in wall_coords and right in wall_coords and bottom in wall_coords and left not in wall_coords:
    print(position_check)
    print(top, right, left, bottom)
    self.xskeleton1 -= 1
    self.yskeleton1 += 0
elif right in wall_coords and (bottom not in wall_coords and top not in wall_coords and left not in wall_coords):
    print(position_check)
    print(top, right, left, bottom)
    flip_coin = random.choice([0, 1])
    if flip_coin == 0:
        self.xskeleton1 -= 1
    else:
        self.yskeleton1 += random.choice([-1, 1])
elif left in wall_coords and (bottom not in wall_coords and top not in wall_coords and right not in wall_coords):
    print(position_check)
    print(top, right, left, bottom)
    flip_coin = random.choice([0, 1])
    if flip_coin == 0:
        self.xskeleton1 += 1
    else:
        self.yskeleton1 += random.choice([-1, 1])
elif bottom in wall_coords and (left not in wall_coords and top not in wall_coords and right not in wall_coords):
    print(position_check)
    print(top, right, left, bottom)
    flip_coin = random.choice([0, 1])
    if flip_coin == 0:
        self.xskeleton1 += 1
    else:
        self.yskeleton1 += random.choice([-1, 1])
elif top in wall_coords and left in wall_coords and (right not in wall_coords and bottom not in wall_coords):
    print(position_check)
    print(top, right, left, bottom)
    flip_coin = random.choice([0, 1])
    if flip_coin == 0:
        self.xskeleton1 += 1
    else:
        self.yskeleton1 += random.choice([-1, 1])
elif bottom in wall_coords and right in wall_coords and (left not in wall_coords and top not in wall_coords):
    print(position_check)
    print(top, right, left, bottom)
    self.xskeleton1 -= 1
    self.yskeleton1 -= 1

elif top in wall_coords and bottom in wall_coords and (right not in wall_coords and left not in wall_coords):
    print(position_check)
    print(top, right, left, bottom)
    self.xskeleton1 += random.choice([-1, 1])
    self.yskeleton1 += 0
elif right in wall_coords and left in wall_coords and (top not in wall_coords and bottom not in wall_coords):
    print(position_check)
    print(top, right, left, bottom)
    self.xskeleton1 += 0
    self.yskeleton1 += random.choice([-1, 1])
elif top in wall_coords and right in wall_coords and bottom in wall_coords and left in wall_coords:
    pass


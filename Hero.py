class Hero:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.img = "hero_down"

    def move(self, x = 0, y = 0):
        self.x += x
        self.y += y
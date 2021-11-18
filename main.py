from tkinter import *
from Hero import Hero

IMG_SIZE = 72
WIDTH = 10 * IMG_SIZE
HEIGHT = 10 * IMG_SIZE

root = Tk()
root.title('Wanderer Game')
canvas = Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

hero = Hero()

# This method is called continuously by the main game loop
def draw_screen():
    canvas.delete("all")
    canvas.create_image(0, 0, image=root.floor, anchor=NW)
    canvas.create_image(IMG_SIZE, 0, image=root.wall, anchor=NW)
    canvas.create_image(2 * IMG_SIZE, 0, image=root.skeleton, anchor=NW)
    canvas.create_image(3 * IMG_SIZE, 0, image=root.boss, anchor=NW)
    canvas.create_image(hero.x * IMG_SIZE, hero.y * IMG_SIZE, image=getattr(root, hero.img), anchor=NW)

# Loading images. You can access these loaded images from the root object.
# For example: root.floor or getattr(root, "floor")
def load_images():
    dir = "images/"
    root.floor = PhotoImage(file=dir + "floor.png")
    root.wall = PhotoImage(file=dir + "wall.png")
    root.hero_down = PhotoImage(file=dir + "hero-down.png")
    root.hero_up = PhotoImage(file=dir + "hero-up.png")
    root.hero_right = PhotoImage(file=dir + "hero-right.png")
    root.hero_left = PhotoImage(file=dir + "hero-left.png")
    root.skeleton = PhotoImage(file=dir + "skeleton.png")
    root.boss = PhotoImage(file=dir + "boss.png")

load_images()

# Binding keyboard key events to functions
def leftKey(event):
    hero.move(x = -1)

def rightKey(event):
    hero.move(x = 1)

def upKey(event):
    hero.move(y = -1)

def downKey(event):
    hero.move(y = 1)

root.bind('<Left>', leftKey)
root.bind('<Right>', rightKey)
root.bind('<Up>', upKey)
root.bind('<Down>', downKey)

# Don't write anything after this while loop, because that won't be executed
# The main game loop, at the moment it calls the draw_screen function continuously
while True:
    draw_screen()
    root.update_idletasks()
    root.update()

import random
from tkinter import *
from Hero import Hero
from skeleton import skeleton
from BOSS import BOSS
from sounds import *
import pygame
import os

IMG_SIZE = 72
WIDTH = 10 * IMG_SIZE
HEIGHT = 10 * IMG_SIZE

root = Tk()
root.title('Wanderer Game')
canvas = Canvas(root, width=WIDTH+300, height=HEIGHT)

canvas.pack()

pygame.mixer.init()

path = os.getcwd()
stop_button_img = PhotoImage(file=path + "\\images\\cutsound.png")
play_button_img = PhotoImage(file=path + "\\images\\playsound.png")
stop_music_button = Button(root, text="stop music", image=stop_button_img, command=stop_music, height=38,
                           width=40)
stop_music_button.place(x=970, y=674)
play_music_button = Button(root, text="play music", image=play_button_img, command=play_background_music,
                           height=38,
                           width=40)
play_music_button.place(x=915, y=674)

play_background_music()
stop_music()



hero = Hero()
hero.stats()
skeleton1 = skeleton()
skeleton2 = skeleton()
skeleton3 = skeleton()
skeleton1.stats()
skeleton2.stats()
skeleton3.stats()
Boss =BOSS()
Boss.stats()



class draw():

    def __init__(self):
        self.map_key = None

    def draw_map(self):

        canvas.delete("all")
        if not self.map_key:
            with open('map.txt', 'r') as map_display:
                self.map_key = map_display.readlines()
            ending_point = 0
            all_wall_coords = []
            temp_coords = [0,0]
            for line in range(len(self.map_key)):
                starting_point = 0
                for i in range(0, len(self.map_key[line])):
                    if self.map_key[line][i] == "F":
                        canvas.create_image(starting_point, ending_point, image=root.floor, anchor=NW)
                        starting_point += IMG_SIZE
                    elif self.map_key[line][i] == "W":
                        canvas.create_image(starting_point, ending_point, image=root.wall, anchor=NW)
                        starting_point += IMG_SIZE
                        temp_coords[0] = int(starting_point/IMG_SIZE)-1
                        temp_coords[1] = int(ending_point/IMG_SIZE)
                        all_wall_coords.append(tuple(temp_coords))

                ending_point += IMG_SIZE
            return  all_wall_coords

    def draw_characters(self):
        canvas.create_image(hero.x * IMG_SIZE, hero.y * IMG_SIZE, image=getattr(root, hero.img), anchor=NW)
        canvas.create_image(skeleton1.xskeleton1 * IMG_SIZE, skeleton1.yskeleton1 * IMG_SIZE, image=getattr(root, skeleton1.img), anchor=NW)
        canvas.create_image(skeleton2.xskeleton2 * IMG_SIZE, skeleton2.yskeleton2 * IMG_SIZE, image=getattr(root, skeleton2.img), anchor=NW)
        canvas.create_image(skeleton3.xskeleton3 * IMG_SIZE, skeleton3.yskeleton3 * IMG_SIZE, image=getattr(root, skeleton3.img), anchor=NW)
        canvas.create_image(Boss.xBoss * IMG_SIZE, Boss.yBoss * IMG_SIZE, image=getattr(root, "boss"), anchor=NW)


class show_stats():

    def draw_stats(self):
        canvas.create_rectangle(723,3,1020,720, fill = "#FDDEC7", width = 3)
        canvas.create_rectangle(733, 13, 1007, 100, fill="#EDD7F5", width=2)
        canvas.create_text(870,55,text = "STATS" ,font = ("arial",50,"bold"), fill = "#FA545C")
        canvas.create_text(790, 140, text=f"\nHero HP : {hero.HP}\nHero DP : {hero.DP}\nHero SP : {hero.SP}", font=("arial", 16) , fill="black")
    def show_monster_stats(self):

        coords_hero = (hero.x, hero.y)
        coords_monster1 = (skeleton1.xskeleton1, skeleton1.yskeleton1)
        coords_monster2 = (skeleton2.xskeleton2, skeleton2.yskeleton2)
        coords_monster3 = (skeleton3.xskeleton3, skeleton3.yskeleton3)
        coords_Boss = (Boss.xBoss,Boss.yBoss)

        if coords_hero == coords_monster1:
            canvas.create_text(810, 220,
                               text=f"\nMonster HP : {skeleton1.HP}\nMonster DP : {skeleton1.DP}\nMonster SP : {skeleton1.SP}",
                               font=("arial", 16), fill="Red")
        elif coords_hero == coords_monster2:
            canvas.create_text(810, 220,
                               text=f"\nMonster HP : {skeleton2.HP}\nMonster DP : {skeleton2.DP}\nMonster SP : {skeleton2.SP}",
                               font=("arial", 16), fill="Red")
        elif coords_hero == coords_monster3:
            canvas.create_text(810, 220,
                               text=f"\nMonster HP : {skeleton3.HP}\nMonster DP : {skeleton3.DP}\nMonster SP : {skeleton3.SP}",
                               font=("arial", 16), fill="Red")
        elif coords_hero == coords_Boss:

            canvas.create_text(795, 220,
                               text=f"\nBoss HP : {Boss.HP}\nBoss DP : {Boss.DP}\nBoss SP : {Boss.SP}",
                               font=("arial", 16), fill="Red")


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
    root.strike = PhotoImage(file=dir +"strike.png")
    root.ghost = PhotoImage (file=dir + "ghost.png")
    root.key = PhotoImage(file=dir + "key.png")
load_images()


map = draw()
wall_coords = map.draw_map()
count = 0

def leftKey(event):


    position_check = (hero.x-1, hero.y)
    if 10 > hero.x > 0 and position_check not in wall_coords :
        hero.move(x = -1)
        hero.img = "hero_left"
        coords_hero = (hero.x, hero.y)
        coords_Boss = (Boss.xBoss, Boss.yBoss)
        if coords_hero == coords_Boss:
            Boss_sound()
    else:
        hero.img = "hero_down"

    global count
    count +=1

    if count < 2 :
        skeleton1.move_skeleton1()
        skeleton2.move_skeleton2()
        skeleton3.move_skeleton3()
        Boss.move()
    else:
        count =0

def rightKey(event):

    position_check = (hero.x + 1 , hero.y)
    if 9 > hero.x >= 0 and position_check not in wall_coords:
        hero.move(x = 1)
        hero.img = "hero_right"
        coords_hero = (hero.x, hero.y)
        coords_Boss = (Boss.xBoss, Boss.yBoss)
        if coords_hero == coords_Boss:
            Boss_sound()
    else:
        hero.img = "hero_down"

    global count
    count += 1

    if count < 2:
        skeleton1.move_skeleton1()
        skeleton2.move_skeleton2()
        skeleton3.move_skeleton3()
        Boss.move()
    else:
        count = 0

def upKey(event):

    position_check = (hero.x , hero.y-1)
    if 10 > hero.y > 0 and position_check not in wall_coords :
        hero.move(y = -1)
        hero.img = "hero_up"
        coords_hero = (hero.x, hero.y)
        coords_Boss = (Boss.xBoss, Boss.yBoss)
        if coords_hero == coords_Boss:
            Boss_sound()
    else:
        hero.img = "hero_down"

    global count
    count += 1

    if count < 2:
        skeleton1.move_skeleton1()
        skeleton2.move_skeleton2()
        skeleton3.move_skeleton3()
        Boss.move()
    else:
        count = 0

def downKey(event):


    position_check = (hero.x , hero.y +1 )
    if 9 > hero.y >= 0 and position_check not in wall_coords:
        hero.move(y = 1)
        hero.img = "hero_down"
        coords_hero = (hero.x, hero.y)
        coords_Boss = (Boss.xBoss, Boss.yBoss)
        if coords_hero == coords_Boss:
            Boss_sound()
    else:
        hero.img = "hero_up"

    global count
    count += 1

    if count < 2:
        skeleton1.move_skeleton1()
        skeleton2.move_skeleton2()
        skeleton3.move_skeleton3()
        Boss.move()
    else:
        count = 0
def space_key_press(event):

    for i in range(0,100):
        canvas.create_image(hero.x * IMG_SIZE, hero.y * IMG_SIZE,
                            image=getattr(root, "strike"), anchor=NW)
        canvas.create_image(hero.x * IMG_SIZE, hero.y * IMG_SIZE,
                            image=getattr(root, "strike"), anchor=NW)
    coords_hero = (hero.x, hero.y)
    coords_monster1 = (skeleton1.xskeleton1, skeleton1.yskeleton1)
    coords_monster2 = (skeleton2.xskeleton2, skeleton2.yskeleton2)
    coords_monster3 = (skeleton3.xskeleton3, skeleton3.yskeleton3)
    coords_Boss = (Boss.xBoss, Boss.yBoss)
    if coords_hero == coords_monster1:
        hero.strike()
        if hero.SP_Value > skeleton1.DP:
            skeleton1.receive_strike(hero.SP_Value)
            if skeleton1.HP > 0 :
                hero.receive_strike(skeleton1.strike_back)


    elif coords_hero == coords_monster2:
        hero.strike()
        if hero.SP_Value > skeleton2.DP:
            skeleton2.receive_strike(hero.SP_Value)
            if skeleton2.HP > 0 :
                hero.receive_strike(skeleton1.strike_back)
    elif coords_hero == coords_monster3:
        hero.strike()
        if hero.SP_Value > skeleton3.DP:
            skeleton3.receive_strike(hero.SP_Value)
            if skeleton3.HP > 0 :
                hero.receive_strike(skeleton1.strike_back)
            elif skeleton3.HP == 0:
                skeleton3.img = "key"
                
    elif coords_hero == coords_Boss :
        hero.strike()
        if hero.SP_Value > Boss.DP:
            Boss.receive_strike(hero.SP_Value)
            if Boss.HP > 0 :
                hero.receive_strike(Boss.strike_back)


root.bind('<Left>', leftKey)
root.bind('<a>', leftKey)
root.bind('<Right>', rightKey)
root.bind('<d>', rightKey)
root.bind('<Up>', upKey)
root.bind('<w>', upKey)
root.bind('<Down>', downKey)
root.bind('<s>', downKey)
root.bind('<space>', space_key_press)

# Don't write anything after this while loop, because that won't be executed
# The main game loop, at the moment it calls the draw_screen function continuously
clock = pygame.time.Clock()
stat_report = show_stats()
def move_skeletons():
    skeleton1.move_skeleton1()
    skeleton2.move_skeleton2()
    skeleton3.move_skeleton3()
while True:
    map = draw()
    map.draw_map()
    map.draw_characters()
    stat_report.draw_stats()
    stat_report.show_monster_stats()
    clock.tick(60)
    root.update_idletasks()
    root.update()

from tkinter import *
from tkinter import NW
from Hero import Hero
from skeleton import *
from BOSS import BOSS
from sounds import *
from key import key
from IntermediaryForMapCreation import *
from potion import *
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
next_level_img = PhotoImage(file=path + "\\images\\next.png")
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
skeleton1 = skeleton_1()
skeleton2 = skeleton_2()
skeleton3 = skeleton_3()
Boss = BOSS()
keys = key()
current_map = game_map()
spawn_potion = potion()
blue_potion = blue_potion()
class draw:

    def __init__(self):
        self.map_key = None

    def draw_characters(self):
        canvas.create_image(hero.x * IMG_SIZE, hero.y * IMG_SIZE, image=getattr(root, hero.img), anchor=NW)
        canvas.create_image(skeleton1.x * IMG_SIZE, skeleton1.y * IMG_SIZE, image=getattr(root, skeleton1.img), anchor=NW)
        canvas.create_image(skeleton2.x * IMG_SIZE, skeleton2.y * IMG_SIZE, image=getattr(root, skeleton2.img), anchor=NW)
        canvas.create_image(skeleton3.x * IMG_SIZE, skeleton3.y * IMG_SIZE, image=getattr(root, skeleton3.img), anchor=NW)
        canvas.create_image(Boss.x * IMG_SIZE, Boss.y * IMG_SIZE, image=getattr(root, Boss.img), anchor=NW)
        canvas.create_image(keys.x * IMG_SIZE, keys.y * IMG_SIZE, image=getattr(root, keys.img), anchor=NW)
        canvas.create_image(spawn_potion.x * IMG_SIZE, spawn_potion.y * IMG_SIZE, image=getattr(root, spawn_potion.img), anchor=NW)
        canvas.create_image(blue_potion.x * IMG_SIZE, blue_potion.y * IMG_SIZE, image=getattr(root, blue_potion.img),
                            anchor=NW)



    def draw_map(self):

        canvas.delete("all")
        if not self.map_key:
            if current_map.map_number != 10:
                with open(current_map.map_path, 'r') as map_display:
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
            elif current_map.map_number == 10 :
                root.destroy()

    def distribute_key(self):
        if skeleton1.key_holder == 1 :
            skeleton2.Is_key_holder(x = 0)
            skeleton3.Is_key_holder(x=0)
        elif skeleton2.key_holder == 1:
            skeleton1.Is_key_holder(x=0)
            skeleton3.Is_key_holder(x=0)
        elif skeleton3.key_holder == 1:
            skeleton1.Is_key_holder(x=0)
            skeleton2.Is_key_holder(x=0)
        elif skeleton1.key_holder == 0 and skeleton2.key_holder == 0 and skeleton3.key_holder == 0:
            skeleton2.Is_key_holder(x=1)





class show_stats():

    def draw_stats(self):
        canvas.create_rectangle(723,3,1020,720, fill = "#FDDEC7", width = 3)
        canvas.create_rectangle(733, 13, 1007, 100, fill="#EDD7F5", width=2)
        canvas.create_text(870,55,text = "STATS" ,font = ("arial",50,"bold"), fill = "#FA545C")
        canvas.create_text(790, 140, text=f"\nHero HP : {hero.HP}\nHero DP : {hero.DP}\nHero SP : {hero.SP}", font=("arial", 16) , fill="black")
        canvas.create_text(870,600, text=f"\n Your Mission it to eliminate the monsters"
                                          f"\n first then extract the key."
                                          f"\n Defeat the Boss, and you will"
                                          f"\n teleport to the next map."
                                          f"\n\n Press the space bar to strike."
                                          f"\n Press F to pick an item.", font=("arial", 11,"bold") , fill="red")
        canvas.create_text(870 , 490, text=f"\n CURRENT LEVEL -> {current_map.map_number}", font=("arial", 19, "bold"), fill="red")
        if keys.x == -2 and keys.y == -2:
            canvas.create_text(860, 300, text=f"You have successfully retrieved the key.",
                               font=("arial", 11), fill="blue")

    def show_monster_stats(self):

        coords_hero = (hero.x, hero.y)
        coords_monster1 = (skeleton1.x, skeleton1.y)
        coords_monster2 = (skeleton2.x, skeleton2.y)
        coords_monster3 = (skeleton3.x, skeleton3.y)
        coords_Boss = (Boss.x,Boss.y)
        red_potion = (spawn_potion.x,spawn_potion.y)
        blue_potion_coords = (blue_potion.x,blue_potion.y)

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
        elif coords_hero == red_potion:
            canvas.create_text(865, 350, text=f"\nPick up a red potion before a boss fight"
                                              f"\nto heal up.",
                               font=("arial", 10, "bold"), fill="red")
        elif coords_hero == blue_potion_coords:
            canvas.create_text(865, 350, text=f"\nPick up a blue potion to make your strikes"
                                              f"\nmore effective."
                                              ,
                               font=("arial", 10, "bold"), fill="blue")

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
    root.effect = PhotoImage(file=dir + "effect.png")
    root.gameover = PhotoImage(file=dir + "game_over.png")
    root.skull = PhotoImage(file=dir + "skull.png")
    root.potion = PhotoImage(file=dir + "potion.png")
    root.blue_potion = PhotoImage(file=dir + "blue_potion.png")
load_images()

map = draw()

count = 0

def leftKey(event):

    current_map.coords_check()

    position_check = (hero.x-1, hero.y)
    if 10 > hero.x > 0 and position_check not in current_map.coords_check() :
        if hero.HP != 0:
            hero.move(x = -1)
            hero.img = "hero_left"
            coords_hero = (hero.x, hero.y)
            coords_Boss = (Boss.x, Boss.y)
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
        if Boss.HP != 0:
            Boss.move()
    else:
        count =0
def rightKey(event):
    current_map.coords_check()
    position_check = (hero.x + 1 , hero.y)
    if 9 > hero.x >= 0 and position_check not in current_map.coords_check():
        if hero.HP != 0:
            hero.move(x = 1)
            hero.img = "hero_right"
            coords_hero = (hero.x, hero.y)
            coords_Boss = (Boss.x, Boss.y)
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
        if Boss.HP != 0:
            Boss.move()
    else:
        count = 0
def upKey(event):
    current_map.coords_check()
    position_check = (hero.x , hero.y-1)
    if 10 > hero.y > 0 and position_check not in current_map.coords_check():
        if hero.HP != 0:
            hero.move(y = -1)
            hero.img = "hero_up"
            coords_hero = (hero.x, hero.y)
            coords_Boss = (Boss.x, Boss.y)
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
        if Boss.HP != 0:
            Boss.move()
    else:
        count = 0

def downKey(event):
    current_map.coords_check()
    position_check = (hero.x, hero.y +1)
    if 9 > hero.y >= 0 and position_check not in current_map.coords_check():
        if hero.HP != 0:
            hero.move(y=1)
            hero.img = "hero_down"
            coords_hero = (hero.x, hero.y)
            coords_Boss = (Boss.x, Boss.y)
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
        if Boss.HP != 0:
            Boss.move()
    else:
        count = 0

def space_key_press(event):
    current_map.coords_check()
    for i in range(0,100):
        canvas.create_image(hero.x * IMG_SIZE, hero.y * IMG_SIZE,
                            image=getattr(root, "strike"), anchor=NW)
        canvas.create_image(hero.x * IMG_SIZE, hero.y * IMG_SIZE,
                            image=getattr(root, "strike"), anchor=NW)
    coords_hero = (hero.x, hero.y)
    coords_monster1 = (skeleton1.x, skeleton1.y)
    coords_monster2 = (skeleton2.x, skeleton2.y)
    coords_monster3 = (skeleton3.x, skeleton3.y)
    coords_Boss = (Boss.x, Boss.y)
    if coords_hero == coords_monster1:
        hero.strike()
        if hero.SP_Value > skeleton1.DP:
            skeleton1.receive_strike(hero.SP_Value)
            if skeleton1.HP > 0:
                hero.receive_strike(skeleton1.strike_back)
            elif skeleton1.HP == 0:
                if skeleton1.key_holder == 1:
                    keys.receive_position(x=skeleton1.x, y=skeleton1.y)

                else:
                    pass
    elif coords_hero == coords_monster2:
        hero.strike()
        if hero.SP_Value > skeleton2.DP:
            skeleton2.receive_strike(hero.SP_Value)
            if skeleton2.HP > 0:
                hero.receive_strike(skeleton1.strike_back)
            elif skeleton2.HP == 0:
                if skeleton2.key_holder == 1:
                    keys.receive_position(x=skeleton2.x, y=skeleton2.y)
                else:
                    pass
    elif coords_hero == coords_monster3:
        hero.strike()
        if hero.SP_Value > skeleton3.DP:
            skeleton3.receive_strike(hero.SP_Value)
            if skeleton3.HP > 0:
                hero.receive_strike(skeleton1.strike_back)
            elif skeleton3.HP == 0:
                if skeleton3.key_holder == 1:
                    keys.receive_position(x=skeleton3.x, y=skeleton3.y)
                else:
                    pass

    elif coords_hero == coords_Boss and skeleton1.HP == 0 and skeleton2.HP == 0 and skeleton3.HP == 0:
        hero.strike()
        if hero.SP_Value > Boss.DP:
            Boss.receive_strike(hero.SP_Value)
            if Boss.HP > 0:
                hero.receive_strike(Boss.strike_back)
            elif Boss.HP ==0 and skeleton1.HP == 0 and skeleton2.HP == 0 and skeleton3.HP == 0 and keys.x == -2 and keys.y == -2:
                # next_level_button(770,430)
                next_level = Button(root, text="Next ->", image=next_level_img, command=reset_and_go, height=50,
                                    width=200)
                next_level.place(x=770, y=430)

def reset_and_go():
    if Boss.HP ==0 and skeleton1.HP == 0 and skeleton2.HP == 0 and skeleton3.HP == 0 and keys.x == -2 and keys.y == -2:
        current_map.go_next_map()
        current_map.coords_check()
        hero.reset()
        skeleton1.reset()
        skeleton2.reset()
        skeleton3.reset()
        Boss.reset()
        blue_potion.reset()
        spawn_potion.reset()
        hero.level_up()
        skeleton1.level_up()
        skeleton2.level_up()
        skeleton3.level_up()
        Boss.level_up()

def pick_up_key(event):
    hero_coords = (hero.x, hero.y)
    key_coords = (keys.x, keys.y)
    potion_coords = (spawn_potion.x,spawn_potion.y)
    blue_potion_coords = (blue_potion.x,blue_potion.y)
    if hero_coords == key_coords:
        keys.receive_position(x=-2,y=-2)
        for i in range(0, 100):
            canvas.create_image(hero.x * IMG_SIZE, hero.y * IMG_SIZE,
                                image=getattr(root, "effect"), anchor=NW)
    elif hero_coords == potion_coords:
        spawn_potion.receive_position(x=-2,y=-2)
        hero.heal_up()
        for i in range(0, 100):
            canvas.create_image(hero.x * IMG_SIZE, hero.y * IMG_SIZE,
                                image=getattr(root, "effect"), anchor=NW)
    elif hero_coords == blue_potion_coords:
        blue_potion.receive_position(x=-2,y=-2)
        hero.strike_up()
        for i in range(0, 100):
            canvas.create_image(hero.x * IMG_SIZE, hero.y * IMG_SIZE,
                                image=getattr(root, "effect"), anchor=NW)



root.bind('<Left>', leftKey)
root.bind('<a>', leftKey)
root.bind('<Right>', rightKey)
root.bind('<d>', rightKey)
root.bind('<Up>', upKey)
root.bind('<w>', upKey)
root.bind('<Down>', downKey)
root.bind('<s>', downKey)
root.bind('<space>', space_key_press)
root.bind('<f>', pick_up_key)

clock = pygame.time.Clock()
stat_report = show_stats()

while True:
    always_Update_coords_check = game_map()
    always_Update_coords_check.coords_check()
    map = draw()
    map.draw_map()
    map.draw_characters()
    map.distribute_key()
    stat_report.draw_stats()
    stat_report.show_monster_stats()
    clock.tick(50)
    root.update_idletasks()
    root.update()

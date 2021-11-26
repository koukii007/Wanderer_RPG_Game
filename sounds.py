import pygame
import os
path = os.getcwd()
def play_background_music():

    pygame.mixer.music.load(path + "\\sounds\\Pirate Battle Music - Walk the Plank.mp3")
    pygame.mixer.music.play(loops = 0)
def stop_music():

    pygame.mixer.music.stop()
def Boss_sound():
    pygame.mixer.music.load(path + "\\sounds\\Laughing Pirate.mp3")
    pygame.mixer.music.play(loops=0)


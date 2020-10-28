import os
import pygame
pygame.mixer.init()
pygame.mixer.set_num_channels(20)
class GameConstants:
    SCREEN_DIMENSIONS = (800,700)
    FRUIT_SIZE = (100 , 100)
    FRUIT_HALF_SIZE = (90 , 90)
    BG = pygame.transform.scale(pygame.image.load(os.path.join("Assets" , "bg.jpg")) , SCREEN_DIMENSIONS)
    MENU_BG = pygame.transform.scale(pygame.image.load(os.path.join("Assets" , "menu_bg.jpg")) , SCREEN_DIMENSIONS)
    HEART = pygame.transform.scale(pygame.image.load(os.path.join("Assets" , "heart.png")) , (20,20))
    GAME_START_SOUND = pygame.mixer.Sound(os.path.join("Assets" , "Sound" ,"Game-start.wav"))
    GAME_OVER_SOUND = pygame.mixer.Sound(os.path.join("Assets" , "Sound" ,"Game-over.wav"))
    SWORD_SOUNDS = pygame.mixer.Sound(os.path.join("Assets" , "Sound" ,f"VOLUME_Sword-swipe-7.wav"))
    SPLASH_SOUND = pygame.mixer.Sound(os.path.join("Assets" , "Sound" , "Splatter-Small-1.wav"))
    BOMB_EXPLODE_SOUND = pygame.mixer.Sound(os.path.join("Assets" , "Sound" , "Bomb-explode.wav"))
    THROW_FRUIT_SOUND = pygame.mixer.Sound(os.path.join("Assets" , "Sound" , "Throw-fruit.wav"))

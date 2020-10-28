import os
import pygame
from Game.Shared import GameConstants

class Scene:

    def __init__(self , game):
        self.__game = game
        self.__texts = []

    def render(self):
        for text in self.__texts:
            text[1][0] = (GameConstants.SCREEN_DIMENSIONS[0]//2)-(text[0].get_width()//2)
            self.__game.screen.blit(text[0] , text[1])

    def getGame(self):
        return self.__game

    def handleEvents(self , events):
        pass

    def clearText(self):
        self.__texts = []

    def addText(self , string , x=0 , y=0 , color=(255,255,255) , background = None , size = 20):
        font = pygame.font.Font( os.path.join("Assets" , "Fonts" , "zorque.ttf") , size)
        self.__texts.append([font.render(string , True , color , background) , [x,y]])

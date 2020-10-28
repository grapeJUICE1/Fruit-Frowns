import sys
import pygame
from Game.Scenes.Scene import Scene
from Game.Shared import GameConstants
from Game.Button import *

class MenuScene(Scene):
    def __init__(self , game):
        super(MenuScene , self).__init__(game)
        self.game = self.getGame()
        self.bg = GameConstants.MENU_BG.convert_alpha()
        self.play_button = Button((0,0,255) , (GameConstants.SCREEN_DIMENSIONS[0]//2)-150 , 350 , 300 , 60 , 'Play')
        self.about_button = Button((0,0,255) , (GameConstants.SCREEN_DIMENSIONS[0]//2)-300 , 450 , 600 , 60 , 'about')

    def render(self):
        self.clearText()
        self.game.getScreen.blit(self.bg , (0,0))
        self.addText("FRUIT  FROWNS" ,GameConstants.SCREEN_DIMENSIONS[0]//2-(110*3), 30 , size=90 , color=(255,255,255))
        self.addText(f"You high score is {self.game.getHighScore}" ,GameConstants.SCREEN_DIMENSIONS[0]//2-(50*5), 200 , size=50 , color=(255,255,255))
        self.play_button.draw(self.game.getScreen , 100)
        self.about_button.draw(self.game.getScreen , 100)
        super(MenuScene , self).render()


    def handleEvents(self , events):
        for event in events:
            if self.play_button.isOver(pygame.mouse.get_pos()):
                self.play_button.color = (0,0,139)
            elif self.about_button.isOver(pygame.mouse.get_pos()):
                self.about_button.color = (0,0,139)
            else:
                self.play_button.color = (0,0,255)
                self.about_button.color = (0,0,255)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.play_button.isOver(pygame.mouse.get_pos()):
                    self.game.changeScene(0)
                if self.about_button.isOver(pygame.mouse.get_pos()):
                    self.game.changeScene(3)



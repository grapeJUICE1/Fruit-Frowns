import sys
import pygame
from Game.Scenes.Scene import Scene
from Game.Shared import GameConstants
from Game.Button import *

class AboutScene(Scene):
    def __init__(self , game):
        super(AboutScene , self).__init__(game)
        self.game = self.getGame()
        self.bg = GameConstants.MENU_BG.convert_alpha()

    def render(self):
        self.clearText()
        self.game.getScreen.blit(self.bg , (0,0))
        self.addText(f"About" ,(GameConstants.SCREEN_DIMENSIONS[0]//2)-(70*4), 50 , size=70 , color=(255,255,255))
        self.addText("Press Esc key to go back to menu" ,(GameConstants.SCREEN_DIMENSIONS[0]//2)-(70*4), 150 , size=40 , color=(255,255,255))
        self.addText("Fruit Frowns is a game developed with python and pygame" ,(GameConstants.SCREEN_DIMENSIONS[0]//2)-(70*4), 220 , size=20 , color=(255,255,255))
        self.addText("inspired by fruit ninja..... Main theme of the game is" ,(GameConstants.SCREEN_DIMENSIONS[0]//2)-(70*4), 250 , size=20 , color=(255,255,255))
        self.addText("Fruits spawn randomly and you basically have to cut them" ,(GameConstants.SCREEN_DIMENSIONS[0]//2)-(70*4), 280 , size=20 , color=(255,255,255))
        self.addText("You can cut fruits with your mouse if your mouse passes" ,(GameConstants.SCREEN_DIMENSIONS[0]//2)-(70*4), 300 , size=20 , color=(255,255,255))
        self.addText("The Fruit...." ,(GameConstants.SCREEN_DIMENSIONS[0]//2)-(70*4), 330 , size=20 , color=(255,255,255))
        self.addText("Made with love by GrapeJUICE" ,(GameConstants.SCREEN_DIMENSIONS[0]//2)-(70*4), 400 , size=40 , color=(255,255,255))
        self.addText("github : https://github.com/grapeJUICE1" ,(GameConstants.SCREEN_DIMENSIONS[0]//2)-(70*4), 450 , size=30 , color=(255,255,255))
        super(AboutScene , self).render()


    def handleEvents(self , events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.game.changeScene(1)




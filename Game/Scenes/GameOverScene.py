import sys
import pygame
from Game.Scenes.Scene import Scene
from Game.Shared import GameConstants
from Game.Button import *

class GameOverScene(Scene):
    def __init__(self , game):
        super(GameOverScene , self).__init__(game)
        self.game = self.getGame()
        self.bg = GameConstants.MENU_BG.convert_alpha()
        self.play_button = Button((0,0,255) , (GameConstants.SCREEN_DIMENSIONS[0]//2)-200 , 300 , 400 , 60 , 'Play Again')
        self.menu_button = Button((0,0,255) , (GameConstants.SCREEN_DIMENSIONS[0]//2)-300 , 400 , 600 , 60 , 'Main Menu')

    def render(self):
        self.clearText()
        self.game.getScreen.blit(self.bg , (0,0))
        self.addText(f"You score is {self.game.getScore}" ,(GameConstants.SCREEN_DIMENSIONS[0]//2)-(70*4), 50 , size=70 , color=(255,255,255))
        self.play_button.draw(self.game.getScreen , 100)
        self.menu_button.draw(self.game.getScreen , 100)
        super(GameOverScene , self).render()


    def handleEvents(self , events):
        for event in events:
            if self.play_button.isOver(pygame.mouse.get_pos()):
                self.play_button.color = (0,0,139)
            elif self.menu_button.isOver(pygame.mouse.get_pos()):
                self.menu_button.color = (0,0,139)
            else:
                self.play_button.color = (0,0,255)
                self.menu_button.color = (0,0,255)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.play_button.isOver(pygame.mouse.get_pos()):
                    self.game.reset()
                    self.game.changeScene(0)
                elif self.menu_button.isOver(pygame.mouse.get_pos()):
                    self.game.reset()
                    self.game.changeScene(1)



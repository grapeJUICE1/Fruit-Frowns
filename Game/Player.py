import pygame
from Game.Shared import *

class Player(GameObject):
    def __init__(self, pos, size=0, sprite=0):
        super(Player , self).__init__(pos, size, sprite)
        self.draw = False
        self.last_pos = None






import math
import pygame
from Game.Shared import *


class Fruit(GameObject):
    def __init__(self, pos, angle, size=0, sprite=0, color="red", name="apple"):
        super(Fruit, self).__init__(pos, size, sprite)
        self.name = name
        self.color = color
        self.angle = angle
        self.X = pos[0]
        self.Y = pos[1]
        self.x = pos[0]
        self.y = pos[1]
        self.velocity = 90
        self.vx = self.velocity * math.cos(math.radians(angle))
        self.vy = self.velocity * math.sin(math.radians(angle))
        self.tx = 0
        self.ty = 0
        self.txIncreamentsBy = 0.16
        self.tyIncreamentsBy = 0.16
        self.gravity = 8.81
        self.tossed = False

    def checkCollision(self, player, linePos1, linePos2):
        if player.draw and linePos1 != None and linePos2 != None:
            temp_rect = pygame.Rect(
                self.x, self.y, GameConstants.FRUIT_SIZE[0], GameConstants.FRUIT_SIZE[1]
            )
            if temp_rect.clipline(linePos1, linePos2):
                return True

            return False

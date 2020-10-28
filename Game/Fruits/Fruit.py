import math
from Game.Shared import *
class Fruit(GameObject):
    def __init__(self ,pos, angle, size=0, sprite=0 , color='red', name='apple'):
        super(Fruit , self).__init__( pos, size, sprite)
        self.name = name
        self.color = color
        self.angle = angle
        self.X = pos[0]
        self.Y = pos[1]
        self.x= pos[0]
        self.y = pos[1]
        self.velocity=90
        self.vx= (self.velocity * math.cos(math.radians(angle)))
        self.vy= (self.velocity * math.sin(math.radians(angle)))
        self.tx=0
        self.ty=0
        self.txIncreamentsBy=0.16
        self.tyIncreamentsBy=0.16
        self.gravity = 8.81
        self.tossed = False

    def checkCollision(self , player , mousePos1 , mousePos2):
        if player.draw and player.last_pos != None:
            #collision detection between player and fruit ...

            x = player.last_pos[0]
            y = player.last_pos[1]
            sqx = (x - self.x)**2
            sqy = (y - self.y)**2

            x_2 = mousePos1[0]
            y_2 = mousePos1[1]
            sqx_2 = (x_2 - self.x)**2
            sqy_2 = (y_2 - self.y)**2

            x_3 = mousePos2[0]
            y_3 = mousePos2[1]
            sqx_3 = (x_3 - self.x)**2
            sqy_3 = (y_3 - self.y)**2

            if math.sqrt(sqx + sqy) < GameConstants.FRUIT_SIZE[0]/2 or math.sqrt(sqx_2 + sqy_2) < GameConstants.FRUIT_SIZE[0]/2 or math.sqrt(sqx_3 + sqy_3) < GameConstants.FRUIT_SIZE[0]/2:
                return True

            return False





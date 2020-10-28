import math
class GameObject:
    def __init__(self, pos, size, sprite):
        self.__pos = pos
        self.__sprite = sprite
        self.__size = size

    @property
    def getPos(self):
        return self.__pos

    @property
    def getSprite(self):
        return self.__sprite

    @property
    def getSize(self):
        return self.__size

    def setPos(self, newPos):
        self.__pos = newPos

    def setSprite(self, newSprite):
        self.__sprite = newSprite

    def setSize(self, newSize):
        self.__size = newSize





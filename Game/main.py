import fixModuleNotFoundError
import random, os, enum
import pygame
from Game.Shared import *
from Game.Scenes import *
from Game.Fruits import Fruit
from Player import Player


class FruitColors(enum.Enum):
    apple = "red"
    banana = "yellow"
    pineapple = "yellow"
    coconut = "transparent"
    bomb = "explosion"
    watermelon = "red"
    orange = "orange"


class Game:
    def __init__(self):
        self.__lives = 10
        self.__score = 0
        f = open(os.path.join("highscore.dat"), "r")
        self.__high_score = int(f.read())

        pygame.init()
        pygame.display.set_caption("Fruit Frowns")

        self.__clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(GameConstants.SCREEN_DIMENSIONS)
        self.__currentScene = 1
        self.__player = Player((400, 350), (400, 300))
        self.__fruitTypes = [
            "apple",
            "orange",
            "banana",
            "pineapple",
            "coconut",
            "watermelon",
            "bomb",
        ]
        self.__fruits = self.createFruits()
        self.__scenes = (
            PlayingGameScene(self),
            MenuScene(self),
            GameOverScene(self),
            AboutScene(self),
        )

    def start(self):
        while 1:
            self.__clock.tick(60)
            self.screen.fill((0, 0, 0))
            currentScene = self.__scenes[self.__currentScene]
            currentScene.render()
            currentScene.handleEvents(pygame.event.get())
            pygame.display.update()

    @property
    def getLives(self):
        return self.__lives

    @property
    def getScore(self):
        return self.__score

    @property
    def getDisplay(self):
        return self.screen

    @property
    def getPlayer(self):
        return self.__player

    @property
    def getScreen(self):
        return self.screen

    @property
    def getFruits(self):
        return self.__fruits

    @property
    def getHighScore(self):
        return self.__high_score

    def setHighScore(self, newHighScore):
        self.__high_score = newHighScore

    def createFruits(self):
        fruit = random.sample(self.__fruitTypes, len(self.__fruitTypes))
        return [
            Fruit(
                name=fruit[i - 1],
                pos=(
                    random.randint(300, GameConstants.SCREEN_DIMENSIONS[0] - 200),
                    random.randint(
                        GameConstants.SCREEN_DIMENSIONS[1],
                        GameConstants.SCREEN_DIMENSIONS[1] + 20,
                    ),
                ),
                angle=random.randint(70, 115),
                sprite=pygame.transform.scale(
                    pygame.image.load(os.path.join("Assets", f"{fruit[i-1]}.png")),
                    GameConstants.FRUIT_SIZE,
                ),
                color=f"{FruitColors[fruit[i-1]].value}",
            )
            for i in range(random.randint(4, 7))
        ]

    def removeFruit(self, fruit):
        self.__fruits.remove(fruit)

    def increaseLives(self, amount):
        self.__lives += amount

    def reduceLives(self, amount):
        self.__lives -= amount

    def increaseScore(self, amount):
        self.__score += amount

    def changeScene(self, scene):
        self.reset()
        self.__currentScene = scene

    def reset(self):
        self.__lives = 10
        self.__score = 0
        self.fruits = []


game = Game()
game.start()

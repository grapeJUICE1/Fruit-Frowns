import sys , math , os , copy
import pygame
from Game.Scenes.Scene import Scene
from Game.Shared import GameConstants

class PlayingGameScene(Scene):

    def __init__(self , game ):
        super(PlayingGameScene , self).__init__(game)
        self.game = self.getGame()
        self.gamePlayer = None
        self.mouse_position = (0, 0)
        self.fruits = self.game.createFruits()
        self.splashes = []
        self.cutFruits = []
        self.last = pygame.time.get_ticks()
        self.cooldown = 2000
        self.soundChannel = 0
        self.soundStarted = False
        self.bg = GameConstants.BG.convert_alpha()
        self.heart_x = 2
        self.heart_y = 5


    def render(self):

        self.clearText()
        self.game.getScreen.blit(self.bg , (0,0))
        if self.soundStarted == False:
            GameConstants.GAME_START_SOUND.play()
            self.soundStarted = True

        self.Player = self.game.getPlayer

        for fruit in self.fruits:
            self.renderBall(fruit)

        for life in range(self.game.getLives+1):
            self.game.getScreen.blit(GameConstants.HEART , (self.heart_x , self.heart_y))
            self.heart_x+=20

        self.heart_x = 2

        for splash in self.splashes:
            self.game.getScreen.blit(splash[0] , splash[1] )
        self.addText(f"{self.game.getScore}" , GameConstants.SCREEN_DIMENSIONS[0]//2 - 50 , 30 , size=50)

        for cutFruit in self.cutFruits:

            self.game.getScreen.blit(cutFruit[0] , cutFruit[1])
            if cutFruit[1][1] > GameConstants.SCREEN_DIMENSIONS[1]:
                if cutFruit in self.cutFruits:
                    self.cutFruits.remove(cutFruit)
            cutFruit[1][1] += 8


        super(PlayingGameScene , self).render()

    def renderPlayer(self):
        if (self.Player.draw):
            self.mouse_position = pygame.mouse.get_pos()
            if self.Player.last_pos is not None:
                line = pygame.draw.line(self.game.getScreen, (255,0,0), self.Player.last_pos, self.mouse_position, 8)
                GameConstants.SWORD_SOUNDS.play()

            self.Player.last_pos = self.mouse_position




    def renderBall(self , fruit):
        if self.soundChannel == 1:
            self.soundChannel = 9
        if self.soundChannel >= 19:
            self.soundChannel = 9
        self.soundChannel+=1
        fruit.tx += fruit.txIncreamentsBy
        fruit.ty += fruit.tyIncreamentsBy
        fruit.x = int(fruit.X+(fruit.vx*fruit.tx))
        fruit.y = int(fruit.Y -(fruit.vy*fruit.ty - (fruit.gravity/2)*fruit.ty*fruit.ty))
        if fruit.x <= 0:
            fruit.txIncreamentsBy*=-1
        elif fruit.x+GameConstants.FRUIT_SIZE[0] > GameConstants.SCREEN_DIMENSIONS[0]:
            fruit.txIncreamentsBy*=-1
        if fruit.y <= GameConstants.SCREEN_DIMENSIONS[1]:
            fruit.tossed = True

        self.game.getScreen.blit(fruit.getSprite , (fruit.x , fruit.y))




    def handleEvents(self , events):
            self.Player = self.game.getPlayer
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    self.renderPlayer()

                elif event.type == pygame.MOUSEBUTTONUP:
                    self.mouse_position = (0, 0)
                    self.Player.draw = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.Player.draw = True


                for fruit in self.fruits:
                    if fruit in self.fruits and fruit.tossed == True and (fruit.y > GameConstants.SCREEN_DIMENSIONS[1]):
                        self.fruits.remove(fruit)
                        if fruit.name != 'bomb':
                            self.game.reduceLives(1)

                    if fruit in self.fruits and fruit.checkCollision(self.Player , self.Player.last_pos , self.mouse_position):
                        if self.soundChannel >= 8:
                            self.soundChannel = 1
                        self.soundChannel+=1
                        self.splashes.append([pygame.image.load(os.path.join("Assets" , f"splash_{fruit.color}_small.png")) , (fruit.x , fruit.y) , False])
                        self.fruits.remove(fruit)

                        if fruit.name != 'bomb':
                            self.cutFruits.append([pygame.transform.scale(pygame.image.load(os.path.join("Assets" , f"{fruit.name}_half_1.png")) , GameConstants.FRUIT_HALF_SIZE) , [fruit.x , fruit.y]])
                            self.cutFruits.append([pygame.transform.scale(pygame.image.load(os.path.join("Assets" , f"{fruit.name}_half_2.png")) , GameConstants.FRUIT_HALF_SIZE) , [fruit.x , fruit.y + 60]])
                            self.game.increaseScore(10)
                            pygame.mixer.Channel(self.soundChannel).play(pygame.mixer.Sound(os.path.join("Assets" , "Sound" ,f"Impact-{fruit.name.capitalize()}.wav")))
                        else:
                            self.game.reduceLives(1)
                            GameConstants.BOMB_EXPLODE_SOUND.play()
                if self.Player.draw == False:
                    self.Player.last_pos = pygame.mouse.get_pos()

                if self.game.getLives <= 0:
                    GameConstants.GAME_OVER_SOUND.play()
                    f = open(os.path.join("highscore.dat"), "r")
                    if self.game.getScore > int(f.read()):
                        self.game.setHighScore(self.game.getScore)
                        f = open(os.path.join("highscore.dat"), "w")
                        f.write(f"{self.game.getScore}")
                        f.close()
                    self.game.changeScene(2)

                if self.splashes != []:
                    now = pygame.time.get_ticks()
                    if now - self.last >= self.cooldown:
                        self.last = now
                        self.splashes = []

                if self.fruits == []:
                    now = pygame.time.get_ticks()
                    if now - self.last >= self.cooldown:
                        self.last = now
                        self.splashes = []
                        self.fruits = self.game.createFruits()









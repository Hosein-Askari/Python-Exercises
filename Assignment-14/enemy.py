import random
import time
import arcade


class Enemy(arcade.Sprite):
    def __init__(self,game):
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")
        self.center_x = random.randrange(25,game.width-25)
        self.center_y = game.height+25
        self.angle = 180
        self.speed= 2
        self.height = 50
        self.width = 50
        self.creation_time=time.time()
    def move(self):
        self.center_y -= self.speed
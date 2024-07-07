import arcade
import random 

class Ball(arcade.Sprite):
    def __init__(self,game):
        super().__init__()
        self.center_x = game.width//2
        self.center_y = game.height//2
        self.change_x =random.choice([1,-1])
        self.change_y = random.choice([1,-1])
        self.color = arcade.color.WHITE
        self.radians = 15
        self.height=10
        self.width = 10
        self.speed = 4
        self.game = game
    def draw(self):
        arcade.draw_circle_filled(self.center_x,self.center_y,self.radians,self.color)

    def move(self):
        self.center_x += self.change_x*self.speed
        self.center_y += self.change_y*self.speed

        if self.top > self.game.height:    
            self.change_y = -1
        if self.bottom < 0:
            self.change_y = 1

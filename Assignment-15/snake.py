import random
import arcade
class Snake(arcade.Sprite):
    def __init__(self,game):
        super().__init__()
        self.width = 15
        self.height= 15
        self.center_x = game.width//2
        self.center_y = game.height//2
        self.change_x = 0
        self.change_y = 0
        self.speed = 0
        self.score = 0
        self.screen_Score =  0
        self.body =[]
        self.eat_sound=arcade.load_sound(":resources:sounds/coin1.wav")
        self.hurt_sound=arcade.load_sound(":resources:sounds/lose2.wav")
    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

    def eat(self,apple,score):
        
        del apple
        self.screen_Score += score
        if score>0:
            self.score += score
            arcade.play_sound(self.eat_sound)
        else:
            arcade.play_sound(self.hurt_sound)



    def draw(self):
        arcade.draw_rectangle_filled(self.center_x,self.center_y,32,32,arcade.color.BLACK,45)
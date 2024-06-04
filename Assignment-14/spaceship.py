import time
import arcade
from bullet import Bullet

class Space_ship(arcade.Sprite):
    def __init__(self,game):
        super().__init__(":resources:images/space_shooter/playerShip3_orange.png")
        self.center_x = 100
        self.center_y = 100
        self.change_x=0
        self.change_y=0
        self.speed = 4
        self.height = 50
        self.width = 50
        self.game_width=game.width
        self.game_height=game.height
        self.bullets=[]
        self.health = 3
        self.health_png =arcade.load_texture("Assignment-14/heart.png")
        self.score=0
        self.fire_sound=arcade.load_sound(":resources:sounds/hit1.wav")
        self.hit_enemy_sound =arcade.load_sound(":resources:sounds/explosion1.wav")
        self.hurt_sound = arcade.load_sound(":resources:sounds/hurt1.wav")
    def fire(self):
        new_bullet=Bullet(self)
        self.bullets.append(new_bullet)
        arcade.play_sound(self.fire_sound)

    def move(self):
        if self.change_x == 1:
            self.center_x += self.speed
        elif self.change_x == -1 :
            self.center_x -= self.speed
        elif self.change_y == 1:
            self.center_y += self.speed
        elif self.change_y == -1:
            self.center_y -= self.speed
      
        if self.left < 0:
            self.left = 0
        elif self.right > self.game_width -1 :
            self.right = self.game_width - 1

        if self.bottom < 0:
             self.bottom = 0
        elif self.top > self.game_height /3:
            self.top = self.game_height /3
    
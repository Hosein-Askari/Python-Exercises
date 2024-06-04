import arcade

class Bullet(arcade.Sprite):
    def __init__(self,spaceship):
        super().__init__(":resources:images/space_shooter/laserRed01.png")
        self.center_x=spaceship.center_x
        self.center_y=spaceship.top
        self.width = 10
        self.height = 10
        self.speed = 3



    def move(self):
        self.center_y += self.speed
import arcade

class Ball(arcade.Sprite):
    def __init__(self,game):
        super().__init__("Assignment-16/arkanoid/images/ball.png")
        self.center_x = 20
        self.center_y = 20
        self.change_x =1
        self.change_y = 1
        self.height=45
        self.width = 45
        self.speed = 4
        self.game = game
    

    def move(self):
        self.center_x += self.change_x*self.speed
        self.center_y += self.change_y*self.speed

        if self.top > self.game.height:    
            self.change_y = -1
        if self.right > self.game.width:
            self.change_x *= -1
        if self.left < 0 :
            self.change_x *= -1
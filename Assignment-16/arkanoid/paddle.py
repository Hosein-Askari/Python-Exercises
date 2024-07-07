import arcade


class Paddle (arcade.Sprite):
    def __init__(self,game):
        super().__init__("Assignment-16/arkanoid/images/paddle.png")
        self.center_x=game.width//2
        self.center_y=30
        self.width=200
        self.height=90
        self.change_x=0
        self.change_y=0
        self.speed = 4
        self.score= 0 
        self.health = 3
        self.health_png = arcade.load_texture("Assignment-16/arkanoid/images/paddle.png")
        self.hit = False
        self.hit_sound1 = arcade.load_sound(":resources:sounds/coin5.wav")
        self.hit_sound2 = arcade.load_sound(":resources:sounds/error3.wav")
        self.lose_sound = arcade.load_sound(":resources:sounds/lose2.wav")
        self.game = game

    def move(self):
        
        self.center_x += self.change_x*self.speed
        
        #if  self.center_y+self.speed < self.game_height-self.height   and      self.center_y-self.speed > self.height: it's not worrk

        if self.right > self.game.width:
            self.right = self.game.width
        if self.left <0:
            self.left = 0
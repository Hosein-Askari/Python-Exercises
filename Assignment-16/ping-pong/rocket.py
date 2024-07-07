import arcade


class Rocket (arcade.Sprite):
    def __init__(self,x,y,c,game):
        super().__init__()
        self.center_x=x
        self.center_y=y
        self.width=15
        self.height=70
        self.color = c
        self.change_x=0
        self.change_y=0
        self.speed = 3.5
        self.score=0
        self.game= game
        self.hit = False
        self.hit_sound = arcade.load_sound(":resources:sounds/error2.wav")
        self.lose_sound = arcade.load_sound(":resources:sounds/lose1.wav")
    def draw(self):
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.width,self.height,self.color)

    def move(self,ball):
        
        self.center_y += self.change_y*self.speed
        if ball.center_x > self.game.width//2 and ball.change_x == 1:
            
            if ball.center_y>self.center_y:
                self.change_y = 1
            elif ball.center_y < self.center_y :
                self.change_y = -1
        else:
            self.change_y = 0     
        #if  self.center_y+self.speed < self.game_height-self.height   and      self.center_y-self.speed > self.height: it's not worrk

        if self.top > self.game.height-self.height//2:
            self.top = self.game.height-self.height//2
        if self.bottom <self.height//2:
            self.bottom = self.height//2
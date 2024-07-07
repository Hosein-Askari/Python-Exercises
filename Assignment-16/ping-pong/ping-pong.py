import arcade
from ball import Ball
from rocket import Rocket





class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=1280, height=720 , title="Ping-Pong")
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)
        self.ball = Ball(self)
        self.player1=Rocket(50,self.height//2,arcade.color.BLUE_GRAY,self)
        self.player2=Rocket(self.width-50,self.height//2,arcade.color.DARK_RED,self)
        
    
    def on_draw(self):
        arcade.start_render()
        
        arcade.draw_rectangle_outline(self.width//2,self.height//2,self.width-30,self.height-30,arcade.color.YELLOW_GREEN,15)
        arcade.draw_line(self.width//2,20,self.width//2,self.height-20,arcade.color.YELLOW_GREEN,15)

        self.player1.draw()
        self.player2.draw()
        self.ball.draw()

        

        arcade.draw_text(str(self.player1.score)+"     "+str(self.player2.score),self.width//2-80,self.height-100, 
                            arcade.color.OLD_ROSE,50)
        





    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.player1.height < y < self.height-self.player1.height:
            self.player1.center_y = y




    def on_update(self, delta_time: float):
        self.ball.move()
        self.player2.move(self.ball)
        if   arcade.check_for_collision(self.player1,self.ball) and self.player1.hit==False:
            self.player1.hit = True
            self.player2.hit = False
            self.ball.change_x  *= -1
            arcade.play_sound(self.player1.hit_sound)

        if arcade.check_for_collision(self.player2,self.ball) and self.player2.hit==False :
            self.player2.hit = True
            self.player1.hit = False
            self.ball.change_x  *= -1
            arcade.play_sound(self.player2.hit_sound)
       
        if self.ball.right > self.width :
            self.player1.score += 1
            self.player1.hit = False
            del self.ball
            self.ball = Ball(self)
            arcade.play_sound(self.player1.lose_sound)

        if self.ball.left < 0 :
            self.player2.score += 1
            self.player2.hit = False
            del self.ball
            self.ball = Ball(self)
            arcade.play_sound(self.player1.lose_sound)
        
game=Game()
arcade.run()
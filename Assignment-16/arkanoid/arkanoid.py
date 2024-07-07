import arcade
import arcade.color
from paddle import Paddle
from bricks import Brick
from ball import Ball

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=770,height=550)
        
        # self.width  = 1200
        # self.height = 800
        self.background = arcade.load_texture(":resources:images/backgrounds/abstract_2.jpg")
        self.paddle=Paddle(self)
        self.ball = Ball(self)
        self.setup = False
        self.brick_list = []
        self.game_over=False
        self.game_over_sound = arcade.load_sound(":resources:sounds/gameover1.wav")
        self.game_over_sound_flag =False

    def on_draw(self):
        arcade.start_render()
        if self.game_over==False:    
            arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.background)
            
            arcade.draw_text(str(self.paddle.score),self.width-70,40, arcade.color.RED_DEVIL,30)
            for brick in self.brick_list:
                brick.draw()
            
            for i in range (1,self.paddle.health+1):
                arcade.draw_texture_rectangle(i*50,10,80,50,self.paddle.health_png)
            

            self.ball.draw()
            self.paddle.draw()



        else:
            arcade.set_background_color(arcade.color.BLACK)
            arcade.draw_text("GAME OVER",self.width//2-200,self.height//2, arcade.color.RED_DEVIL,50)




    def on_update(self, delta_time: float):
        if self.game_over == False:
            if self.setup == False:
                x=0
                for i in range(1,71):
                    if 0<i<11 :
                        x += 1
                        y = 500
                        new_diwmond = Brick(x*70,y,1)
                    elif 10<i<21:
                        x -= 1
                        y = 460
                        if i == 11 :
                            x += 1
                        new_diwmond = Brick(x*70,y,2)
                    elif 20<i<31 :
                        x += 1
                        y = 420
                        if i==21:
                            x -= 1
                        new_diwmond = Brick(x*70,y,3)
                    elif 30<i<41:
                        x -= 1
                        y = 380
                        if  i == 31 :
                            x += 1
                        new_diwmond = Brick(x*70,y,4)
                    elif 40<i<51:
                        x += 1
                        y = 340
                        if i == 41:
                            x -=1
                        new_diwmond = Brick(x*70,y,5)
                    elif 50<i<61:
                        x -= 1
                        y = 300
                        if i ==51:
                            x += 1
                        new_diwmond = Brick(x*70,y,6)
                    elif 60<i<71:
                        x += 1
                        y = 260
                        if i ==61:
                            x -= 1
                        new_diwmond = Brick(x*70,y,7)
                    self.brick_list.append(new_diwmond)
                self.setup = True

            for brick in self.brick_list:
                if arcade.check_for_collision(self.ball,brick)  :
                    self.brick_list.remove(brick)
                    self.ball.change_y *= -1
                    self.paddle.score += 10
                    self.paddle.hit = False
                    arcade.play_sound(self.paddle.hit_sound1)

            if self.paddle.hit == False:
                if arcade.check_for_collision(self.ball,self.paddle):
                    self.ball.change_y *= -1
                    self.paddle.hit = True
                    arcade.play_sound(self.paddle.hit_sound2)

            if self.ball.bottom < 0:
                self.paddle.health -= 1
                del self.ball
                self.ball = Ball(self)
                self.paddle.hit = False
                arcade.play_sound(self.paddle.lose_sound)

            if self.ball.top > self.height or self.ball.right>self.width or self.ball.left<0:
                self.paddle.hit=False
            
            if self.paddle.health == 0:
                self.game_over = True

            if self.game_over:
                if self.game_over_sound_flag == False:
                    arcade.play_sound(self.game_over_sound)
                    self.game_over_sound_flag = True
            self.ball.move()
            self.paddle.move()






    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.paddle.center_x =x

    




    def on_key_press(self, symbol: int, modifiers: int):
        match symbol:
            case arcade.key.RIGHT:
                self.paddle.change_x = 1
            case arcade.key.LEFT : 
                self.paddle.change_x = -1
    





    def on_key_release(self, symbol: int, modifiers: int):
        match symbol:
            case arcade.key.RIGHT:
                self.paddle.change_x = 0
            case arcade.key.LEFT : 
                self.paddle.change_x = 0






game = Game()
arcade.run()
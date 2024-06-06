
import random
import time
import arcade
from apple import Apple
from snake import Snake
from pear import Pear
from shi import Shi
class Game(arcade.Window):
    def __init__(self):
        super().__init__(width = 800,  height = 600, title ="snake_game")

        arcade.set_background_color(arcade.color.KHAKI)
        self.apple = Apple(self)
        self.snake = Snake(self)
        self.pear= Pear(self)
        self.shi = Shi(self)
        self.choice = 1
        self.start_game =False
        self.game_over =False
        self.time = 0
        self.Game_over_sound=arcade.load_sound(":resources:sounds/gameover1.wav")
        self.flag_sound=False
    def on_draw(self):
        arcade.start_render()

        if self.game_over :
            arcade.set_background_color(arcade.color.BLACK)
            arcade.draw_text(" GAME OVER ",self.width//2-200,self.height//2, 
                            arcade.color.RED_DEVIL,50)
            if self.flag_sound==False:
                arcade.play_sound(self.Game_over_sound)
                self.flag_sound = True
        else:
            self.apple.draw()
            self.snake.draw()
            self.pear.draw()
            self.shi.draw()
            for part in self.snake.body:
                if self.snake.body.index(part) % 2 ==0 :
                    color =arcade.color.YELLOW
                    
                else :
                    color =arcade.color.GREEN
                
                arcade.draw_circle_filled(part[0],part[1],10,color)
            arcade.draw_text("Score : "+str(self.snake.screen_Score),self.width-190,5, 
                            arcade.color.RED_DEVIL,30) 
            arcade.draw_text("Pc Mode",5,self.height-20, 
                            arcade.color.RED_DEVIL,10) 


    def on_update(self, delta_time: float):
        if self.game_over == False:
            self.snake.speed =1
            if arcade.check_for_collision(self.snake,self.apple):
                self.snake.eat(self.apple,1)
                self.apple =Apple(self)
                self.choice = random.randint(1,2)
            if arcade.check_for_collision(self.snake,self.pear):
                self.snake.eat(self.pear,2)
                self.pear =Pear(self)
                self.choice = random.randint(1,2)
            if arcade.check_for_collision(self.snake,self.shi):
                self.snake.eat(self.shi,-1)
                self.shi = Shi(self)
            if arcade.check_for_collision(self.apple,self.shi) or arcade.check_for_collision(self.pear,self.shi) :
                self.shi = Shi(self)
            if arcade.check_for_collision(self.apple,self.pear) :
                self.apple = Apple(self)
            
            self.snake.body.append([self.snake.center_x,self.snake.center_y])
            if self.snake.score < len(self.snake.body):
                self.snake.body.pop(0)

            for part in self.snake.body :
                if  self.snake.body.index(part) != len (self.snake.body)-1:
                    if self.snake.center_x == part[0] and self.snake.center_y == part [1]:
                        self.game_over = True

            match self.choice :
                case 1 :
                    if self.snake.center_x > self.apple.center_x:
                        if self.snake.change_x != 1:
                            self.snake.change_x = -1
                            self.snake.change_y = 0
                        elif self.snake.change_x == 1:
                            self.snake.change_x = 0
                            self.snake.change_y = 20

                    if self.snake.center_x < self.apple.center_x:
                        if self.snake.change_x !=-1:    
                            self.snake.change_x = 1
                            self.snake.change_y = 0
                        else:
                            self.snake.change_x = 0
                            self.snake.change_y = 20

                    if self.snake.center_y > self.apple.center_y:
                        if self.snake.change_y != 1:
                            self.snake.change_y = -1
                            self.snake.change_x = 0
                        else :
                            self.snake.change_y = 0
                            self.snake.change_x = 20
                    if self.snake.center_y < self.apple.center_y:
                        if self.snake.change_y != -1:
                            self.snake.change_y = 1
                            self.snake.change_x = 0
                        else :
                            self.snake.change_y = 0
                            self.snake.change_x = 20
                case 2:
                    if self.snake.center_x > self.pear.center_x:
                        if self.snake.change_x != 1:
                            self.snake.change_x = -1
                            self.snake.change_y = 0
                        elif self.snake.change_x == 1:
                            self.snake.change_x = 0
                            self.snake.change_y = 20

                    if self.snake.center_x < self.pear.center_x:
                        if self.snake.change_x !=-1:    
                            self.snake.change_x = 1
                            self.snake.change_y = 0
                        else:
                            self.snake.change_x = 0
                            self.snake.change_y = 20

                    if self.snake.center_y > self.pear.center_y:
                        if self.snake.change_y != 1:
                            self.snake.change_y = -1
                            self.snake.change_x = 0
                        else :
                            self.snake.change_y = 0
                            self.snake.change_x = 20
                    if self.snake.center_y < self.pear.center_y:
                        if self.snake.change_y != -1:
                            self.snake.change_y = 1
                            self.snake.change_x = 0
                        else :
                            self.snake.change_y = 0
                            self.snake.change_x = 20

            self.snake.move()
        

        if self.snake.screen_Score>0 or self.snake.screen_Score<0:
            self.start_game =True

        if self.start_game :
            if self.snake.screen_Score == 0 or self.snake.screen_Score == -1:
                self.game_over =True

        if self.snake.right > self.width or self.snake.left < 0 or self.snake.top > self.height or self.snake.bottom < 0:
            self.game_over =True
            

        if self.game_over == False:
            self.time = time.time()

        if self.game_over :
            if time.time()- self.time >3:
                exit(0)

game =Game()
arcade.run()
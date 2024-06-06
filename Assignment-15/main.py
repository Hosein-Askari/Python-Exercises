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
        self.game_over =False
        self.start_game =False
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
                    color =arcade.color.GRAPE
                
                arcade.draw_circle_filled(part[0],part[1],15,color)

            arcade.draw_text("Score : "+str(self.snake.screen_Score),self.width-190,5, 
                            arcade.color.RED_DEVIL,30) 
            arcade.draw_text("Player Mode",5,self.height-20, 
                            arcade.color.RED_DEVIL,10) 
    def on_update(self, delta_time: float):
        
        if self.game_over==False:
            self.snake.speed =4
            self.snake.move()
            
            if arcade.check_for_collision(self.snake,self.apple):
                self.snake.eat(self.apple,1)
                self.apple =Apple(self)
            if arcade.check_for_collision(self.snake,self.pear):
                self.snake.eat(self.apple,2)
                self.pear =Pear(self)
            if arcade.check_for_collision(self.snake,self.shi):
                self.snake.eat(self.apple,-1)
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
    def on_key_release(self, symbol: int, modifiers: int):
        match symbol:
            case arcade.key.UP :
                if self.snake.change_y != -1 :
                    self.snake.change_y = 1
                    self.snake.change_x = 0
            case arcade.key.DOWN :
                if self.snake.change_y != 1 :
                    self.snake.change_y = -1
                    self.snake.change_x = 0
            case arcade.key.RIGHT :
                if self.snake.change_x != -1 :
                    self.snake.change_x = 1
                    self.snake.change_y = 0
            case arcade.key.LEFT :
                if self.snake.change_x != 1 :
                    self.snake.change_x = -1
                    self.snake.change_y = 0


game =Game()
arcade.run()
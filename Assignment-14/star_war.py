import time
import arcade
import arcade.key
import arcade.key
import arcade.key
from spaceship import Space_ship
from enemy import Enemy







class Main_Game(arcade.Window):
    def __init__(self):
        super().__init__(width=1280,height=960,title="STAR WARAS")
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me = Space_ship(self)
        self.enemies=[]
        self.speed =0
        self.Game_over_sound=arcade.load_sound(":resources:sounds/gameover1.wav")
        self.flag_sound=False
    def on_draw(self):
        arcade.start_render()
        if self.me.health==0:
            arcade.set_background_color(arcade.color.BLACK)
            arcade.draw_text(" GAME OVER ",self.width//2-200,self.height//2, 
                         arcade.color.RED_DEVIL,50)
            if self.flag_sound==False:
                arcade.play_sound(self.Game_over_sound)
                self.flag_sound = True
            
        elif self.me.health>0:
            
            arcade.set_background_color(arcade.color.SKY_BLUE)
            arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.background)
            for i in range(self.me.health):
                arcade.draw_lrwh_rectangle_textured(i*40,0,40,40,self.me.health_png)
            self.me.draw()
            for enemy in self.enemies:
                enemy.draw()
            for bullet in self.me.bullets:
                bullet.draw()
            arcade.draw_text("Score : "+str(self.me.score),self.width-190,5, 
                            arcade.color.RED_DEVIL,30) 
        
         
        
        elif self.me.health ==-1 :
            exit(0)

    def on_update(self, delta_time):
        
        
        self.me.move()
        
        if (len(self.enemies)>0):
            if  (time.time() - self.enemies[-1].creation_time) >=3 :
                new_enemy = Enemy(self)
                new_enemy.speed += self.speed
                self.enemies.append(new_enemy)
        else:
            new_enemy = Enemy(self)
            self.enemies.append(new_enemy)
        self.speed += 0.0005
        
            
        

        for bullet in self.me.bullets:
            bullet.move()
        
        
        for enemy in self.enemies:
            enemy.move()
            
            
            if arcade.check_for_collision(self.me,enemy):
                self.enemies.remove(enemy)
                arcade.play_sound(self.me.hurt_sound)
                self.me.health -= 1
            if enemy.center_y <0 :
                self.enemies.remove(enemy)
                arcade.play_sound(self.me.hurt_sound)
                self.me.health -= 1
                
            for bullet in self.me.bullets:
                if arcade.check_for_collision(enemy,bullet):
                    self.enemies.remove(enemy)
                    self.me.bullets.remove(bullet)
                    arcade.play_sound(self.me.hit_enemy_sound)
                    self.me.score += 1
                if bullet.center_y > self.height:
                    self.me.bullets.remove(bullet)
            
    def on_key_press(self, symbol, modifiers):
        match symbol:
            case arcade.key.RIGHT:
                self.me.change_x = 1
                self.me.change_y = 0
            case arcade.key.LEFT:
                self.me.change_x = -1
                self.me.change_y = 0
            case arcade.key.UP :
                self.me.change_y = 1
                self.me.change_x = 0
            case arcade.key.DOWN :
                self.me.change_y = -1
                self.me.change_x = 0
            case arcade.key.SPACE:
                self.me.fire()
    def on_key_release(self, symbol, modifiers):
        if (symbol == arcade.key.UP or symbol == arcade.key.DOWN 
        or symbol == arcade.key.RIGHT or symbol == arcade.key.LEFT) :
            self.me.change_y = 0
            self.me.change_x = 0
    
game = Main_Game()
arcade.run()
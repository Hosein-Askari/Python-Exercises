
import random
import arcade
from spaceship import Space_ship
from enemy import Enemy







class Main_Game(arcade.Window):
    def __init__(self):
        super().__init__(width=1280,height=960,title="STAR WARAS")
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me = Space_ship()
        self.enemy = Enemy(self)
      
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.background)
        self.me.draw()
        self.enemy.draw()
    
    def on_update(self, delta_time):
        self.me.center_x += self.me.speed
        self.enemy.center_y -= self.enemy.speed

    def on_key_press(self, symbol, modifiers):
        match symbol:
            case arcade.key.RIGHT:
                self.me.speed = 4
            case arcade.key.LEFT:
                self.me.speed = -4

    def on_key_release(self, symbol, modifiers):
        match symbol:
            case arcade.key.RIGHT:
                    self.me.speed=0
            case arcade.key.LEFT:
                    self.me.speed=0
        
game = Main_Game()
arcade.run()
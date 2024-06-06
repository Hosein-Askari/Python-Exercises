import random
import arcade

class Apple(arcade.Sprite):
    def __init__(self,game):
        super().__init__("Assignment-15/apple.png")

        self.center_x = random.randint(15,game.width//2-15)
        self.center_y = random.randint(15,game.height//2 - 15)
        self.width = 90
        self.height = 50




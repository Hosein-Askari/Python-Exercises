import arcade


class Space_ship(arcade.Sprite):
    def __init__(self):
        super().__init__(":resources:images/space_shooter/playerShip3_orange.png")
        self.center_x = 100
        self.center_y = 200
        self.speed=0
        self.height = 50
        self.width = 50
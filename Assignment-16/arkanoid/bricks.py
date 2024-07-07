import arcade

class Brick(arcade.Sprite):
    def __init__(self,cx,cy,c) :
        super().__init__()    
        self.width = 30
        self.height = 30
        self.center_x = cx
        self.center_y = cy
        self.texture1 = arcade.load_texture("Assignment-16/arkanoid/images/bricks 1.png")
        self.texture2 = arcade.load_texture("Assignment-16/arkanoid/images/bricks 2.png")
        self.texture3 = arcade.load_texture("Assignment-16/arkanoid/images/bricks 3.png")
        self.texture4 = arcade.load_texture("Assignment-16/arkanoid/images/bricks 4.png")
        self.texture5 = arcade.load_texture("Assignment-16/arkanoid/images/bricks 5.png")
        self.texture6 = arcade.load_texture("Assignment-16/arkanoid/images/bricks 6.png")
        self.texture7 = arcade.load_texture("Assignment-16/arkanoid/images/bricks 7.png")
        self.colors = c
            


    def draw(self):
        match self.colors :
            case 1 :
                arcade.draw_scaled_texture_rectangle(self.center_x,self.center_y, self.texture1,.9)
            case 2 :
                arcade.draw_scaled_texture_rectangle(self.center_x,self.center_y, self.texture2,.9)
            case 3 :
                arcade.draw_scaled_texture_rectangle(self.center_x,self.center_y, self.texture3,.9)
            case 4 :
                arcade.draw_scaled_texture_rectangle(self.center_x,self.center_y, self.texture4,.9)
            case 5 :
                arcade.draw_scaled_texture_rectangle(self.center_x,self.center_y, self.texture5,.9)
            case 6 :
                arcade.draw_scaled_texture_rectangle(self.center_x,self.center_y, self.texture6,.9)
            case 7 :
                arcade.draw_scaled_texture_rectangle(self.center_x,self.center_y, self.texture7,.9)
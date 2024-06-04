import arcade

 

arcade.open_window(600, 600, "Draw nested loop")
 

arcade.set_background_color(arcade.color.WHITE)

x=80
y=530
name=""
arcade.start_render()
for i in range(10):
    for j in range(10):
            if (j %2 ==0):
                name="gemRed.png"
            else:
                name="gemBlue.png"
            texture = arcade.load_texture(":resources:images/items/"+name)
                
            arcade.draw_scaled_texture_rectangle(x, y, texture, 0.7, 0)
                
            x = x + 50
            
        
        
    y -= 50
    x=80

arcade.finish_render()
 

arcade.run()
import turtle
import time


turtle.bgcolor("white")
pos = 15.0
length=50
p=turtle.Pen()
p.shape(name="turtle")
for i in range (3,10):
    x= 180-(((i-2)*180)/i)
    y = 180-((((i-2)*180)/i)/2)
    
   
    for j in range (0,i):
        p.color("black")

        if(j==0):
            p.right(y)
        else:
            p.right(x)
        p.forward(length)
        
        time.sleep(1)

    p.left(360-(p.heading()))
    p.color("white")
    p.forward(pos)
    pos += 4
    length += 12
    
turtle.done()
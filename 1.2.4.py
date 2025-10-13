#-----import statements-----
import turtle
import random



#-----initialize turtle-----
turtle.colormode(255)
win = turtle.Screen()
spiral = turtle.Turtle()

#-----game configuration----
win.setup(600,600)      #sets the overall dimensions of the screen
#win.bgcolor(input("Pick any color you want"))  #background color of window
win.bgcolor(255, 0, 0)  #background color of window


spiral.pencolor(0, 0, 0)
walls=20
wall_length=20

#-----game functions--------
    #spiral
def makeSpiral():
    spiral.pensize(10)
    spiral.goto(0, 0)
    spiral.setheading(90)
    for i in range(walls):
        spiral.forward(wall_length)
        spiral.right(90)
        spiral.forward(wall_length)
        spiral.right(90)
        wall_length+=20
        


#-----events / function calls----------------
makeSpiral()

win.mainloop()
#-----import statements-----
import turtle
import random
#-----initialize turtle-----
turtle.colormode(255)
win=turtle.Screen()
spiral=turtle.Turtle()
spiral.pensize(5)
spiral.speed(0)
spiral.pencolor(0, 0, 0)
#-----game configuration----
win.setup(600,600)#sets the overall dimensions of the screen
#rwin.bgcolor(input("Pick any color you want"))  #background color of window 
win.bgcolor(255, 255, 255)  #background color of window
walls=20
path_width=20
#-----game functions--------
def makeSpiral():       #spiral
    global path_width
    wall_length=20
    spiral.goto(0, 0)
    spiral.setheading(90)
    for i in range(walls):
        spiral.forward(wall_length)
        spiral.left(90)
        spiral.forward(wall_length)
        spiral.left(90)
        wall_length+=path_width
def go():
    win.tracer(0)
    makeSpiral()
    win.update()
#-----events / function calls----------------
go()
win.mainloop()

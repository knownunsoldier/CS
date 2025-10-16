#-----import statements-----
import turtle
import random
#-----initialize turtle(s)-----
turtle.colormode(255)
win=turtle.Screen()
spiral=turtle.Turtle()
spiral.pensize(5)
spiral.speed(1)
spiral.pencolor(0, 0, 0)
#-----game configuration----
win.setup(600,600)                                  #sets the overall dimensions of the screen
win.bgcolor(255, 255, 255)                          #background color of window
#rwin.bgcolor(input("Pick any color you want"))     #background color of window 
walls=20
path_width=20
door_width=20
#-----game functions--------
def makeSpiral():                                   
    global path_width
    wall_length=60
    spiral.goto(0, 0)
    for i in range(walls):
        for l in range(2):
            spiral.left(90)
            spiral.forward(10)
            spiral.penup()
            spiral.forward(door_width)
            spiral.pendown()
            spiral.forward(40)

            spiral.right(90)
            spiral.forward(path_width)
            spiral.forward(-path_width)
            spiral.left(90)
            spiral.forward(wall_length-(door_width+50))
        wall_length+=path_width
def go():                                           
    makeSpiral()
    win.tracer(0)
    win.update()
#-----events / function calls----------------
go()
win.mainloop()

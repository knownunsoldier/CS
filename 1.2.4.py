#-----import statements-----
import turtle
import random
#-----initialize turtle(s)-----
turtle.colormode(255)
win=turtle.Screen()
spiral=turtle.Turtle()
spiral.pensize(5)
spiral.speed(0)
spiral.pencolor(0, 0, 0)
spiral.penup()
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
    global wall_length
    wall_length=70
    spiral.goto(0, 0)
    global i
    for i in range(walls):
        global l
        for l in range(2):
            if i==0 and l==0:
                spiral.penup()
            spiral.forward(40)
            spiral.left(90)
            makeDoor()

            #makeBarrier()
            spiral.pendown()
            spiral.right(90)
            spiral.forward(path_width)
            spiral.forward(-path_width)
            spiral.left(90)
            spiral.forward(wall_length-(door_width+50))
        wall_length+=path_width
def makeDoor():
    spiral.forward(10)
    spiral.penup()
    if i==0 and l==0:
        spiral.pendown()
    spiral.forward(door_width)
def go():
    makeSpiral()
    win.tracer(0)
    win.update()
#-----events / function calls----------------
go()
win.mainloop()

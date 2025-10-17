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
wall_length=70
#-----game functions--------
def makeSpiral():                                   
    global path_width
    global wall_length
    spiral.goto(40, 0)
    global i
    spiral.penup() 
    for i in range(walls):
        spiral.left(90) 
        whichfirst=random.randint(0, 1) 
        half = (wall_length-(door_width+(path_width*2)))/2
        distance_one = random.randint(0, int(half))
        distance_two = random.randint(0, int(half))
        spiral.forward(distance_one)
        if whichfirst==0:
            makeDoor() 
        else:
            makeBarrier()
        spiral.forward(distance_two)
        if whichfirst==0:
            makeBarrier() 
        else:
            makeDoor()
        spiral.forward(wall_length-(distance_one+distance_two))
        if i%2==1:
            wall_length+=path_width

def makeDoor():
    spiral.pendown()
    if i==0: #is it the first loop?
        spiral.penup()
    spiral.forward(10)
    spiral.penup()
    spiral.forward(door_width) #draw door section
    spiral.pendown()
def makeBarrier():
    if i>walls-5: 
        spiral.penup()
    spiral.right(90)
    spiral.forward(path_width)
    spiral.forward(-path_width)
    spiral.left(90)
    spiral.pendown()
def go():
    makeSpiral()
    win.tracer(0)
    win.update()
#-----events / function calls----------------
go()
win.mainloop()

#-----import statements-----
import turtle
import random
#-----initialize turtle(s)-----
turtle.colormode(255)
win=turtle.Screen()
spiral=turtle.Turtle()
spiral.pensize(5)
spiral.hideturtle()
spiral.speed(0)
spiral.pencolor(0, 0, 0)
rnr = turtle.Turtle()
rnr.shape("turtle")
rnr.color(0, 0, 255)
rnr.pencolor(0, 128, 128)
#-----game configuration----
win.setup(600,600)
win.bgcolor(255, 255, 255)
walls=30
path_width=20
door_width=20
wall_length=70
#-----game functions--------
def makeSpiral():
    global path_width
    global wall_length
    spiral.penup() 
    spiral.hideturtle()
    spiral.goto(40, 0)
    global i
    for i in range(walls): 
        '''i know this whole for loop looks like 
        insanity but i promise i can explain 
        it if you need me to'''
        spiral.left(90) 
        spiral.pendown()
        whichfirst=random.randint(0, 1) 
        distances = []
        for l in range(3):
            distances.append(random.randint(0, 10))
        x=sum(distances)
        distance_one = (distances[0]/x)*(wall_length - (door_width + (path_width * 2)))
        distance_two = distances[1]/x*(wall_length - (door_width + (path_width * 2)))
        distance_three = distances[2]/x*(wall_length - (door_width + (path_width * 2)))
        spiral.forward(distance_one)
        if whichfirst==0:
            makeDoor() 
            print("door first")
        else:
            makeBarrier()
            print("barrier first")
        spiral.forward(distance_two)
        if whichfirst==0:
            makeBarrier()
        else:
            makeDoor()
        spiral.forward(distance_three)
        if i%2==1:
            wall_length+=path_width
def makeDoor():
    spiral.pendown()
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
    win.tracer(0)
    makeSpiral()
    win.update()
    print("donesies!")
#-----events / function calls----------------
go()
win.mainloop()

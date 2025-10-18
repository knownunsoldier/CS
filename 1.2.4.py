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
rnr=turtle.Turtle()
rnr.speed(0)
rnr.penup()
rnr.shape("turtle")
rnr.color(0, 0, 255)
rnr.pencolor(0, 128, 128)
rnr.pensize(4)
rnr.goto(-160, -160)
rnr.pendown()
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
            distances.append(random.randint(1, 10))
        x=sum(distances)
        distance_one = (distances[0]/x)*(wall_length - (door_width + (path_width * 2)))
        distance_two = distances[1]/x*(wall_length - (door_width + (path_width * 2)))
        distance_three = distances[2]/x*(wall_length - (door_width + (path_width * 2)))
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
        if i==walls-1:
            spiral.forward(distance_three-path_width)
            spiral.left(90)
            spiral.forward(path_width)
        else:
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
def up():
    print("going up")
    rnr.setheading(90)
    rnr.forward(5)
    win.update()
def down():
    print("going down")
    rnr.setheading(270)
    rnr.forward(5)
    win.update()
def right():
    print("going right")
    rnr.setheading(0)
    rnr.forward(5)
    win.update()
def left():
    print("going left")
    rnr.setheading(180)
    rnr.forward(5)
    win.update()
def all():
    win.tracer(0)
    makeSpiral()
    win.listen()
    win.update()
    print("donesies!")
#-----events / function calls----------------
all()
win.onkeypress(up, "Up")
win.onkeypress(down, "Down")
win.onkeypress(right, "Right")
win.onkeypress(left, "Left")
win.listen()
win.mainloop()

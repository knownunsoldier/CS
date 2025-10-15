#-----import statements-----
import turtle
import random



#-----initialize turtle-----
turtle.colormode(255)
win = turtle.Screen()
spiral = turtle.Turtle()
spiral.pensize(5)
spiral.speed(0)


#-----game configuration----
win.setup(600,600)      #sets the overall dimensions of the screen
#win.bgcolor(input("Pick any color you want"))  #background color of window
win.bgcolor(255, 255, 255)  #background color of window


spiral.pencolor(0, 0, 0)
walls=20
wall_length=20

#-----game functions--------
    #spiral
def makeSpiral():
    global wall_length
    spiral.goto(0, 0)
    spiral.setheading(90)
    for i in range(walls):
        spiral.forward(wall_length)
        spiral.right(90)
        spiral.forward(wall_length)
        spiral.right(90)
        wall_length+=20
        


#-----events / function calls----------------
win.tracer(0)
makeSpiral()
win.update()
win.mainloop()
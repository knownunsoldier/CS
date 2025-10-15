import turtle as trtl
wn = trtl.Screen()
turtle_list = []
color_list = ["red", "green", "blue", "black", "orange", "yellow"]
for i in range(len(color_list)):
    temp_turtle = trtl.Turtle()
    temp_turtle.pencolor(color_list[i])
    temp_turtle.pensize(10)
    temp_turtle.turtlesize(3)
    turtle_list.append(temp_turtle)
for i in range(len(turtle_list)):
    turtle_list[i].setheading(60*i)
    turtle_list[i].forward(500)
for i in range(len(turtle_list)):
    turtle_list[i].right(180)
    turtle_list[i].forward(250)
trtl.mainloop()
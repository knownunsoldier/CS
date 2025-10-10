#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.addshape(apple_image) # Make the screen aware of the new file

apple = trtl.Turtle()
apple.penup()
apple.left(90)  #image loads rotated 90 degrees clockwise
apple.speed(0)

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.sety(150)
  active_apple.shape(apple_image)


#-----function calls-----
draw_apple(apple)




wn.mainloop()
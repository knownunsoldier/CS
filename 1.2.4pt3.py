import turtle
import random
turtle.hideturtle()
numbers = []
for i in range(4):
    numbers.append(random.randint(1, 4))
print(numbers)
four=0
for i in range(len(numbers)):
    if numbers[i]==4:
        turtle.write("4", font=("Arial", 50, "normal"))
        four+=1
        break
if four==0:
    turtle.write("no 4", font=("Arial", 50, "normal"))
turtle.mainloop()
from turtle import Turtle,Screen
import random
timmy = Turtle()
screen = Screen()
screen.bgcolor("white")
timmy.speed("fastest")
def random_color():
    return (random.random(),random.random(),random.random())
timmy.speed(10)
side = 3
timmy.pensize(5)
for items in range (8):
    angle = (side-2)*180
    inter_angle = angle/side
    for order in range(side):
        timmy.pencolor(random_color())
        timmy.forward(100)
        timmy.right(180 - inter_angle)
    side += 1
screen.mainloop()


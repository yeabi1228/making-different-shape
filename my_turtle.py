
from turtle import Turtle,Screen
from random import choice
timmy = Turtle()
screen = Screen()
timmy.shape("turtle")
order = ["red","yellow","green","blue"]
timmy.pensize(50)
timmy.goto(-100,0)
for items in range (4):
    timmy.color(choice(order))
    timmy.forward(100)
    timmy.pencolor(choice(order))
    timmy.right(90)
    timmy.forward(100)
    timmy.left(90)
    timmy.forward(50)
    timmy.left(90)

screen.mainloop()

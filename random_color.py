from turtle import Turtle , Screen
import random
timmy = Turtle()
screen = Screen()
def random_color():
    return (random.random(),random.random(),random.random())
direction =[0,90,180,270]
timmy.speed("fastest")
for items in range (200):
    timmy.pencolor(random_color())
    timmy.forward(15)
    timmy.setheading(random.choice(direction))
screen.mainloop()

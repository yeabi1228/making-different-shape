from turtle import Turtle , Screen
import random
timmy = Turtle()
screen = Screen()
screen.bgcolor("#123456")
timmy.speed("fastest")
def random_color():
    return (random.random(),random.random(),random.random())


def draw_spirograph(size_of_gab,default_angle):
    number_circle = int(360/size_of_gab)
    timmy.setheading(default_angle)
    for circle in range(number_circle):
        timmy.pencolor(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading()+ size_of_gab)

draw_spirograph(15,45)
screen.mainloop()





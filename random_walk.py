from turtle import Turtle,Screen
import random
timmy = Turtle()
screen = Screen()
screen.bgcolor("white")
timmy.pensize(15)
timmy.speed("fastest")

def random_color():
     return (random.random(),random.random(),random.random())
direction = [0,90,180,270]
for _ in range (200):
     timmy.pencolor(random_color())
     timmy.forward(30)
     timmy.setheading(random.choice(direction))
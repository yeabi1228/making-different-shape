
import colorgram
import random
import turtle
timmy = turtle.Turtle()
turtle.colormode(255)
#rbg_color = []
#colors = colorgram.extract("image.jpg",30)
colors = [ (202, 164, 164), (240, 245, 245), (236, 239, 239), (149, 75, 75), (222, 201, 201), (53, 93, 93), (170, 154, 154), (138, 31, 31), (134, 163, 163), (197, 92, 92), (47, 121, 121), (73, 43, 43), (145, 178, 178), (14, 98, 98), (232, 176, 176), (160, 142, 142), (54, 45, 45), (101, 75, 75), (183, 205, 205), (36, 60, 60), (19, 86, 86), (82, 148, 148), (147, 17, 17), (27, 68, 68), (12, 70, 70), (107, 127, 127), (176, 192, 192), (168, 99, 99)]
timmy.penup()
timmy.hideturtle()
timmy.setheading(210)
timmy.forward(300)
timmy.setheading(0)
timmy.speed("fastest")
for i in range(13):
    if  i%2 == 0:
        timmy.setheading(0)
    for _ in range(14):
        timmy.dot(20,random.choice(colors))
        timmy.forward(40)
    timmy.setheading(90)
    timmy.forward(35)
    timmy.setheading(180)


turtle.Screen().mainloop()



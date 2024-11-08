from turtle import Turtle ,Screen

timmy = Turtle()
timmy.color("yellow","blue")
timmy.setheading(180)
timmy.forward(200)
timmy.setheading(0)
timmy.speed("fastest")
timmy.begin_fill()
for i in range(50):
    timmy.forward(200)
    timmy.left(168.5)
timmy.end_fill()
timmy.penup()
timmy.forward(100)
timmy.pendown()
timmy.setheading(225)
timmy.setheading(0)
timmy.speed("fastest")
timmy.begin_fill()
for i in range(50):
    timmy.forward(200)
    timmy.left(168.5)
timmy.end_fill()

timmy.penup()

timmy.forward(100)
timmy.pendown()
timmy.setheading(225)
timmy.setheading(0)
timmy.speed("fastest")
timmy.begin_fill()
for i in range(50):
    timmy.forward(200)
    timmy.left(168.5)
timmy.end_fill()
Screen().mainloop()


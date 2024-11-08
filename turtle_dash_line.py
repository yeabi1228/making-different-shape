from turtle import Turtle,Screen
timmy = Turtle()
screen = Screen()
for items in range(4):
    for order in range(10):
        timmy.forward(8)
        timmy.penup()
        timmy.forward(8)
        timmy.pendown()
        timmy.forward(8)
    timmy.right(90)
screen.mainloop()
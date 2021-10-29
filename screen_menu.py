from turtle import Turtle

POSITIONS = [(-420, 300), (420, 300), (420, -295), (-420, -295), (-420, 300)]
MIDDLE_BORDER_POS = [(0, 310), (0, -310)]


class CreateScreen:
    def __init__(self):
        self.border = Turtle()
        self.border.color('white')
        self.border.hideturtle()
        self.border.speed('fastest')
        self.border.pensize(20)
        self.border.penup()
        for coordinates in POSITIONS:
            self.border.goto(coordinates)
            self.border.pendown()
        self.border.penup()
        self.border.pensize(5)
        self.border.goto(MIDDLE_BORDER_POS[0])
        self.border.setheading(270)
        while 320 > self.border.ycor() > -320:
            self.border.forward(10)
            self.border.penup()
            self.border.forward(10)
            self.border.pendown()


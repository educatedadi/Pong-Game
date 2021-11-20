from turtle import Turtle

POSITIONS = [(-420, 300), (420, 300), (420, -295), (-420, -295), (-420, 300)]
MIDDLE_BORDER_POS = [(0, 310), (0, -310)]
GAME_OVER_FONT = ('Chunq', 24, 'bold')


class CreateScreen(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.speed('fastest')
        self.pensize(20)
        self.penup()
        for coordinates in POSITIONS:
            self.goto(coordinates)
            self.pendown()
        self.penup()
        self.pensize(5)
        self.goto(MIDDLE_BORDER_POS[0])
        self.setheading(270)
        while 320 > self.ycor() > -320:
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()
        self.penup()

    def game_over(self):
        self.home()
        self.write('G A M E  O V E R !', False, align='center', font=GAME_OVER_FONT)


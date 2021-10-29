from turtle import Turtle

MOVE_DISTANCE = 30


class PlayerBat (Turtle):
    def __init__(self, coordinate_for_bat):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.speed(0)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(coordinate_for_bat)

    def move_up(self):
        y_position = self.ycor()
        if 230 > y_position:
            self.sety(y_position + MOVE_DISTANCE)

    def move_down(self):
        y_position = self.ycor()
        if y_position > -230:
            self.sety(y_position - MOVE_DISTANCE)

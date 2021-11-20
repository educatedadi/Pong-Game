
from turtle import Turtle
SCORE_FONT = ('Chunq', 72, 'bold')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, False, 'center', SCORE_FONT)
        self.goto(100, 200)
        self.write(self.r_score, False, 'center', SCORE_FONT)

    def l_increase(self):
        self.l_score += 1
        self.update()

    def r_increase(self):
        self.r_score += 1
        self.update()


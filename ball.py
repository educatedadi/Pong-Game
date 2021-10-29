from turtle import Turtle
from random import randint
import time

move_y_distance = randint(5, 10)
move_x_distance = randint(5, 10)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('green')
        self.penup()

    def start_moving(self):
        global move_y_distance, move_x_distance
        # self.left(randint(-45, 45))
        current_x = self.xcor()
        current_y = self.ycor()
        self.goto(current_x + move_x_distance, current_y + move_y_distance)
        time.sleep(0.07)

    def bounce(self):
        global move_y_distance
        move_y_distance = -move_y_distance



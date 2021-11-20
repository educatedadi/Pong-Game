from turtle import Turtle
from random import randint
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('green')
        self.penup()
        self.move_y_distance = randint(5, 10)
        self.move_x_distance = randint(5, 10)
        self.time_of_bounce = 0.09

    def start_moving(self):
        current_x = self.xcor()
        current_y = self.ycor()
        self.goto(current_x + self.move_x_distance, current_y + self.move_y_distance)
        time.sleep(self.time_of_bounce)

    def bounce(self):
        self.move_y_distance *= -1

    def hit_by_bat(self):
        self.move_x_distance *= -1
        self.time_of_bounce *= 0.9

    def reset_position(self):
        self.move_x_distance *= -1
        self.move_y_distance *= -1
        self.home()
        self.time_of_bounce = 0.09


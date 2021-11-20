from turtle import Screen
from player_bat import PlayerBat
from screen_menu import CreateScreen
from ball import Ball
from scoreboard import ScoreBoard

canvas = Screen()

canvas.setup(width=800, height=600)
canvas.bgcolor('black')
canvas.title('PONG')
canvas.listen()
canvas.tracer(0)

create_screen = CreateScreen()
right_side_bat = PlayerBat((350, 0))
left_side_bat = PlayerBat((-350, 0))
my_ball = Ball()
score = ScoreBoard()


def switch_off():
    global game_is_on
    game_is_on = False


game_is_on = True
while game_is_on:
    canvas.update()
    canvas.onkey(right_side_bat.move_up, 'Up')
    canvas.onkey(right_side_bat.move_down, 'Down')

    canvas.onkey(left_side_bat.move_up, 'w')
    canvas.onkey(left_side_bat.move_down, 's')

    my_ball.start_moving()

    if my_ball.ycor() > 290 or my_ball.ycor() < -290:
        my_ball.bounce()

    if my_ball.xcor() > 320 or my_ball.xcor() < -320:
        if my_ball.distance(right_side_bat) < 50 or my_ball.distance(left_side_bat) < 50:
            my_ball.hit_by_bat()

    # Detects if right side misses the ball
    if my_ball.xcor() > 400:
        my_ball.reset_position()
        score.l_increase()

    # Detects if left side misses the ball
    if my_ball.xcor() < -400:
        my_ball.reset_position()
        score.r_increase()

    canvas.onkey(switch_off, 'e')

# canvas.exitonclick()

from turtle import Screen, Turtle
from bricks import Bricks
from ball import Ball
from walls import Walls
from score import Score
import time
def move_right():
    new_x = paddle.xcor() + 35
    paddle.setx(new_x)

def move_left():
    new_x = paddle.xcor() - 35
    paddle.setx(new_x)

def reset_game():
    ball.x_move = 5
    ball.y_move = 5


# Instantiate classes
screen = Screen()
paddle = Turtle()
bricks = Bricks()
walls = Walls()
ball = Ball()
score = Score()

game_on = True

# Ball starting loc
ball.goto(0, -100)

# Score
score.score = 0

# Screen settings
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0, 1)

screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# Instantiate bricks
bricks.spawn_bricks()

# Paddle Settings
paddle.penup()
paddle.setposition(0, -250)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(1, 4)
paddle.speed(10)

while game_on:
    # time.sleep(.1)
    screen.update()
    ball.move()
    for brick in bricks.all_bricks:
        if ball.distance(brick.position()) < 10:
            brick.clear()
            brick.hideturtle()
            score.score += 10
            score.update_scoreboard()
            ball.bounce_y()
    if ball.xcor() == 350 or ball.xcor() == -280:
        ball.bounce_x()
    if ball.ycor() == 250:
        ball.bounce_y()
    if ball.distance(paddle) < 30:
        ball.bounce_y()
    if ball.ycor() == -250:
        ball.goto(0,-100)
        ball.x_move = 0
        ball.y_move = 0
        screen.onkey(reset_game, "space")

# Keep the window open
screen.mainloop()

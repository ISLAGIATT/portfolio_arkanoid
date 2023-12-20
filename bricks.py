import turtle
from turtle import Turtle
import random

COLORS = ["red", "green", "orange", "blue", "yellow", "purple"]

class Bricks(Turtle):
    def __init__(self):
        super().__init__()
        self.all_bricks = []

    def spawn_bricks(self):
        turtle.tracer(0)
        for row in range(6):
            for brick in range(10):
                new_brick = Turtle("square")
                new_brick.penup()
                new_brick.color(random.choice(COLORS))
                new_brick.shapesize(1, 3)
                new_brick.goto(-255 + (65 * brick), 180 - (30 * row))
                self.all_bricks.append(new_brick)

        turtle.update()
        turtle.tracer(1)




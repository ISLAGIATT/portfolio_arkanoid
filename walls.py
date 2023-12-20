from turtle import Turtle, Screen
class Walls(Turtle):
    def __init__(self):
        super().__init__()
        self.screen.tracer(0)
        self.hideturtle()
        self.goto(365, 250)
        self.color("white")
        self.pendown()
        self.goto(365, -250)
        self.penup()
        self.goto(-290, 250)
        self.pendown()
        self.goto(-290, -250)
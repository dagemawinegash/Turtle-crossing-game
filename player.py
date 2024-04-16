STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 15
FINISH_LINE_Y = 280
from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.setheading(90)
        self.setpos(STARTING_POSITION)
        self.shape("turtle")

    def move(self):
        self.goto(0, self.ycor() + MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)

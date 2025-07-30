from turtle import Turtle

MOVE_DISTANCE = 20
UPPER_BOUND = 250
LOWER_BOUND = -250

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        if self.ycor() + 50 < UPPER_BOUND:  # 50 = half of paddle height
            self.sety(self.ycor() + MOVE_DISTANCE)

    def down(self):
        if self.ycor() - 50 > LOWER_BOUND:
            self.sety(self.ycor() - MOVE_DISTANCE)

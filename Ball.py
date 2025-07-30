from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.x_move = 10
        self.y_move = 10
        self.movespeed = 0.068

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1
        self.movespeed *= 0.9

    def bounce_x(self):
        self.x_move *= -1
        self.movespeed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.movespeed = 0.068

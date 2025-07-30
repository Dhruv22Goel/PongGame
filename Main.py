from turtle import Screen, Turtle
from Paddle import Paddle
from Ball import Ball
from ScoreBoard import ScoreBoard
import time

# Setup screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("🏓 Pong Game")
screen.tracer(0)

# Draw center line
center_line = Turtle()
center_line.hideturtle()
center_line.color("gray")
center_line.penup()
center_line.goto(0, 300)
center_line.setheading(270)
for _ in range(30):
    center_line.pendown()
    center_line.forward(10)
    center_line.penup()
    center_line.forward(10)

# Paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Ball and Score
ball = Ball()
scoreboard = ScoreBoard()

# Controls
screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

# Game loop
game_on = True
while game_on:
    time.sleep(ball.movespeed)  # 60 FPS
    screen.update()
    ball.move()

    # Wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Paddle collision (and prevent getting stuck)
    if (340 < ball.xcor() < 360 and ball.distance(r_paddle) < 50) or \
       (-360 < ball.xcor() < -340 and ball.distance(l_paddle) < 50):
        ball.bounce_x()

    # Missed paddle
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()

screen.mainloop()

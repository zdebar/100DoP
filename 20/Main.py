from turtle import Screen
import time
from Snake import *
from Food import *
from Scoreboard import *


# Setting up game window

screen = Screen()
screen.setup(width=580, height=580)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) # stop updating screen in time loops


# Creating Snake Object

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Game Run

game_is_on = True
while game_is_on:
    screen.update() # update screen now
    time.sleep(0.1)
    snake.move()

    # Detect Collision with Food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.refresh()
        snake.extend()

    # Detect Collision with Wall
    if 280 < snake.head.xcor() or snake.head.xcor() < -280 or 280 < snake.head.ycor() or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detext Collision with Tail
    for segment in snake.segments[1:]:
        if snake.head.position() == segment.position():
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
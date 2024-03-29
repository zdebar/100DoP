from turtle import Screen, Turtle
import time


# Setting up game window

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) # stop updating screen in time loops


# Setting up snake body

segments = []
for i in range(3):
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.up()
    new_segment.goto(-20*i,0)
    segments.append(new_segment)


# Snake movement

game_is_on = True
while game_is_on:
    screen.update() # update screen now
    time.sleep(0.01)
    for seg in segments:
        seg.forward(1)



       



















screen.exitonclick()
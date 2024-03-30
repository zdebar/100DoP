from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.up()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        random_x = random.randrange(-280,280,20)
        random_y = random.randrange(-280,280,20)
        self.goto(random_x, random_y)

    def refresh(self):
        random_x = random.randrange(-280,280,20)
        random_y = random.randrange(-280,280,20)
        self.goto(random_x, random_y)
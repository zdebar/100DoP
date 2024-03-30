from turtle import Turtle
import time

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20  
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


# Setting up snake body

class Snake():

    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.up()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_coord = self.segments[seg_num-1].position()
            self.segments[seg_num].goto(new_coord)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN :
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP :
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT :
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT :
            self.head.setheading(RIGHT)



       




















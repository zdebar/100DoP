import turtle as t

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
starting_positions = [(0,0), (-20,0),(-40,0)]
screen.tracer(0)

segments = []

for position in starting_positions:
    new_segment = t.Turtle("square")
    new_segment.color("white")
    new_segment.up()  
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True

while game_is_on:
    screen.update()
    for seg in segments:
        seg.forward(20)
       



















screen.exitonclick()
import turtle as t
import random

colors = ("royal blue", "deep pink","thistle")
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

tim = t.Turtle()
tim.speed(0)

def draw_spirograph(circles):
    for i in range(circles):
        tim.color(random_color())
        tim.circle(100, None)
        tim.right(360/circles)


draw_spirograph(24)
screen = t.Screen()
screen.exitonclick()

# random direction, color, speed, thickness
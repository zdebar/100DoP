import colorgram
import turtle as t
import random

# rgb_colors = []
# colors = colorgram.extract("./18/image.jpg", 12)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

def draw_dot():
    tim.down()
    tim.dot(25, random.choice(colors))
    tim.up()
    tim.forward(50)

def move_back(number_of_dots):
    tim.backward(5*50)
    tim.left(90)
    tim.forward(50)
    tim.right(90)


def draw_array(number_of_dots):
    for j in range(number_of_dots+1):
        for i in range(number_of_dots+1):
            draw_dot()
        move_back(number_of_dots)

t.colormode(255)
colors = [(245, 243, 239), (246, 243, 244), (202, 164, 109), (240, 245, 242), (236, 239, 243), (153, 75, 49), (222, 201, 136), (53, 94, 124), (171, 153, 41), (136, 32, 21), (133, 163, 184), (197, 93, 73)]
tim = t.Turtle()
tim.speed(0)

draw_array(4)
screen = t.Screen()
screen.exitonclick()




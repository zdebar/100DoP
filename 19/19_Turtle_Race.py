import turtle as t
import random

# Setup
screen = t.Screen()
screen.setup(width=500,height=400)

colors = ['red', 'orange', 'yellow', 'blue', 'green', 'violet']
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ")
print(user_bet)

is_race_on = True
turtles = []
coord_y = -125

for color in colors:
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.up() 
    new_turtle.color(color)
    new_turtle.goto(-230,coord_y)
    coord_y += 50
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Vou've won! The {winning_color} turtle is the winner! ")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner! ")
            is_race_on = False
            continue


screen.exitonclick()
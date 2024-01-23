import random
import turtle
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle do you want to win the race? Enter colour: ")
colors = ["red", "green", "blue", "yellow", "violet", "orange", "indigo"]
y_positions = [-70, -40, -10, 20, 50, 80, 110]
all_turtles = []

for turtle_index in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won!!.The {winning_color} turtle is the winner")
            else:
                print(f"You Lost!! The {winning_color} turtle is the winner")
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)

screen.exitonclick()

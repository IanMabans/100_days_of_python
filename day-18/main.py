import random
import turtle as t

tim = t.Turtle()

# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("blue")
# timmy_the_turtle.forward(100)

# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)
#
# forward(100)
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#
# def draw_shape(num_side):
#     angle = 360 / num_side
#     for _ in range(num_side):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     draw_shape(shape_side_n)

########### Challenge 4 - Random Walk ########
t.colormode(255)


# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
#            "SeaGreen"]
def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# directions = [0, 90, 180, 270]
# tim.pensize(5)
tim.speed("fastest")


# for _ in range(200):
#     tim.color(random_colour())
#     # tim.forward(30)
#     # tim.setheading(random.choice(directions))
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_colour())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()

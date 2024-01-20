# import module
# import turtle
# from turtle import Screen
#
# # create a turtle
# timy = turtle.Turtle()
# print(timy)
# timy.shape("turtle")
# timy.color("coral")
# timy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Name", ["Mary", "Maggie", "Joy"])
table.add_column("Type", ["Ken", "Roy", "Ian"])
table.align = "l"
print(table)

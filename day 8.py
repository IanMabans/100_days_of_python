import math


def greet():
    print("Good morning")
    print("How do you do?")
    print("Isn't the weather lovely\n")


greet()


# # Function that allows input
def greet_with_name(name):
    print(f"Good morning {name}")
    print(f"How do you do {name}?\n")


greet_with_name("Ian")


# # Functions with more than one input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


greet_with("Bob", "Mombasa")


def paint_calc(height, width, cover):
    num_cans = (height * width) / cover
    round_up_cans = math.ceil(num_cans)
    print(f"You'll need {round_up_cans} cans of paint.")


test_h = int(input())
test_w = int(input())
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

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


test_h = int(input("Input height\n"))
test_w = int(input("Input width\n"))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


# Checking prime numbers
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("Its a prime number")
    else:
        print("Its a non-prime number")


n = int(input("Insert a prime number\n"))
prime_checker(number=n)

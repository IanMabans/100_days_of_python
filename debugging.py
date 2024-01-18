############DEBUGGING#####################
# Reproduce the Bug
from random import randint

dice_img = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_img[dice_num])


# Describe Problem
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()

# # Play Computer
year = int(input("What's your year of birth?"))
if 1980 <= year < 1994:
    print("You are a millennial.")
elif year >= 1994:
    print("You are a Gen Z.")

# # Fix the Errors
age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")

# #Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(f"pages = {pages}")
print(f"total words = {total_words}")
print(total_words)


# #Use a Debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])

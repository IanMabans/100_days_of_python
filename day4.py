import random
# random_integer = random.randint(100,10000)
# print(random_integer)

# pi = 3.142323

# random_float = random.random()
# print(random_float)

# random_no = random.randint(0,1)
# if random_no == 0:
#     print("Heads")
# else:
#     print("Tails")
    
# Treasure map
# line1 = ["", "", ""]
# line2 = ["", "", ""]
# line3 = ["", "", ""]
# treasure_map = [line1, line2, line3]

# print("Hiding your treasure! X marks the spot")
# position = input()

# if len(position) >= 2:
#     letter = position[0].lower()  # Assuming the letter is the first character, converting to lowercase for consistency
#     number_index = int(position[1]) - 1
    
#     abc = ["a", "b", "c"]
    
#     letter_index = abc.index(letter)
#     treasure_map[number_index][letter_index] = "X"

#     print(f"{line1}\n{line2}\n{line3}")
# else:
#     print("Input position is too short.")


# Rock paper scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock,paper,scissors]

user_input = int(input("What do you choose? 0 for rock and roll, 1 for paper and 2 for scissors.\n"))
if user_input >=3 or  user_input < 0:
    print("You typed an invalid number. You loose")  
print(game_images[user_input])
comp_choice = random.randint(0,2)
print ("Computer choice")

print(game_images[user_input])

if user_input == 0 and comp_choice ==2:
    print ("You win")

elif comp_choice >user_input:
    print("You loose")
elif comp_choice ==user_input:
    print ("You draw")
elif comp_choice ==0 and user_input ==2:
    print ("You lose")
elif user_input > comp_choice:
    print ("You win")

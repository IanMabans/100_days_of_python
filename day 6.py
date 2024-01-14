import random

from hangman_resources import word_list, stages, logo

# Functions

# def my_function():
#     print("Hello")
#     print("Bye")


# my_function()

display = []
lives = 6

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(logo)
# print(f"The solution is {chosen_word}")
for _ in range(len(chosen_word)):
    display += "_"
print(display)
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have already guessed {guess}")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You've guessed {guess} that's not in the word. You loose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You loose")
            print(f"The correct word was {chosen_word}")

    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win")
    print(stages[lives])

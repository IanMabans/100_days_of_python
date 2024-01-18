from random import randint

turns = 0


def set_difficulty():
    level = input("Choose a difficulty. Type easy or hard")
    if level == 'easy':
        return easy_level_turns
    else:
        return hard_level_turns


def check_answer(guess, answer, turns):
    """Check answer after guess, returns the number of turns remaining"""
    if guess > answer:
        print("Too high")
        return turns - 1

    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer is {answer}")


easy_level_turns = 10
hard_level_turns = 5


def game():
    print("Welcome to the Guessing Game!")
    print("I am thinking of a number between 1 and 100")
    answer = randint(1, 100)

    print(f"haha the answer is {answer}")
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        guess = int(input("Make a number guess: "))

        print(f"You have {turns} attempts left ")
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You lose ")
            return


game()

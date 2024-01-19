import random

from art import logo, vs
from game_data import data


# Format the account data into printable form
def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}  from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower count and returns if the user is right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


score = 0
game_continue = True
while game_continue:

    # display art
    print(logo)
    # Generate a random account from the game data
    account_a = random.choice(data)
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask the user for a guess
    guess = input("Who has more followers? A or B : ").lower()

    # Check if user is correct
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Get follower count for each and check if the user is correct
    # Give user the feedback on their guess
    if is_correct:
        score += 1
        print(f"You are correct!! Current score is {score}")
    else:

        print(f"You are wrong. Final score is {score}")
        game_continue = False



# Making the accounts at B be at position A

# clear the screen

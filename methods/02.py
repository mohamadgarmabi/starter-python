import random
from typing import Literal

max_number = 20
counter_guess: int = 0

computer_number = random.randint(1, max_number)
print(computer_number)

def check_win(user_number: int, computer_number: int) -> bool:
    """Check if the user number is equal to the computer number.

    Args:
        user_number (int): The user's guess.
        computer_number (int): The computer's number.

    Returns:
        bool: True if the user's number matches the computer's, False otherwise.
    """
    global counter_guess ## global variable to count the number of guesses
    counter_guess = counter_guess + 1

    if user_number > max_number:
        print("You are out of range!")
        return False

    if user_number == computer_number:
        print(f"You win! in {counter_guess} guesses")
        return True
    elif user_number < computer_number:
        print("You are too low!")
        return False
    else:
        print("You are too high!")
        return False

def get_number_from_user() -> int:
    """Get and return a number input from the user."""
    return int(input("Enter a number between 1 and 20: "))

def user_status() -> dict[str, Literal["win", "lose"]]:
    """Get the user's status (win/lose) after a guess."""
    user_number = get_number_from_user()
    result = check_win(user_number, computer_number)
    return {
        "status": "win" if result == True else "lose"
    }

while user_status()['status'] == "lose":
    pass

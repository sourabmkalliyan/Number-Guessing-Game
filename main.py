from random import randint
EASY_TURNS = 10
HARD_TURNS = 5
# Function to check user's guess against actual answer

def check_answer(guess, answer, turn):
    if guess > answer:
        print("High")
        turn -= 1
        return turn
    elif guess < answer:
        print("Low")
        turn -= 1
        return turn
    else:
        print(f"You got it!!! The answer is {answer}")


# Make function to set difficulty

def set_difficulty():
    level = input("Choose a difficulty, Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_TURNS
    elif level == "hard":
        return HARD_TURNS

def game():
    # Choosing a randon number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1, 100)
    # print(f"Psst!! The actual answer is {answer}")



    # Let the user guess the number
    turns = set_difficulty()
    user_guess = 0
    while user_guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        user_guess = int(input("Make a Guess: "))
        turns = check_answer(user_guess, answer, turns)
        if turns == 0:
            print("You've ran out of guesses, You Lose")
            print(f"The actual answer is {answer}")
            return 0
        elif user_guess != answer:
            print("Guess Again")

# Track the number of turns and reduce by 1
# if they got wrong

# Repeat the guessing functionality if they got wrong


game()
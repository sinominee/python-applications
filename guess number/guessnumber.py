from random import randint
from art import logo

print(logo)

EASY_LEVEL_TURNS = 6
HARD_LEVEL_TURNS = 3

def check_answer(guess, answer, turns):
    ''' checks answer aginst guess. returns the number of turns remaining'''
    if guess > answer:
        print("Too High.")
        return turns - 1
    elif guess < answer:
        print("Too Low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")


def set_difficulty():
    level = input("Choose a difficulty.Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print('Welcome to the Number guessing Game! ')
    print('Im thinking of a number between 1 and 100. ')
    answer = randint(1, 100)
    print(f"psst, the correct answer is {answer}")

    turns = set_difficulty()
    
    guess = 0
    while guess != answer :
        print(f"you have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print(f"You have run out of gueeses. You lose.")
            return
        elif guess != answer:
            print('GUESS AGAIN')
game()





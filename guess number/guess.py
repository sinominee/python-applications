import random 
from art import logo

print(logo)
print('Welcome to the Number guessing Game! ')
print(' Im thinking of a number between 1 and 100 ')

diff_choice = input("Choose a difficulty. Type 'easy' or 'hard': ")


if diff_choice == "easy":
    chance = 10
    print(f"You have {chance} chance's ")
else:
    chance = 5
    print(f"You have {chance} chance's ")



def game():
    user_choice = int(input("choose the number betwenn 1 and 100: "))

    gen_number = random.randint(1, 100)
    should_cont = True

    while should_cont:        
        if user_choice == gen_number:
            print(f"Correct guess {user_choice} == {gen_number} ")
        else:
            chance -= 1
            print(f"Wrong choice Try Again ")
            print(chance)
            game()           
    if chance < 0:
        should_cont = False
        game()
game()



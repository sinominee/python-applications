import random

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

#Write your code below this line 👇
# Define constants
game_images = [rock, paper, scissors]

user_choice = int(
    input(
        "what is your pick? Type 0 for rock,1 for paper or 2 for scissor ? \n")
)

if user_choice >= 3 or user_choice < 0:
  print("Invalid choice, you lose")
else:
  print("user choice:")
  print(game_images[user_choice])

  computer_choice = random.randint(0, 2)
  print("computer choice:")
  print(game_images[computer_choice])
  if user_choice == computer_choice:
    print("It's a tie")
  elif user_choice == 0 and computer_choice == 2:
    print("You win!")
  elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
  elif computer_choice > user_choice:
    print("You lose")
  elif user_choice > computer_choice:
    print("you win!")
  # print(f"Computer's choice {computer_choice}")

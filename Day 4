# Day 4 Project: Rock Paper Scissors Bot

import random

Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper = '''
    _______
---'   ____)
      __________)
      ___________)
      __________)
---._________)
'''

Scissors = '''
    _______
---'   ____)
      __________)
      ___________)
      (____)
---.__(___)
'''

game_images = [Rock, Paper, Scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
while user_choice != 0 or user_choice != 1 or user_choice != 2:
    if user_choice == 0:
        print(game_images[0])
        break
    elif user_choice == 1:
        print(game_images[1])
        break
    elif user_choice == 2:
        print(game_images[2])
        break
    else:
        print("Invalid Choice, please select again.\n")
        user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

print("Bot's choice: ")
bot_choice = random.randint(0,2)
print(game_images[bot_choice])

if user_choice == bot_choice:
    print("It's a draw!")
elif (user_choice == 0 and bot_choice == 1) or (user_choice == 1 and bot_choice == 2) or \
    (user_choice == 2 and bot_choice == 0):
    print("You lose!")
else:
    print("You win!")

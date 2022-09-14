import random

# print(random.random()**random.randint(1,5))

#Randomly selects someone to pay for dinner
# names = input("Give me the names separated by ', ': ").split(", ")
# print(f"{names[random.randint(0,len(names)-1)]} will pay for dinner today!")

# #Burry your treasure on the map
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
#
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
#
# position = input("Where do you want to put the treasure? ")
#
# if position[0] == '1':
#     row1[int(position[1])-1] = 'X'
# elif position[0] == '2':
#     row2[int(position[1])-1] = 'X'
# elif position[0] == '3':
#     row3[int(position[1])-1] = 'X'
#
# map = [row1,row2,row3]
#
# Alternate Solution
# horizontal = int(position[0])
# vertical = int(position[1])
# map[vertical-1][horizontal-1] = "X"
#
# print(f"{row1}\n{row2}\n{row3}")

# Rock Paper Scissors Project

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
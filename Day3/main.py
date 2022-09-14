# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("Teen tickets are $7.")
#     else:
#         bill = 12
#         print("Adult tickets are $12.")
#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y":
#         bill += 3
#     print(f"Your final bill is ${bill}.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

#Love Calculator
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
#
# true_score = ((name1.lower().count("t"))+(name2.lower().count("t")))+((name1.lower().count("r"))
#               +(name2.lower().count("r")))+((name1.lower().count("u"))+(name2.lower().count("u")))\
#               +((name1.lower().count("e"))+(name2.lower().count("e")))
# love_score = ((name1.lower().count("l"))+(name2.lower().count("l")))+((name1.lower().count("o"))
#               +(name2.lower().count("o")))+((name1.lower().count("v"))+(name2.lower().count("v")))\
#               +((name1.lower().count("e"))+(name2.lower().count("e")))
# total_score = str(true_score)+str(love_score)
# if int(total_score) < 10 or int(total_score) > 90:
#     print(f"Your score is {total_score}, you go together like coke and mentos.")
# elif int(total_score) > 40 and int(total_score) < 50:
#     print(f"Your score is {total_score}, you are alright together.")
# else:
#     print(f"Your score is {total_score}.")

#---------------------------------------------------------------------------------------------------#
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')

print('''Welcome to Treasure Island!
Your goal is to make your way through a bunch of rooms
and drum roll please...
locate the treasure
shocker right?
anywhos good luck!\n''')


print('''You enter the dungeon and you\'re immediately faced with your first choice:
1. Pick the door on your left (type "left or Left")
2. Pick the door infront of you (type "middle or Middle")
3. Pick the door on your right (type "right or Right")\n''')

choice = input("Choice: ")
if choice.lower() == "middle" or choice.lower() == "right":
    print('''Yeesh, you were burned alive.
    What a toasty way to go!
    Better luck next time :)''')
else:
    print('''You stumble upon a gloomy looking lake.
    Do you:
    1. Swim across (type "swim or Swim")
    2. Wait for a boat (type "wait or Wait")\n''')
    choice = input("Choice: ")
    if choice.lower() == "swim":
        print('''That lake had the HYDRA!?
        You are beyond cursed.
        Better luck next time :)''')
    else:
        print('''You step into the final chamber where you spot three levers.
        Which one do you pull?
        1. The Red Lever (type "red" or "Red")
        2. The Yellow Lever (type "yellow" or "Yellow")
        3. The Blue Lever (type "blue" or "Blue")\n''')
        choice = input("Choice: ")
        if choice.lower() == "Blue" or choice.lower() == "Red":
            print('''DAMN! You got sheshkababed by some ogres.
            Better luck next time :)''')
        else:
            print('''Congratulations!
    You found the one piece!
    It was the friendships you made along your journey XD''')

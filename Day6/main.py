# Day 6 Project : Reeborg's World "Maze" Level Solutions

# Specific Solution
# def turn_right():
#     turn_left()
    #     turn_left()
#     turn_left()
#
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()


General Solution
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear() and not front_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

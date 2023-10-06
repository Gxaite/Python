'''
Jokempo game
'''
import random

player_choice = int(input("0 scissor, 1 = paper, 2 = rock: "))

pc_choice = random.randint(0,2)
print(pc_choice)

if player_choice == 0:
    if pc_choice == 0:
        print("Draw")
    elif pc_choice == 1:
        print("You win!!")
    else:
        print("You lose!")


if player_choice == 1:
    if pc_choice == 0:
        print("You lose!!")
    elif pc_choice == 1:
        print("Draw")
    else:
        print("You win!")

if player_choice == 2:
    if pc_choice == 0:
        print("You win")
    elif pc_choice == 1:
        print("|You lose!!")
    else:
        print("Draw!")

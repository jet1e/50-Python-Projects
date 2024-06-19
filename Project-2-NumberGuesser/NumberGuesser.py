# Random number guessing game
from random import randint

player = 0
computer = 0

def rand_num():
    return int(randint(1,10))

while True:
    try:
        print("Player: {}, Computer: {}".format(player, computer))
        com_choice = rand_num()
        # print (com_choice)
        choice = int(input("Choose a number from 1-10: "))
        if (choice<1) or (choice>10):
            print("Choice not in range")
        elif choice == com_choice:
            print("YOU WIN!")
            player += 1
        else:
            print("YOU LOSE!")
            computer += 1
    except ValueError:
        print("You must enter a integer")
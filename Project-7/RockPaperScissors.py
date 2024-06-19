# Rock paper scissors game
import random

choices = ["rock", "paper", "scissors"]

def computer_choice():
    return random.choice(choices)

def main():
    c_score = 0
    p_score = 0
    for i in range(3):
        round = i+1
        print(f"=== Round {round} ===")
        while True:
            choice = input("You choose... ")
            if choice.lower() in choices:
                break
            else:
                print("Incorrect selection, please try again.")

        c_choice = computer_choice()
        p_choice = choice.lower()
        print(f"Computer chooses... {c_choice}")

        if(p_choice == "rock") and (c_choice == "scissors"): # Winning conditions
            print(f"Rock beats Scissors, you win Round {round}")
            p_score += 1
        elif(p_choice == "paper") and (c_choice == "rock"):
            print(f"Paper beats Rock, you win Round {round}")
            p_score += 1
        elif(p_choice == "scissors") and (c_choice == "paper"):
            print(f"Scissors beats Paper, you win Round {round}")
            p_score += 1
        elif(p_choice == "rock") and (c_choice == "paper"): # Losing conditions
            print(f"Rock doesn't beat Paper, you lose Round {round}")
            c_score += 1
        elif(p_choice == "paper") and (c_choice == "scissors"):
            print(f"Paper doesn't beat Scissors, you lose Round {round}")
            c_score += 1
        elif(p_choice == "scissors") and (c_choice == "rock"):
            print(f"Scissors doesn't beat Rock, you lose Round {round}")
            c_score += 1
        elif p_choice == c_choice: # Draw condition
            print(f"You chose the same option! You drew Round {round}")
            p_score += 1
            c_score += 1
        
        print("\n=== Score ===")
        print(f"You: {p_score} | Computer: {c_score}")
        print("=============\n")

    if p_score > c_score:
        print("You win best of 3!")
    elif p_score < c_score:
        print("You lose best of 3!")
    else:
        print("Draw!")

main()
#Snake Eater Gun Game

import random


def solution(a, b):

    if a is b:
        return "Its a Draw."
    
    # Defining losing conditions for user
    winning_combinations = {
        (1, 0): "You win! Snake drinks Water.",
        (0, -1): "You win! Water sinks Gun.",
        (-1, 1): "You win! Gun kills Snake."
    }
    
    # Defining losing conditions for user
    losing_combinations = {
        (0, 1): "You lose! Snake drinks Water.",
        (-1, 0): "You lose! Water sinks Gun.",
        (1, -1): "You lose! Gun kills Snake."
    }
    
    # Determine result based on user and computer choices
    if (a, b) in winning_combinations:
        return winning_combinations[(a, b)]
    elif (a, b) in losing_combinations:
        return losing_combinations[(a, b)]

def game():
    print("-------------------------------")
    print("Welcome to Snake-Water-Gun game")
    print("-------------------------------")

    # Options for user to choose
    options = {1: "Snake", 0: "Water", -1: "Gun"}

    # creating an empty list to store results
    results =[]

    while True:

        try:
            # User choice
            ask_user = int(input(f"What you want to choose?:{options} "))

            if ask_user not in options:
                print("Please enter a valid input")
                continue
                
        except ValueError:
            print("Please enter a valid input 1, 0, -1")
            continue

        # Generating computer choice using random
        computer = random.randint(-1, 1)

        print(f"You chose {options[ask_user]} and computer chose {options[computer]}")

        #showing results to user
        print(solution(ask_user, computer))

        # Printing the result of the game
        result = solution(ask_user, computer)

        # storing all the result in results
        results.append(result)

        # asking user to play again
        play_again = input("You want to play again?(yes or no): ").strip().lower()


        if play_again != "yes":
            print("Thanks for playing! Results of the games played shown below: ", '\n')

            # creating a loop to show results using enumerate()

            for i, r in enumerate(results, start=1):
                print(f"Round {i}: {r}")

            break

game()
# Exercise B: Paper, scissors, rock
# Write a program that plays rock, paper, scissors.
# 1. Create a program that randomly prints 0, 1, or 2.
# 2. Expand the program so it randomly prints rock, paper, or scissors using if statements.
# 3. Add to the program so it first asks the user their choice.
# 4. Add conditional statement to figure out who wins – the player or the computer?
# 5. Add to the program so that it asks the user if they want to play again.

import random
import time

def paper_scissors_rock():
    playAgain = True
    while playAgain:
        number = random.randrange(3)
        hand = ["paper", "scissors", "rock"]
        userHand = False
        while userHand not in hand:
            userHand = input("Enter paper, scissors, or rock: ").lower()
            if userHand not in hand:
                print("'{}' is not a valid choice".format(userHand))
        print("You chose {}".format(userHand))
        time.sleep(1)
        print("The program chose {}".format(hand[number]))
        time.sleep(1)
        result = [userHand, hand[number]]
        if userHand == hand[number]:
            print("You both made the same choice, it's a draw")
        elif result == ["paper", "rock"] or result == ["scissors", "paper"] or result == ["rock", "scissors"]:
            print("Your {} beats the program's {}, you won!".format(userHand, hand[number]))
        else:
            print("The program's {} beats your {}, you lost".format(hand[number], userHand))
        time.sleep(1)
        replay = input("Do you want to play again? Y/N: ")
        if replay.upper() in ["Y", "YES"]:
            playAgain = True
        else:
            playAgain = False
            print("Thank you playing!")

paper_scissors_rock()

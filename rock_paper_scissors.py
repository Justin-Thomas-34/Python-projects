
"""
Python Rock-Paper-Scissors Game Project

This Python project is an interactive rock-paper-scissors game where users play against the computer. 
The user can input their choice of "rock," "paper," or "scissors," and the computer randomly selects its choice. 
The game then determines the winner based on the traditional rules of rock-paper-scissors. 
The game keeps track of the number of wins for both the user and the computer. 
The game continues until the user decides to quit by typing "Q".

Features:

Real-time user input for rock, paper, or scissors
Random computer choice
Immediate feedback on the outcome of each round
Score tracking for both the user and the computer
Option to quit the game at any time

This project is a fun way to practice Python programming concepts such as user input handling, 
conditionals, loops, and random number generation. 
Enjoy the classic game of rock-paper-scissors while honing your coding skills!

"""

import random

user_wins = 0
computer_wins = 0

options = ["rock","paper","scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        print("Invalid input, please try again.")
        continue

    random_number = random.randint(0,2)
    # rock: 0 , paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You win!")
        user_wins += 1
       
    elif user_input == "paper" and computer_pick == "rock":
        print("You win!")
        user_wins += 1
        
    elif user_input == "scissors" and computer_pick == "paper":
        print("You win!")
        user_wins += 1
    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times")
print("Computer won", computer_wins, "times")
print("Goodbye!")

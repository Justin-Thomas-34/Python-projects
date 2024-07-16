"""
Python Number Guessing Game Project

This Python project is an engaging number guessing game where users try to guess a randomly generated number within a specified range.
The user inputs an upper limit, and the program selects a random number between 0 and that limit. 
Users then guess the number, and the program provides feedback on whether the guess is too high or too low. 
The game continues until the user correctly guesses the number, and the total number of guesses is displayed at the end.

Features:

User-defined range for the random number
Input validation for both the range and guesses
Real-time feedback on guesses
Count of total guesses taken to find the correct number

This project is a great way to practice essential Python programming concepts such as user input handling, 
loops, conditionals, and random number generation. Test your guessing skills and have fun with this interactive game!

"""


import random

# Get the upper limit for the random number
top_of_range = input("Type a number: ")

# Check if the input is a digit
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0 :
        print("Please type a number larger than zero next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

# Generate a random number within the specified range
random_number = random.randint(0,top_of_range)
guesses = 0

# Main game loop
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
   
    # Check if the guess is a digit
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Please type a number next time.")
        continue

    # Compare the user's guess with the random number    
    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number")

print("You got it in", guesses, "guesses!")
        
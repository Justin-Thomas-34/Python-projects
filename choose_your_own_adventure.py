"""
Python Text Adventure Game Project

Welcome to the Python Text Adventure Game Project! 
In this interactive game, the user embarks on an adventure where they must make choices at various decision points. 
Each decision leads to different outcomes, including winning or losing the game.

Features:

Personalized user input with the player's name
Multiple choice-based decision points
Different paths and outcomes based on user decisions
Immediate feedback and conclusion of the game based on choices

This project is a fantastic way to practice Python programming concepts such as user input handling, 
conditionals, and basic control flow. Enjoy the adventure and see where your choices take you!

"""



name = input("Type your name: ")
print("Welcome",name,"to the adventure.")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across:  ").lower()

    if answer == "swim":
        print("You swim across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back? (cross/back) ").lower()

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you want to talk to them? (yes/no)").lower()
        if answer == "yes":
            print("You talk to the stranger and they give you gold. You WIN!")
        elif answer == "no":
            print("You ignored the stranger and they are offended. You lose.")
        else:
            print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")
else:
    print("Not a valid option. You lose.")

print("Thank you for trying", name)
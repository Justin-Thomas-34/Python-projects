# Quiz Game
'''
This Python project is a simple yet engaging quiz game where users answer a series of questions. 
The program will prompt the user with each question and evaluate their response. 
For every correct answer, the user's score increases. 
At the end of the quiz, the program will display the user's total score out of the number of questions asked, 
along with the percentage of correct answers. 
This project is a great way to practice fundamental programming concepts such as loops, 
conditionals, and user input handling in Python.

'''

print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

print(playing)

if playing.lower() != "yes":
  quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

answer = input("What does GPU stands for? ")
if answer.lower() == "graphics processing unit":
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

answer = input("What does PSU stands for? ")
if answer.lower() == "power supply":
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) *100) + "% .") 



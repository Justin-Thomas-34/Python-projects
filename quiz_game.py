# Quiz Game
'''
Welcome to the Python Quiz Game Project!
This interactive program allows users to test their knowledge on computer-related acronyms. 
The quiz consists of a series of questions where users must input the correct full forms of given abbreviations. 
The program will evaluate the answers and keep track of the score. 
At the end of the quiz, the total number of correct answers and the percentage score will be displayed.

Features:

Interactive user input
Real-time feedback on answers
Score tracking
Final score and percentage display
This project is an excellent way to practice basic Python programming concepts, 
including user input handling, conditional statements, and simple arithmetic operations. 
Dive in and enhance your Python skills while having fun with this quiz game!

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



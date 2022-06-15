# Write your solution below the starter code
# Follow the instructions in the tab to the right

import random

# Welcome the user to the game
print("Welcome to rock, paper, scissors. Good luck!")

print("Enter your choice")
# Make a choice for the computer player
user_choice = input("P, R, Scissors? ")

computer_choice = "Rock", "Paper", "Scissors"
com_choice = random.choice(computer_choice)

print(com_choice)
# Get a choice from the user
# Compare the user and computer choice
# Print the right message, based on the choices
#Rock smashes Scissors
#Paper covers Rock
#Scissors cuts Paper
if (user_choice == "Paper" and com_choice == "Rock"):
  print("Paper covers Rock. You win!")
elif (user_choice == "Rock" and com_choice == "Paper"):
  print("Paper covers Rock. You Lose!")
# else:
  # print("You draw")
    
if (user_choice == "Scissors" and com_choice == "Rock"):
  print("Rock smashes Scissors. You lose!")
elif (user_choice == "Rock" and com_choice == "Scissors"):
  print("Rock smashes scissors. You Win!")
if (user_choice == "Paper" and com_choice == "Scissors"):
  print("Scissors cut paper. You Lose!")
elif(user_choice == "Scissors" and com_choice == "Paper"):
  print("Scissors cut paper, You Win!")

if(user_choice == com_choice):
  print("Computer chose " + com_choice + " You draw!")


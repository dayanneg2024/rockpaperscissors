import random

while True:
    user_action = input ("enter a chice (rock, paper, scissors")
possible_actions = ["rock" , "paper" , "scissors"]
    computer_action = ramdom.choice(possible_actions)
print (f"Both players selected {user_action}, compter chose {computer_action}.\n")

if user_action == computer_action:
    print (f"Both players selected {user_action}. It's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print ("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose>")
elif user_action == "paper":
    if computer_action == "rock":
        print ("Paper covers rock! You win!")
    
        
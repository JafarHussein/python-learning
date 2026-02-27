# Building a simple rock, paper, scissors game
import random
print("                                     ")
print("**********************************")
print("Choose between Rock, Paper and scissors")
choices=['rock', 'paper', 'scissors']
player_choice=str(input("Choose from the provided Options: \n").lower())

while player_choice not in choices:
    print("Invalid Entry ❌")
    player_choice=str(input("Choose between rock, paper and scissors: \n").lower())

computer_choice=random.choice(choices)

if player_choice == 'rock':
    if computer_choice == 'scissors':
        print(f"player choice:{player_choice} vs computer choice:{computer_choice}")
        print("You win 🥳")
    elif computer_choice == 'paper':
        print(f"player choice:{player_choice} vs computer choice:{computer_choice}")
        print("You Lose 😭")
    else:
        print(f"player choice:{player_choice} vs computer choice:{computer_choice}")
        print("Its a draw 🤝")
elif player_choice == 'paper':
     if computer_choice == 'scissors':
        print(f"player choice:{player_choice} vs computer choice:{computer_choice}")
        print("You Lose 😭")
     elif computer_choice == 'rock':
         print(f"player choice:{player_choice} vs computer choice:{computer_choice}")
         print("You win 🥳")
     else:
         print(f"player choice:{player_choice} vs computer choice:{computer_choice}")
         print("Its a draw 🤝")

elif player_choice =='scissors':
    if computer_choice =='paper':
         print(f"player choice:{player_choice} vs computer choice:{computer_choice}")
         print("You win 🥳")
    elif computer_choice == 'rock':
        print(f"player choice:{player_choice} vs computer choice:{computer_choice}")
        print("You Lose 😭")
    else:
        print(f"player choice:{player_choice} vs computer choice:{computer_choice}")
        print("Its a draw 🤝")




         



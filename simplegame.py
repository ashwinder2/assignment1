            ##(ROCK,PAPER,SCISSORS) GAME
 
 #import the module
from random import randint
 
#create a list
list = ["Rock", "Paper", "Scissors"]
 
system = list[randint(0,2)]

#welcoming the user.
print('''
    **************************************
    Welcome to (ROCK,PAPER, SCISSORS) game
    **************************************

    Please select a menu option:

    
    1 - Play Game
    2 - Exit

    ''')
#user choice. 
choice= input("Enter your choice: ")

if choice == "2":
    print("Exiting the game...")
elif choice == "1":
 
#set player to False
    player = False
 
while player == False:
#set player to True
    print()
    print("Please select your option.")
    player = input("Rock, Paper, Scissors?\n")
    print()
    if player == system:
        print("Tie!")
    elif player == "Rock":
        if system == "Paper":
            print("You lose!", system, "covers", player)
        else:
            print("You win!", player, "smashes", system)
    elif player == "Paper":
        if system == "Scissors":
            print("You lose!", system, "cut", player)
        else:
            print("You win!", player, "covers", system)
    elif player == "Scissors":
        if system == "Rock":
            print("You lose...", system, "smashes", player)
        else:
            print("You win!", player, "cut", system)
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    system = list[randint(0,2)]
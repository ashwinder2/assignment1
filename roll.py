#PYTHON GAME - ROLLING THE DICE.
print("WELCOME") 
print("TO A SIMPLE  'ROLLING THE DICE' GAME IN PYTHON")

import random #Here we use random module for getting different numbers from the dice.
#Here we set two variables for highest and lowest value of the dice.
min = 1
max = 6

roll_again = "y"
#while loop is used , so that the user can roll the dice again. 
while roll_again == "y":
    print ("Rolling the dice")
    print ("The values are....")
#Randint accepts two parameters: a lowest and a highest value.
    print (random.randint(min,max))
    print (random.randint(min,max))

    roll_again =input("Roll the dices again?")







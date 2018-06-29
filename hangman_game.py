#HERE WE ARE GOING TO BUILD A SIMPLE GAME OF HANGMAN.


#importing the module.
import random
choice= None

list=["race","dhoom","heartbeat","hate","love","breakup","song"]
while choice != "0":
#welcoming the user.
    print('''
    ******************
    Welcome to Hangman
    ******************

    Please select a menu option:

    
    1 - Play Game
    2 - Exit

    ''')
#user choice. 
    choice= input("Enter your choice: ")

    if choice == "2":
        print("Exiting the game...")
    elif choice == "1":
#here we set the word.
        word = random.choice(list)
        word = word.upper()
        hidden_word = " _ " * len(word)
        turns = 6
        guessed = []
    

#create a while loop.
        while turns != 0 and hidden_word != word:
            print("The word is")
            print(hidden_word)
            print("There are", len(word), "letters in this word")
            print("the words you are guessed ")
            print(' '.join(guessed))
            print("\n You have", turns,"turns remaining")
            guess = input("\n Guess a letter: \n")
            guess = guess.upper()
            if len(guess) > 1:
                guess = input(" You can only guess one letter at a time!\n Try again: ")
                guess = guess.upper()
            while guess in guessed:
                print(" You have already guessed that letter!")
                guess = input("Please take another guess: ")
                guess = guess.upper()
            guessed.append(guess)
            if guess in word:
                print("Well done!", guess.upper(),"is in the word")
                word_so_far = ""
                for i in range (len(word)):
                    if guess == str(word[i]):
                        word_so_far += guess
                    else:
                        word_so_far += hidden_word[i]
                hidden_word = word_so_far
            else:
                print("Sorry, but", guess, "is not in the word")
                turns -= 1

        if turns == 0:
                print("GAME OVER! You have no turn left")
                print("You have failed to guess the word: ",word)
        else:
            print(" CONGRATULATIONS! You have guessed the word")
            print("The word was", word)
            print("Thank you for playing Hangman")

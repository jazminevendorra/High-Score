# Menu driven program that plays guess the word.
# Final Project
# Jazmin Even Dorra

# Import libraries
import random

def main():
    # Intro
    print("Can you guess the word?")

    # Initialize Quit constant
    QUIT = 4

    # Initialize control variable
    option = 0

    # Default High score
    playerName = input("\nPlayer name: ")
    highscore = 20
    highscore_file = open('highscore.txt', 'w')
    highscore_file.write("Jane Doe" + '\n')
    highscore_file.write("20")
    highscore_file.close()  

    # Menu
    while option != QUIT:

        #Display menu and prompt user for choice
        print("\n---------------------------------------------")
        print("| Choose one of the following options:      |")
        print("|\t1. Display Rules.                   |")
        print("|\t2. Play                             |")
        print("|\t3. Display High Score!              |")
        print("|\t4. Quit.                            |")
        print("---------------------------------------------")
        option = int(input("Option: "))

        if(option == 1):     #Display rules
            print("\nThe rules of the game are simple!")
            print("- Try to guess the word, using the hint and length of word")
            print("- You can try and play as many times as you want!")
            print("- Keep track of your highscore by choosing option 3 in the main menu")
            print("Thats it! Have fun!")

        elif(option == 2):   #Play game
            # Initialize variables
            score = 0
            tryAgain = 'y'                               
            
            while tryAgain == 'y':

                # topic sub-menu display
                print("\nPlease choose a topic")
                print("\t1. Food")
                print("\t2. Colors")
                print("\t3. Animals")
                topic = int(input("Choice: "))

                if topic == 1:      # Food topic
                    score = foodTopic(score)
                if topic == 2:      # Color Topic
                    score = colorTopic(score)
                if topic == 3:      # Animal Topic
                    score = animalTopic(score)

                # write highscore into high score file
                if score > highscore:
                    highscore_file = open('highscore.txt', 'w')
                    highscore_file.write(playerName+'\n')
                    highscore_file.write(str(score))
                    highscore_file.close()

            tryAgain = input("\nWould you like to keep playing (y/n)? ")
                
        elif(option == 3):   #Display High score
            highscore_file = open('highscore.txt','r')
            print("\nTHE HIGH SCORE IS: ")
            file_contents = highscore_file.read()
            highscore_file.close()
            print(file_contents)
            
        elif(option == 4):   # Quit
            print("\nHope to see you back soon",playerName+'!')
            print()

        else:                #Invalid option
            print("\nError ... Invalid option. Please Try Again.")

def foodTopic(playerScore):     # if player choice of topic is food
    #initialize variables
    tryAgain = 'y'
    decision = '1'

    #food list
    food = ['pasta','hamburger','rice']
   
    while tryAgain == 'y' and decision == '1':
        # randomly choose one of the foods
        index = random.randint(0,2)
        print("\nLength of word: ", "-"*len(food[index]))
        if index == 0:
            print("Hint: Most famous dish in Italy\n")
        elif index == 1:
            print("Hint: Most famous food in the United States\n")
        elif index == 2:
            print("Hint: Most famous food in Asia")
        
        guess = input("Guess: ")    # Ask for player guess

        if guess.lower() == food[index]:    # Correct answer
            print("\nCongratulations ... You guessed the Word!")
            playerScore = playerScore + 5
            print("\nScore: ",playerScore)
            print("\nWhat would you like to do next?")
            print("\t1. Try again in same category")
            print("\t2. Go to another category")
            decision =input("Choice: ")
    
        elif len(guess) > len(food[index]):     # Guess is too long
            print("\nThis word is too long. Please try again\n")
            tryAgain =input("Would you like to try again (y/n)? ")
            
        elif len(guess) < len(food[index]):     # Guess is too short
            print("\nThis word is too short. Please try again\n")
            tryAgain =input("Would you like to try again (y/n)? ")

        elif guess.lower() != food[index]:              # Guess is not the word
            print("\nThis is not the correct word\n")
            tryAgain =input("Would you like to try again (y/n)? ")
                 
    return playerScore

def colorTopic(playerScore):        #if player choice of topic is colors
    #initialize variables
    tryAgain = 'y'
    decision = '1'

    # Colors list
    colors = ['red','green','yellow']
   
    while tryAgain == 'y' and decision == '1':

        # Hints
        index = random.randint(0,2)
        print("\nLength of word: ", "-"*len(colors[index]))
        if index == 0:
            print("Hint: Color associated with passion\n")
        elif index == 1:
            print("Hint:  The color of most plants\n")
        elif index == 2:
            print("Hint: The color associated with the sun")
        
        guess = input("Guess: ")    # Ask for player guess

        if guess.lower() == colors[index]:    # Correct answer
            print("\nCongratulations ... You guessed the Word!\n")
            playerScore = playerScore + 5
            print("\nScore: ", playerScore)
            print("\nWhat would you like to do next?")
            print("\t1. Try again in same category")
            print("\t2. Go to another category")
            decision =input("Choice: ")
    
        if len(guess) > len(colors[index]):     # Guess is too long
            print("\nThis word is too long. Please try again\n")
            tryAgain =input("Would you like to try again (y/n)? ")
            
        elif len(guess) < len(colors[index]):     # Guess is too short
            print("\nThis word is too short. Please try again\n")
            tryAgain =input("Would you like to try again (y/n)? ")

        elif guess.lower() != colors[index]:              # Guess is not the word
            print("\nThis is not the correct word\n")
            tryAgain =input("Would you like to try again (y/n)? ")
                 
    return playerScore

def animalTopic(playerScore): #if player choice of topic is animals
    #initialize variables
    tryAgain = 'y'
    decision = '1'

    #animals list
    animals = ['dog','lion','lizard']
   
    while tryAgain == 'y' and decision == '1':

        # Hints
        index = random.randint(0,2)
        print("Length of word: ", "-"*len(animals[index]))
        if index == 0:
            print("Hint: Most popular household pet in America\n")
        elif index == 1:
            print("Hint: Distant relative of cat (bigger and fluffier)\n")
        elif index == 2:
            print("Hint: Lots in Florida(singular)")
        
        guess = input("Guess: ")    # Ask for player guess
        if guess.lower() == animals[index]:    # Correct answer
            print("\nCongratulations ... You guessed the Word!\n")
            playerScore = playerScore + 5
            print("\nScore: ",playerScore)
            print("\nWhat would you like to do next?")
            print("\t1. Try again in same category")
            print("\t2. Go to another category")
            decision =input("Choice: ")
    
        if len(guess) > len(animals[index]):     # Guess is too long
            print("\nThis word is too long. Please try again\n")
            tryAgain =input("Would you like to try again (y/n)? ")
            
        elif len(guess) < len(animals[index]):     # Guess is too short
            print("\nThis word is too short. Please try again\n")
            tryAgain =input("Would you like to try again (y/n)? ")

        elif guess.lower() != animals[index]:              # Guess is not the word
            print("\nThis is not the correct word\n")
            tryAgain =input("Would you like to try again (y/n)? ")
                 
    return playerScore

main()

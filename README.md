# High-Score
Guess the word!\
This program plays guess the word with the user.
In my main function, I used a while and if loops to create a menu driven interface that will repeat itself until quit is input as a choice. The menu shows the options to display the rules of the game if user input for choice is 1, play the game if choice is 2, display the high score if choice is 3, and quit if choice 4. If any other option is input as choice, then an error message will be displayed, and the user will have to input another choice until it is a correct one \
The player is first asked their alias for the game\ 
  Option 1 displays the rules using print. 
  Option 2 will initiate the game. I used a variable named score that will keep the user score as they play along. Using a while loop, as long as      the player decides to keep playing, the game will keep running. 
Next, the player has to input a choice of topic of words\
If the player choses the first option(food), the program will skip to the function Food Topic, using the variable score as a parameter in order to keep the score going throughout the game. In the Food Topic function, I initialized the variable for try again and decision (explained later on). I used a list to put three choices of food. Inside a while loop, I used a random number generator from the random library to choose a random number from zero to two for the index of the list I created. If the random index is zero, then a hint for the first food in the list will be displayed and so on. In order to display the length of the word that the player has to guess, I used the len function. If the user enters a word too short, too long, or not the correct word for the guess, an error message will be displayed, and ask the player if they would like to try again. If the player guesses the word correctly, a congratulatory message will be displayed, five points will be added to the score, and the choice to continue in the same category or go to another category will be displayed. If the user decides to go to another category, the program will return the score collected from this category and return to the main function\
If the player chooses the second option of topic, the program will skip to the Color Topic function. This function works the same as the Food Topic, while using and returning the score tracker in order to maintain the score throughout the game. Same thing if player chooses option 3 and skip to Animal Topic\
In order to stop playing this round, the user must reply no when asked if they would like to continue. If the player chooses no, the main menu will be displayed for the player to choose another option or quit\
Using an if statement, if the player has a high score, the player’s alias and their high score will be recorded into a file that was created at the beginning of the program, named highscore.txt. In order to make it more challenging, I decided to insert a high score that the player must beat in order to replace it. The high score I decided on is 20, and I wrote it to the file using dot notation. After writing down the score, I close the file and continue with the game. When the user choses to view their high score using the third option of the menu, their name and score will be displayed using the dot read notation from the file I created previously\
When the player wants to stop playing, choice number 4 will quit, and display a farewell message.

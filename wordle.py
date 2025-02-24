# Wordle Game
# February 24, 2025
# Marxius Ivan Adolf Denniel

#1. Import random for picking random words in a list.
import random

#2. Create an interface function that asks player to play.
def interface():
    print("Welcome to Wordle! Would you like to play?")
    while True:
        ans = str(input("[Y/N] ")).upper()
        if ans == "Y":
            return True
        elif ans == "N":
            print("\n---Exit---")
            return False
        else:
            print("Invalid input. Please try again.")

#3. Create a display function to display each letter of a 5-letter word.

#4. Create the main wordle game function.

    #4.1 Make a list of 5-letter words and randomly pick one for each wordle.

    #4.2 Print the display (6 rows of empty letter slots).

    #4.3 Ask the player to guess a 5-letter word.

	#4.3.1 Detect if the input contains 5 letters.

	#4.4 Determine which letter of the guessed letter coincides with the correct word.

	#4.5 Update the display. If the guess was correct, end game here (Win). Else, continue to 4.6.

	#4.6 Display whether the guessed letter was in the right or wrong slot (and from which column to avoid confusion).

    #4.7 If all 6 rows are filled without guessing the correct word, end game here (Lose).

#5. Create a function that asks player to continue playing.

#6. Call functions and loop to run the game.

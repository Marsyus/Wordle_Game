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
            print("\n--- Exit ---")
            return False
        else:
            print("Invalid input. Please try again.")

#3. Create a display function to display each letter of a 5-letter word.
def row(x):
    rows = f"[ {x[0]} ][ {x[1]} ][ {x[2]} ][ {x[3]} ][ {x[4]} ]"
    return rows

#4. Create the main wordle game function.
def wordle():
    #4.1 Make a list of 5-letter words and randomly pick one for each wordle.
    words = ["ABODE", "ACUTE", "AGENT", "ALARM", "AMBER", "APPLE", "BEACH", "BLAZE", "BLEND", "BRAVE", "BREAD", "BRISK", "BRUSH", "BUNCH", "BUNNY", "CHAIR", "CHART", "CHIME", "CLOCK", "CLOUD", "CLOVE", "CRISP", "DREAM", "DRESS", "DRIFT", "DROWN", "DWELL", "EAGLE", "EARTH", "ELOPE", "EMBER", "EXCEL", "FABLE", "FLAME", "FEAST", "FLINT", "FLOOR", "FORGE", "FRESH", "FROST", "GLASS", "GLOVE", "GRAPE", "GRASP", "GRIMY", "GUSTO", "HAPPY", "HATCH", "HOIST", "HOUSE", "HUMID", "INBOX", "INDEX", "INFER", "IVORY", "JOINT", "JOKER", "JOLLY", "JOUST", "KAPPA", "KIOSK", "KNACK", "KRAUT", "LAPSE", "LATCH", "LEAFY", "LEMON", "LIGHT", "LODGE", "LUCKY", "MANGO", "MAPLE", "MERCY", "MIRTH", "MOUNT", "MUSIC", "NEXUS", "NIFTY", "NOMAD", "NUDGE", "OCEAN", "OCTET", "OPINE", "OUTER", "PAINT", "PAPER", "PANDA", "PENCIL", "PIQUE", "PLANE", "PLANT", "PLATE", "PLUME", "POWER", "PRINT", "PRISM", "PULSE", "QUAIL", "QUASH", "QUIET", "QUILT", "QUIRK", "REACT", "RIGID", "RINSE", "ROACH", "RULER", "SHELL", "SHIRT", "SHOES", "SLANT", "SLOPE", "SMILE", "SOUND", "SPOON", "STARS", "STONE", "STONY", "STORY", "SWEET", "TABLE", "THORN", "TIGER", "TRACE", "TRAIN", "TRUST", "TWEAK", "ULCER", "UNITE", "URBAN", "USHER", "VAPOR", "VERGE", "VIEWS", "VIVID", "VIXEN", "WALTZ", "WATER", "WHEAT", "WOVEN", "WRECK", "XENON", "XEROX", "YACHT", "YIELD", "YODEL", "ZEBRA", "ZESTS", "ZESTY", "ZONED"]
    word = words[random.randint(0, 149)]
    empty = [" "] * 5
    attempts = 6
    guesses = []

    #4.2 Print the display (6 rows of empty letter slots).
    print("\n--- Wordle ---\n")
    print("\n".join([row(empty)] * attempts))

    #4.3 Ask the player to guess a 5-letter word.
    while True:
        if attempts == 0:
            break

        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        guess = input("\nEnter a 5-letter word: ").upper()
        print()

	#4.3.1 Detect if the input contains 5 letters.
	if any(char not in alphabet for char in guess):
            print("!! Special characters detected  !!\n!! Please input a 5-letter word !!")
        elif len(guess) != 5:
            print(f"!!    {len(guess)}-letter word detected    !!\n!! Please input a 5-letter word !!")
        else:
            guesses.append(guess)
            attempts -= 1

	    #4.4 Determine which letter of the guessed letter coincides with the correct word.
	    for h in guesses:
                right_match = [char if char == letter else " " for char, letter in zip(h, word)]
                wrong_match = [char if char in word and char not in right_match else " " for char in h]

	    #4.5 Update the display. If the guess was correct, end game here (Win). Else, continue to 4.6.
	    for g in guesses:
                print(row(g))
            for i in range(6 - len(guesses)):
                print(row(empty))
            if guess == word:
                print(f"\nThe correct word was: {word}\nCongratulations! You guessed the word!")
                return

	    #4.6 Display whether the guessed letter was in the right or wrong slot (and from which column to avoid confusion).
	    else:
                print("\nColumn      -  1  2  3  4  5")
                print("Right slot  - ", "  ".join(right_match))
                print("Wrong slot  - ", "  ".join(wrong_match))

    #4.7 If all 6 rows are filled without guessing the correct word, end game here (Lose).
    print(f"\nGame over! The correct word was: {word}")

#5. Create a function that asks player to continue playing.
def continues():
    print("\nWould you like to play again?")
    while True:
        ans = str(input("[Y/N] ")).upper()
        if ans == "Y":
            return True
        elif ans == "N":
            print("\n--- Exit ---")
            return False
        else:
            print("Invalid input. Please try again.")   

#6. Call functions and loop to run the game.
if interface():
    wordle()
    while continues():
	wordle()

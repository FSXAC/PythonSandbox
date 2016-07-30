# Number Guessing Game
# Last edited by Mansur

# Imports
import random

# All functions are defined below

def displayIntro():
    """ This will display the game intro"""
    print("\nI'm thinking of a number")
    print("See if you can guess my number in the fewest amount of tries...")

def getDifficulty():
    """This function will let user choose what difficulty they want"""\
    # It is always looping until user's choice is valid
    while True:
        print(\
            """
[A] - Easy      (Guess between 1 to 50)
[B] - Normal    (Guess between 1 to 100)
[C] - Hard      (Guess between 1 to 500)\n""")
        difficulty = str(input("[Your Selection] > "))

        # This will check whether if the user choice is valid or not
        if difficulty.lower() == "a" or difficulty.lower() == "b" or difficulty.lower() == "c":
            break
        else:
            input("Invalid Input, Please Try Again")

    # returns user's difficulty choice once the loop is broken
    return difficulty.lower()

def checkAnswer(guess, answer):
    """ This will check whether if the guess is higher, lower or equal to the number
        Returns a boolean """
    
    if guess == answer:
        print("\nGood job!  You guessed my number!")
        return True
    elif guess < answer:
        print("Your guess is too low.")
        return False
    else:
        print("Your guess is too high.")
        return False
    
def getGuess():
    """ This will check if the guess is actually a number"""
    while True:
        guess = input("\n[Your Guess] > ")
        try:
            guess = int(guess)
            break
        except:
            input("Invalid Input, Try Again Please")
    return guess

def genNumber(difficulty):
    """ Selects the range of the number and generates it
        depends on the difficulty user chose """
    if difficulty == 1:
        number = random.randrange(1, 51)
        return number
    elif difficulty == 2:
        number = random.randrange(1, 101)
        return number
    else:
        number = random.randrange(1, 501)
        return number

# Main program

# Intro
displayIntro()

# Program loop
while True:

    # Reset tries to 0
    tries = 0
    difficulty = getDifficulty()

    # This in only for the print function below
    if difficulty == "a":
        number = genNumber(1)
        guessRange = 50
    elif difficulty == "b":
        number = genNumber(2)
        guessRange = 100
    else:
        number = genNumber(3)
        guessRange = 500
        
    print("\nThe number has generated! guess between 1 and", guessRange)

    # Will keep looping until user gets the number right
    while True:
        guess = getGuess()
        tries += 1
        if checkAnswer(guess, number) == True:
            if tries == 1:
                print("And it only took you 1 try! Amazing!")
            else:
                print("It took you", tries, "tries!")
            break

    # Asks the user if they want to go again
    ask = str(input("\nYou want to go again? (y/n) "))
    if ask.lower() == "n":
        break
    elif ask.lower() == "y":
        None
    else:
        print("Invalid Input, Try Again Please")

# Outro
input("\nThank you for playing, press enter key to continue")

        
        
    

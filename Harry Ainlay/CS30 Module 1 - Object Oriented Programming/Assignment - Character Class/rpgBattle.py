# Defining Classes Assignment - Character Class
#
# This program imports a Character class that students will have to code in order
# for the program to function.  The program executes a turn based battle between two
# users.
# Mr. V September 2014

import time
from characterClass import Character

def main():
    """ Main function"""

    # Welcome, set up players and initialize variables
    print("Welcome to the Battle!")
    player1 = input("Please enter the name of player 1: ")
    player1 = Character(player1)  # Reassign player1 to be an Character object reference

    player2 = input("Please enter the name of player 2: ")
    player2 = Character(player2)  # Reassign player2 to be an Character object reference

    turn = 1    # Player 1's Turn (turn = 1)  Player 2's Turn (turn = 2)

    print()
    print("Welcome", player1.getName(), "and", player2.getName(), ".  Prepare to battle...")
    time.sleep(2)

    # Turn based battle till victory
    loop = True
    while loop:
        # Display Player Stats
        print()
        print("Player Stats")
        print(player1)
        print(player2)


        # Execute a turn of the battle
        gameOn = battleRound(turn, player1, player2)

        # Check results of the last round and take action
        if not gameOn:
            # end battle
            loop = False
        else:
            # switch turns
            if turn == 1:
                turn = 2;
            else:
                turn = 1
        
    # end while loop

# end main()


def battleRound(pTurn, p1, p2):
    """ Execute a round of battle.  Return True if game continues, False if game is over, else return True"""

    # Set up temp variables for attacking player and defending player based on turn
    if pTurn == 1:
        pAttack = p1
        pDefend = p2
    else:
        pAttack = p2
        pDefend = p1

    # Get attacking players selection
    print()
    print(pAttack.getName(), "- Options:")
    print("1. Strong Attack")
    print("2. Quick Attack")
    print("3. Run Away")
    selection = input("Select a number from the menu above: ")
    time.sleep(1)

    if selection == "1":
        pDefend.strongAttack()
    elif selection == "2":
        pDefend.quickAttack()
    elif selection == "3":
        pDefend.addVictory()
        print()
        print(pAttack.getName(), "runs away like a coward.")
        print("Congratulations", pDefend.getName(), ", you have prevailed!")
        print("Final Battle Stats:")
        print(p1)
        print(p2)

        return False  # indicate end of battle
    else:
        print("Invalid selection. You lose a turn.")


    # Check if attack ended battle
    if pDefend.isDead():
        pAttack.addVictory()
        print()
        print("Congratulations", pAttack.getName(), ", you have prevailed!")
        print("Final Battle Stats:")
        print(p1)
        print(p2)
        return False  # indicate end of battle
    else:
        return True  # battle continues

# end battleRound()    


# Call main() to begin program
main()





    

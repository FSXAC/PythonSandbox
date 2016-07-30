# Math Battle assignment for OOP1
#
# Mr. V

# import file for Player Class and MathQuizzer Class
import mathBattleClasses as mbc


class MathManager:
    """ A class to manage a math battle between users."""

    def __init__(self):
        # Print a welcome.
        print()
        print("WELCOME TO THE MATH BATTLE!")
        print()

        self.players = []
        self.player_count = int(self.ask("How many players are joining? (2-4): ", ("2", "3", "4")))

        # a loop that adds player instances to players list
        for i in range(self.player_count):
            self.players.append(mbc.Player(self.ask("Please enter the name of player " + str(i + 1) + ": ")))
        
        # Initialize a math quizzer object.
        self.mathQuizzer = mbc.MathQuizzer()

    # end __init__


    def main(self):
        """ Main method to run main menu for math battle."""

        loop = True
        while loop:
            print()
            print("MENU OPTIONS: ")
            print("1: Play a round.")
            print("2: Play up to a point")
            print("3: Set Operation.")
            print("4: Display Statistics.")
            print("5: Exit")

            print()
            userInput = self.ask("Please select a number from the menu above: ", ("1", "2", "3", "4"))

            if userInput == "1":
                print("Play a round.")
                for i in range(self.player_count):
                    self.playRound(self.players[i])
            elif userInput == "2":
                # play to a point
                # set goal point
                goal = int(self.ask("How many points are we playing to? (2 - 5): ", ("2", "3", "4", "5")))

                # reset player points for this game mode
                for i in range(self.player_count):
                    self.players[i].resetRoundPt()

                # loop var
                game_loop = True
                    
                # play
                while game_loop:
                    for i in range(self.player_count):
                        self.playRound(self.players[i], True)

                        # check if one player has that point
                        if self.players[i].getRoundPt() >= goal:
                            winner = self.players[i].getName()
                            game_loop = False
                            break     
                
                print("\n\n\nCongratulations! " + winner + " wins!!!!")
            elif userInput == "3":
                print("Set Operation.")
                self.mathQuizzer.setOperation(self.ask("Please select an operation (+,-,*,/): ", ("+", "-", "*", "/")))
            elif userInput == "4":
                print("Display Statistics")
                for i in range(self.player_count):
                    print(self.players[i])
            elif userInput == "5":
                print("Goodbye.")
                loop = False
            else:
                print("Invalid selection.")

        # end while loop

    # end main

    def playRound(self, aPlayer, hasGoal = False):

        # the two game modes
        if hasGoal:
            print()
            print(aPlayer.getName(), ", here is your question...")
            self.mathQuizzer.askQuestion()
            userAnswer = int(self.ask("What is your answer to the question above: "))
            if self.mathQuizzer.isAnswer(userAnswer):
                print("Congratulations!  Your answer is correct.")
                aPlayer.increaseRoundPt()
            else:
                print("Sorry, your answer is incorrect.")           
        else:
            print()
            print(aPlayer.getName(), ", here is your question...")
            self.mathQuizzer.askQuestion()
            userAnswer = int(self.ask("What is your answer to the question above: "))
            if self.mathQuizzer.isAnswer(userAnswer):
                print("Congratulations!  Your answer is correct.")
                aPlayer.increaseCorrect()
            else:
                print("Sorry, your answer is incorrect.")
                aPlayer.increaseIncorrect()


    # ask method
    def ask(self, msg, whitelist = ()):
        user_input = str(input(msg))

        # if whitelist is valid
        if whitelist:
            while user_input not in whitelist:
                user_input = input(msg)
        else:
            while not user_input:
                user_input = input(msg)

        return user_input

    # end playRound

            
# end class MathManager    
        
        
    

# Create a MathManager object and ask it to begin the program
myManager = MathManager()
myManager.main()

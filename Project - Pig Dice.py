#### PIG DICE GAME ####

import random
import math
import os


def main():
    userInterface = UI()
    userInterface.menu()


class UI():
    def __init__(self):
        ### something here
        a = True

    def ask(self, whitelist, msg = ""):
        ### ask the user for certain things
        # display a message if there is any
        if msg != "":
                print(msg)
        while True:
            # ask
            var = input("> ")
            if (var.lower() in whitelist):
                break
        return var

    def askNot(self, blacklist, msg = ""):
        ### ask the user for certain things
        # display a message if there is any
        if msg != "":
                print(msg)
        while True:
            # ask
            var = input("> ")
            if (var not in blacklist):
                break
        return var

    def menu(self):
        print("""
#########################################
#            PIG - DICE GAME            #
#########################################

Please select one of the options below

[1]\tSINGLEPLAYER (WIP)
[2]\tMULTIPLAYER
[3]\tHELP
[4]\tEXIT\n""")

        ### ask for commands, if nothing or invalid is entered, it will keep looping
        user_input = self.ask(("1", "2", "3", "4"))

        ### this is after player has entered a choice
        if user_input == "1":
            # singleplayer
            self.singleplayer()

        elif user_input == "2":
            # multiplayer
            # ask for number of players that would be playing
            self.no_of_players = int(self.ask(("2", "3", "4"), "\nHOW MANY PLAYERS ARE GOING TO BE PLAYING? (2-4)"))

            # call the method
            self.multiplayer()

        elif user_input == "3":
            # call help
            self.instruction()

        elif user_input == "4":
            # quit the program
            self.terminate()

        else:
            # error exception
            error = True

    def options(self, isMultiplayer = True):
        ### user will be prompted to select some of the game options
        # ask goal points
        print("""
\nWhat point are you playing to?
[1]\tQUICK GAME (50 PT)
[2]\tSTANDARD GAME (100 PT)
[3]\tEXTENDED GAME (150 PT)\n""")

        # select goal
        goal_choice = int(self.ask(("1", "2", "3")))
        if goal_choice == 1:
            goal = 50
        elif goal_choice == 2:
            goal = 100
        elif goal_choice == 3:
            goal = 150

        # ask for the difficulty of BOT
        if not isMultiplayer:         
            print("""
\nWhat difficulty do you want the BOT to be?
[1]\tHARMLESS BOT
[2]\tMEDIUM BOT
[3]\tEXPERT BOT\n""")
            difficulty = int(self.ask(("1", "2", "3")))

            # return singleplayer options
            return [goal, difficulty]

        else:
            # return multiplayer options
            return [goal]
            
    def singleplayer(self):
        ### singleplayer algorithms
        self.option = self.options(False)
        self.goal = self.option[0]
        self.difficulty = self.option[1]
        self.game = Game()

        ### start the game for singleplayer by creating a new game instance
        self.game.setPlayers(1)
        self.game.setGoal(self.goal)
        self.game.setDifficulty(self.difficulty)
        self.game.play()
        
    def multiplayer(self):
        ### multiplayer algorithms
        self.option = self.options(True)
        self.goal = self.option[0]
        
        ### start the game for multiplayer by creating a new game instance
        self.game = Game()
        self.game.setPlayers(self.no_of_players)
        self.game.setGoal(self.goal)
        self.game.play()

    def instruction(self):
        ### display instructions
        print("""
#########################################
#              INSTRUCTIONS             #
#########################################
# Pig is a dice game                    #
# Lorem Ipsum                           #
# Lorem Ipsum                           #
# Lorem Ipsum                           #
#########################################

Ready?
[1]\tBACK TO MAIN MENU\n""")
        
        # back to the main menu
        input("> ")        
        self.menu()

    def terminate(self):
        ### terminates the program
        input("\nPROGRAM TERMINATED. PRESS ENTER TO CONTINUE.")

  
class Game():

    def __init__(self):
        """ constructor """
        self.number_of_players = 0
        self.players = []

    def roll(self):
        """ rolls the dice """
        return random.randint(1, 6)

    def ask(self, whitelist, msg = ""):
        ### ask the user for certain things
        # display a message if there is any
        if msg != "":
                print(msg)
        while True:
            # ask
            var = input("> ")
            if (var.lower() in whitelist):
                break
        return var

    def askBool(self, true, false, msg = ""):
        # ask boolean
        # display a message if there is any
        if msg != "":
                print(msg)
        while True:
            # ask
            var = input("> ")
            if (var.lower() in true):
                boolean = True
                break
            elif (var.lower() in false):
                boolean = False
                break
        return boolean

    ### Setter
    def setPlayers(self, players):
        ### setter for number of players
        self.number_of_players = players

    def setGoal(self, goal):
        self.goal = goal

    def setDifficulty(self, difficulty):
        self.difficulty = difficulty

    ### Getter
    def getTopScore(self):
        """ returns the top score in the players list """
        scores = []
        for i in range(len(self.players)):
            scores.append(self.players[i].getScore())

        return [max(scores), scores.index(max(scores))]
            
    ### main functions
    def play(self):
        if self.number_of_players == 1:
            self.playSingleplayer(self.difficulty)
        else:
            self.playMultiplayer()

    def playSingleplayer(self, difficulty):
        """ play singleplayer. will add AI in it later """

    def playMultiplayer(self):
        """ play local multiplayer """

        ### initial MP setup
        for i in range(self.number_of_players):
            self.players.append(Player(True))

        # ask for player names
        for i in range(len(self.players)):
            print("\nPlayer " + str(i + 1) + ", what is your name?")
            player_name = input("> ")
            while player_name == "":
                player_name = input("> ")

            # set player names
            self.players[i].setName(player_name)

        end = False
        print("\nGAME STARTED!")
        
        ### main game loop
        while end == False:

            ### turns for players
            for player in range(len(self.players)):
                ### each turn
                print("\n\n\n\n" + self.players[player].getName() + ", it's your turn!")

                current_rolls = []
                current_score = 0
                have_score = False
                roll = self.roll()

                if roll != 1:
                    ### if initial roll is not 1
                    current_rolls.append(roll)
                    
                    while True:
                        # always ask
                        response = self.askBool(("yes", "y"), ("no", "n"), "You rolled a " + str(roll) + ". Again?")
                        if response == True:
                            # player wants to play again
                            roll = self.roll()
                            if roll == 1:
                                print("You have rolled a 1, turn ended!")
                                have_score = False
                                break
                            else:
                                current_rolls.append(roll)
                        else:
                            # players wants to pass
                            have_score = True
                            break 
                else:
                    ### if initial roll is 1
                    print("You have rolled a 1, turn ended!")
                    have_score = False

                ### total up the scores
                if have_score:
                    current_score = sum(current_rolls)
                    self.players[player].setScore(self.players[player].getScore() + current_score)
                    print("\n" + self.players[player].getName() + ", your score is now " + str(self.players[player].getScore()))
                else:
                    # if at anytime a 1 is rolled
                    print("\n" + self.players[player].getName() + ", your score is still " + str(self.players[player].getScore()))
                input()

            # end the game when one reaches the goal and return to menu 
            scores = self.getTopScore()
            top_score = scores[0]
            top_player = scores[1]
            
            if top_score >= self.goal:
                input("\n\n\n\nCONGRATULATIONS, " + self.players[top_player].getName().upper() + ", YOU WIN!")                
                end = True

        userInterface = UI()
        userInterface.menu()

                
class Player():

    def __init__(self, isHuman):
        self.name = "Player"
        self.score = 0
        self.isHuman = isHuman

    ### getters and setters
    ## setters
    def setName(self, name):
        self.name = name

    def setScore(self, score):
        self.score = score
        
    ## getters
    def getName(self):
        return self.name

    def getScore(self):
        return self.score

	
main()

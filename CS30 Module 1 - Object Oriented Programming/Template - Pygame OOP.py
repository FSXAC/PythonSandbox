#### PYGAME BUILDING TEMPLATE ####
#### 2014 SEPTEMBER 03        ####

#### ESSENTIAL IMPORTS
import pygame
import random
import math
import time
import os

def main():

    #### DISPLAY OPTIONS
    SCREEN_WIDTH = 1100
    SCREEN_HEIGHT = 800
    SCREEN_SIZE = [SCREEN_WIDTH, SCREEN_HEIGHT]
    
    game = MainGame(SCREEN_SIZE)
    game.setFPS(2)
    game.setCaption("TEMPLATE")

    # run
    game.run()

#### MAIN CLASS
class MainGame():
    " main class for the game and its properties"
    
    def __init__(self, screenSize):
        """ constructor """
        # Setup
        pygame.init()

        # initialize all variables that will be used later
        self.FPS = 1
        self.isFinished = False

        # pygame variables
        self.pyClock = pygame.time.Clock()
        self.pyFont = pygame.font.Font(None, 80)
        self.pyScreen = pygame.display.set_mode(screenSize)

        #### BASIC COLOR DEFINITION
        self.COLOR_BLACK = [0, 0, 0]
        self.COLOR_WHITE = [255, 255, 255]
        self.COLOR_RED = [255, 0, 0]
        self.COLOR_GREEN = [0, 255, 0]
        self.COLOR_BLUE = [0, 0, 255]

        self.COLORS = [[0, 0, 0],
                       [255, 255, 255],
                       [255, 0, 0],
                       [0, 255, 0],
                       [0, 0, 255]]
                        

    ### GETTERS and SETTERS
    # Set
    def setFPS(self, fps):
        self.FPS = fps

    def setCaption(self, cap):
        pygame.display.set_caption(cap)

    ### Main methods
    def run(self):
        """ run the main methods """
 
        while self.isFinished == False:
            self.pyClock.tick(self.FPS)

            ### Events
            for events in pygame.event.get():

                # Exit the game
                if events.type == pygame.QUIT:
                    self.isFinished = True

            ### Screen draws
            self.pyScreen.blit(self.pyFont.render("HELLO WORLD", True, random.choice(self.COLORS)), [10, 10])
            
            ### Screen update
            pygame.display.flip()

        ### Terminating pygame
        pygame.quit()        

#### Runs the main program
main()

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
    
    global SCREEN_SIZE
    SCREEN_SIZE = [SCREEN_WIDTH, SCREEN_HEIGHT]
    
    game = MainGame(SCREEN_SIZE)
    game.setFPS(60)
    game.setCaption("AcidSnow 2")

    # run
    game.run()

class Snow():
    def __init__(self, size, color):
        "snowflake constructor"
        self.size = size
        self.color = color
        self.position = (random.randint(0, SCREEN_SIZE[0] - self.size),
                         random.randint(0, SCREEN_SIZE[1] - self.size))

    def move(self, speed = 1, wind = 0):
        """ move the snowflake """
        self.position[0] += wind
        self.position[1] += speed

    def draw(self, screen):
        """ draws the snowflake onto the screen """
        pygame.draw.ellipse(screen, self.color, [self.position[0], self.position[1], self.size, self.size])

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

        # game and other logic variables
        self.frame_count = 0

        self.snow_flakes = []
        self.snow_flakes_front = []
        self.snow_flakes_back = []

        self.invisible = True
                        

    ### GETTERS and SETTERS
    # Set
    def setFPS(self, fps):
        self.FPS = fps

    def setCaption(self, cap):
        pygame.display.set_caption(cap)

    # create snow
    def createSnow(self):
        for i in range(50):
            self.snow_flake.append(Snow(12, (250, 250, 250)))
        for j in range(20):
            self.snow_flake_front.append(Snow(20, (255, 255, 255)))
        for k in range(10):
            self.snow_flake_back.append(Snow(10, (150, 150, 150)))

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

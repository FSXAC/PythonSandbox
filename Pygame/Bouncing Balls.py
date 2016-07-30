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
    game.setFPS(60)
    game.setCaption("BOUNCING BALLS")

    # run
    game.run()

#### BALL CLASS
class Ball():
    """ Create a ball """
    def __init__(self, init_pos, screen):
        self.screen = screen
        self.radius = random.randint(2, 15)
        self.position = [init_pos[0], init_pos[1]]
        self.color = (random.randint(200, 255), random.randint(100, 255), 0)
        #self.color = (random.randint(0, 0), random.randint(0, 0), random.randint(50, 255))
        self.speed_x = float(random.randint(-20, 20)) / 10
        self.speed_y = float(random.randint(-20, 20)) / 10
        self.bounce = float(random.randint(2, 8)) / 10

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.position, self.radius, 0)

        # movement
        self.position[0] = int(self.position[0] + self.speed_x)
        self.position[1] = int(self.position[1] + self.speed_y)

        # gravity
        self.speed_y += 0.2

        # bounce
        if self.position[1] > 800:
            self.position[1] = 800 - self.radius
            self.speed_y *= 0 - self.bounce
            #pygame.mixer.Sound("pop.wav").play()

##        if self.position[0] > 1100:
##            self.position[0] = 1100 - self.radius
##            self.speed_x *= -1
##
##        if self.position[0] < 0:
##            self.position[0] = 0 + self.radius
##            self.speed_x *= -1

    def setPosition(self, position):
        self.position = position

##    def setMovementX(self, x):
##        self.delta_x = x
##
##    def setMovementY(self, y):
##        self.delta_y = y

    def getPosition(self):
        return self.position

    def getMovement(self):
        return [self.delta_x, self.delta_y]
    
        
    
#### MAIN CLASS
class MainGame():
    """ main class for the game and its properties"""
    
    def __init__(self, screenSize):
        """ constructor """
        # Setup
        pygame.init()

        # no default mouse cursor
        pygame.mouse.set_visible(False)

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

        # initialize all variables that will be used later
        self.FPS = 1
        self.isFinished = False

        # pygame variables
        self.pyClock = pygame.time.Clock()
        self.pyFont = pygame.font.Font(None, 80)
        self.pyScreen = pygame.display.set_mode(screenSize)
        self.pyPointer = pygame.image.load("pointer.png").convert()
        self.pyPointer.set_colorkey(self.COLOR_BLACK)
    
        #### Game variables
        self.objs = []
        self.auto_clear_screen = True

    ### GETTERS and SETTERS
    # Set
    def setFPS(self, fps):
        self.FPS = fps

    def setCaption(self, cap):
        #pygame.display.set_caption(cap)
        ""

    ### Main methods
    def run(self):
        """ run the main methods """
 
        while self.isFinished == False:
            self.pyClock.tick(self.FPS)

            # always get mouse position
            self.mouse_pos = pygame.mouse.get_pos()

            ### Events
            for events in pygame.event.get():

                # Exit the game
                if events.type == pygame.QUIT:
                    self.isFinished = True
                # Mouse down
                if events.type == pygame.MOUSEBUTTONDOWN:                    
                    self.objs.append(Ball(self.mouse_pos, self.pyScreen))

                # Keyboard commands
                if events.type == pygame.KEYDOWN:

                    # delete all balls
                    if events.key == pygame.K_DELETE:
                        del self.objs[:]

                    # manually clear the screen
                    if events.key == pygame.K_END:
                        self.pyScreen.fill(self.COLOR_BLACK)

                    # toggle auto clear screen
                    if events.key == pygame.K_HOME:
                        if self.auto_clear_screen:
                            self.auto_clear_screen = False
                        else:
                            self.auto_clear_screen = True

                    ### create balls
                    # a line of balls
                    if events.key == pygame.K_1:
                        for y in range(2):
                            for x in range(50):
                                self.objs.append(Ball((x * 25, y * 25), self.pyScreen))

                    # explosion of balls
                    if events.key == pygame.K_2:
                        for i in range(100):
                            self.objs.append(Ball((550, 50), self.pyScreen))

                    # explosion of balls on cursor
                    if events.key == pygame.K_3:
                        for i in range(100):
                            self.objs.append(Ball(self.mouse_pos, self.pyScreen))

                    # random explosions of balls on screen
                    if events.key == pygame.K_4:
                        for i in range(16):
                            for o in range(24):
                                self.objs.append(Ball((random.randint(50, 1050), random.randint(20, 500)), self.pyScreen))
                        

            ### Screen draws
            # clear the screen first
            if self.auto_clear_screen:
                self.pyScreen.fill(self.COLOR_BLACK)

            # mouse pointer
            pointer_x = self.mouse_pos[0] - 2
            pointer_y = self.mouse_pos[1] - 2
            self.pyScreen.blit(self.pyPointer, [pointer_x, pointer_y])

            # messages on the screen
            balls = len(self.objs)
            if balls == 0:
                self.pyScreen.blit(self.pyFont.render("~ BALL ~", True, self.COLOR_WHITE), (440, 350))
            elif balls > 0 and balls < 30:
                self.pyScreen.blit(self.pyFont.render("TRY SCROLLING", True, self.COLOR_WHITE), (320, 350))
            elif balls > 30 and balls < 100:
                self.pyScreen.blit(self.pyFont.render("PRESS 1", True, self.COLOR_WHITE), (440, 350))

            # draw the balls
            for obj in range(len(self.objs)):
                self.objs[obj].draw()
            
            ### Screen update
            pygame.display.flip()

        ### Terminating pygame
        pygame.quit()        

#### Runs the main program
main()

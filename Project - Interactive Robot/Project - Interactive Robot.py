#### PYGAME INTERACTIVE ROBOT ####
#### 2014 SEPTEMBER 03        ####

#### ESSENTIAL IMPORTS
import pygame
import random
import math
import time
import os

def main():

    #### DISPLAY OPTIONS
    global SCREENS_SIZE
    global BODY_INITIAL_POS

    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 800
    SCREEN_SIZE = [SCREEN_WIDTH, SCREEN_HEIGHT]
    
    BODY_INITIAL_POS = ((SCREEN_SIZE[0] - 420) / 2, 200)
    
    game = MainGame(SCREEN_SIZE)
    game.setFPS(20)
    game.setCaption("INTERACTIVE ROBOT")

    # run
    game.run()

#### Robot class
class RobotBody():
    """ this class will be the robot body """
    def __init__(self):
        """ constructor """
        self.body = pygame.image.load("robot.png")
        self.position = (0, 0)

    def draw(self, screen):
        screen.blit(self.body, BODY_INITIAL_POS)

class RobotTooth():
    def __init__(self, position):
        """ constructor """
        self.size = (30, 30)
        self.position = position
        self.light = pygame.image.load("tooth.png")
        self.dark = pygame.image.load("toothDark.png")
        
        self.tooth = self.light
        self.status = True

    def isLight(self):
        return self.status

    def setLight(self, new_status):
        self.status = new_status

    def toggle(self):
        """ toggle the tooth light """
        if self.isLight():
            self.setLight(False)
            self.tooth = self.dark
        elif self.isLight() == False:
            self.setLight(True)
            self.tooth = self.light

    def draw(self, screen):
        """ draw the teeth """
        screen.blit(self.tooth, self.position)

class RobotEye():
    # eye size is 14px x 14px
    def __init__(self, center):
        self.size = 14
        self.origin = center
        self.pos = center
        self.eye = pygame.image.load("eye.png")

    def setPos(self, position):
        self.pos = position

    def setPosToOrigin(self):
        self.pos = self.origin

    def getPos(self):
        return self.pos

    def getDistanceFromCenter(self):
        """ get distance from current eye position to the center of the eye """
        position = self.getPos()
        distance_x = position[0] - self.origin[0]
        distance_y = self.origin[1] - position[1]

        return (distance_x, distance_y)

    def draw(self, screen):
        """ draws the eye """
        screen.blit(self.eye, (self.pos[0] - self.size / 2, self.pos[1] - self.size / 2))
        
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
        self.SCREEN_SIZE = screenSize

        # pygame variables
        self.pyClock = pygame.time.Clock()
        self.pyFont = pygame.font.Font(None, 80)
        self.pyScreen = pygame.display.set_mode(self.SCREEN_SIZE)

        self.background = pygame.image.load("back2_blurred.png").convert()

        self.tones = []
        self.tones.append(pygame.mixer.Sound("tone1.wav"))
        self.tones.append(pygame.mixer.Sound("tone2.wav"))
        self.tones.append(pygame.mixer.Sound("tone3.wav"))
        self.tones.append(pygame.mixer.Sound("tone4.wav"))
        self.tones.append(pygame.mixer.Sound("tone5.wav"))

        # pygame robot
        self.robotBody = RobotBody()
        self.teeth = []
        self.eyes = []

        for y in range(240+ 200, 380+ 200, 110):
            for x in range(120+430, 300+430, 30):
                # make teeth with x set as a position
                self.teeth.append(RobotTooth((x, y)))

        self.eyes.append(RobotEye((155 + 430, 150 + 200)))
        self.eyes.append(RobotEye((265 + 430, 150 + 200)))

        self.eyesMoveTogether = True
                
        #### BASIC COLOR DEFINITION
        self.COLOR_BLACK = [0, 0, 0]
        self.COLOR_WHITE = [255, 255, 255]
        self.COLOR_DARK_GREY = [50, 50, 50]
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

        def toggleTeeth(i):
            self.teeth[i].toggle()
            self.tones[random.randint(0, len(self.tones) - 1)].play()

        def resetTeeth():
            for i in range(len(self.teeth)):
                if self.teeth[i].isLight == False:
                    self.teeth[i].toggle()

        def moveEye(eye, direction):
            current_position = self.eyes[eye].getPos()
            current_distance = self.eyes[eye].getDistanceFromCenter()
            current_distance_r = math.sqrt(current_distance[0] ** 2 + current_distance[1] ** 2)
            current_quad = 0

            # allowed to move or not
            perm_move_right = True
            perm_move_left = True
            perm_move_up = True
            perm_move_down = True
            
            # on the boundary   
            if current_distance_r >= 42:

                # find what quadrant of the eye is on
                if current_distance[0] > 0:
                    if current_distance[1] > 0:
                        # +x +y
                        current_quad = 1
                    else:
                        # +x -y
                        current_quad = 4
                elif current_distance[0] < 0:
                    if current_distance[1] > 0:
                        # -x +y
                        current_quad = 2
                    else:
                        # -x -y
                        current_quad = 3

                # disable controls based on the quadrant
                if current_quad == 1:
                    # disable RIGHT and UP
                    #print("QUADRANT 1")
                    perm_move_right = False
                    perm_move_up = False

                elif current_quad == 2:
                    # disable LEFT and UP
                    #print("QUADRANT 2")
                    perm_move_left = False
                    perm_move_up = False

                elif current_quad == 3:
                    # disable LEFT and DOWN
                    #print("QUADRANT 3")
                    perm_move_left = False
                    perm_move_down = False

                elif current_quad == 4:
                    # disable RIGHT and DOWN
                    #print("QUADRANT 4")
                    perm_move_right = False
                    perm_move_down = False

##            print("DFO:", current_distance_r)
##            print("DFO_X:", current_distance[0])
##            print("DFO_Y:", current_distance[1])
##            print(perm_move_left)
##            print(perm_move_right)
##            print(perm_move_up)
##            print(perm_move_down)
                
            # two eyes will move in unified motion
            if self.eyesMoveTogether:
                for i in range(len(self.eyes)):
                    current_positions = self.eyes[i].getPos()
                    if direction == "left":
                        self.eyes[i].setPos((current_positions[0] - 2, current_positions[1]))
                    elif direction == "right":
                        self.eyes[i].setPos((current_positions[0] + 2, current_positions[1]))
                    elif direction == "up":
                        self.eyes[i].setPos((current_positions[0], current_positions[1] - 2))
                    elif direction == "down":
                        self.eyes[i].setPos((current_positions[0], current_positions[1] + 2))
                    else:
                        print("ERROR! Key not defined")
            else:
                if direction == "left" and perm_move_left:
                    self.eyes[eye].setPos((current_position[0] - 2, current_position[1]))
                elif direction == "right" and perm_move_right:
                    self.eyes[eye].setPos((current_position[0] + 2, current_position[1]))
                elif direction == "up" and perm_move_up:
                    self.eyes[eye].setPos((current_position[0], current_position[1] - 2))
                elif direction == "down" and perm_move_down:
                    self.eyes[eye].setPos((current_position[0], current_position[1] + 2))

        # eye control keys
        pressed_w = False
        pressed_a = False
        pressed_s = False
        pressed_d = False
        pressed_UP = False
        pressed_LEFT = False
        pressed_DOWN = False
        pressed_RIGHT = False

        while self.isFinished == False:
            self.pyClock.tick(self.FPS)

            ### Events
            for events in pygame.event.get():

                # Exit the game
                if events.type == pygame.QUIT:
                    self.isFinished = True

                # Mouse clicks
                if events.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_pos = pygame.mouse.get_pos()
                    self.mouse_button = pygame.mouse.get_pressed()

                # keyboard
                if events.type == pygame.KEYDOWN:
                    # teeth control
                    if events.key == pygame.K_1:
                        toggleTeeth(0)
                    if events.key == pygame.K_2:
                        toggleTeeth(1)
                    if events.key == pygame.K_3:
                        toggleTeeth(2)
                    if events.key == pygame.K_4:
                        toggleTeeth(3)
                    if events.key == pygame.K_5:
                        toggleTeeth(4)
                    if events.key == pygame.K_6:
                        toggleTeeth(5)
                    if events.key == pygame.K_7:
                        toggleTeeth(6)
                    if events.key == pygame.K_8:
                        toggleTeeth(7)
                    if events.key == pygame.K_9:
                        toggleTeeth(8)
                    if events.key == pygame.K_0:
                        toggleTeeth(9)
                    if events.key == pygame.K_MINUS:
                        toggleTeeth(10)
                    if events.key == pygame.K_EQUALS:
                        toggleTeeth(11)

                    # eye control - ON
                    if events.key == pygame.K_w:
                        pressed_w = True
                    if events.key == pygame.K_a:
                        pressed_a = True
                    if events.key == pygame.K_s:
                        pressed_s = True
                    if events.key == pygame.K_d:
                        pressed_d = True
                    if events.key == pygame.K_UP:
                        pressed_UP = True
                    if events.key == pygame.K_LEFT:
                        pressed_LEFT = True
                    if events.key == pygame.K_DOWN:
                        pressed_DOWN = True
                    if events.key == pygame.K_RIGHT:
                        pressed_RIGHT = True

                    # Robot Reset
                    if events.key == pygame.K_TAB:
                        if self.eyesMoveTogether:
                            self.eyesMoveTogether = False
                        else:
                            self.eyesMoveTogether = True

                        for i in range(len(self.eyes)):
                            self.eyes[i].setPosToOrigin()

                        resetTeeth()
                            

                if events.type == pygame.KEYUP:
                    # eye control
                    if events.key == pygame.K_w:
                        pressed_w = False
                    if events.key == pygame.K_a:
                        pressed_a = False
                    if events.key == pygame.K_s:
                        pressed_s = False
                    if events.key == pygame.K_d:
                        pressed_d = False
                    if events.key == pygame.K_UP:
                        pressed_UP = False
                    if events.key == pygame.K_LEFT:
                        pressed_LEFT = False
                    if events.key == pygame.K_DOWN:
                        pressed_DOWN = False
                    if events.key == pygame.K_RIGHT:
                        pressed_RIGHT = False


            # continuous eye control
            if pressed_w:
                moveEye(0, "up")
            if pressed_a:
                moveEye(0, "left")
            if pressed_s:
                moveEye(0, "down")
            if pressed_d:
                moveEye(0, "right")
            if pressed_UP:
                moveEye(1, "up")
            if pressed_LEFT:
                moveEye(1, "left")
            if pressed_DOWN:
                moveEye(1, "down")
            if pressed_RIGHT:
                moveEye(1, "right")

            ### Screen draws
            # background
            self.pyScreen.blit(self.background, (0, 0))

            # body
            self.robotBody.draw(self.pyScreen)

            # teeth
            for obj in range(len(self.teeth)):
                self.teeth[obj].draw(self.pyScreen)

            # eyes
            for eye in range(len(self.eyes)):
                self.eyes[eye].draw(self.pyScreen)
            
            ### Screen update
            pygame.display.flip()

        ### Terminating pygame
        pygame.quit()


#### Runs the main program
main()

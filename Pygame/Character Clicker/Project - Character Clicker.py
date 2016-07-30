import pygame
import math
import time
import random

# Needed to initialize pygame
pygame.init()

# Define some Constants
BLACK = (0, 0, 0)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)
GREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLUE_SHIRT = (46, 194, 201)
BLUE_JEANS = (64, 92, 200)
SKIN = (250, 209, 137)
SKIN_NOSE = (201, 162, 93)
SKIN_DARK = (79, 58, 23)
    
FPS = 60    #Frames per Second

font = pygame.font.Font(None, 25)

# Manipulated Values ============================================================== SCREEN SIZE
SCREEN_WIDTH = 1100 #96 + 100 (starding cord)
SCREEN_HEIGHT = 720 #192 + 100(starding cord)

# Set the width and height of the screen [width,height]
size = [SCREEN_WIDTH,SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Mansur's Character")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#Loop until the user clicks the close button.
done = False

# Position, scale, and other variables ================================================================ Character position and scale
x = 100
y = 100
size = 1
delta_x = 3
delta_y = 3
charBox_x = 96
charBox_y = 192

clickScore = 0

##########################
file = open("highscores.txt")

background_position = [0,0]

timeLimit = 59
frameCount = 0
frameTotal = timeLimit * FPS

font = pygame.font.Font(None, 32)

clickPos = (False, False, False)

pygame.mixer.music.load("cat.ogg")
pygame.mixer.music.play()

click_sound = pygame.mixer.Sound("Hurt.wav")
miss_sound = pygame.mixer.Sound("Click.wav")

background_image = pygame.image.load("minecraft.jpg").convert()

pointer = pygame.image.load("pointer.png").convert()
pointer.set_colorkey(WHITE)

def drawChar(x, y, scale):
    """ Draws the character """
    # Head
    pygame.draw.rect(screen, SKIN, [x + 24 * scale, y + 0 * scale, 48 * scale, 48 * scale])
    pygame.draw.rect(screen, SKIN_DARK, [x + 24 * scale, y + 0 * scale, 48 * scale, 12 * scale])
    pygame.draw.rect(screen, SKIN_DARK, [x + 24 * scale, y + 12 * scale, 6 * scale, 6 * scale])
    pygame.draw.rect(screen, SKIN_DARK, [x + 66 * scale, y + 12 * scale, 6 * scale, 6 * scale])
    
    pygame.draw.rect(screen, SKIN_DARK, [x + 36 * scale, y + 42 * scale, 24 * scale, 6 * scale])
    pygame.draw.rect(screen, SKIN_DARK, [x + 36 * scale, y + 36 * scale, 6 * scale, 6 * scale])
    pygame.draw.rect(screen, SKIN_DARK, [x + 54 * scale, y + 36 * scale, 6 * scale, 6 * scale])

    # Body
    pygame.draw.rect(screen, BLUE_SHIRT, [x + 0 * scale, y + 48 * scale, 96 * scale, 72 * scale])
    pygame.draw.rect(screen, SKIN, [x + 0 * scale, y + 72 * scale, 24 * scale, 48 * scale])
    pygame.draw.rect(screen, SKIN, [x + 72 * scale, y + 72 * scale, 24 * scale, 48 * scale])
    pygame.draw.rect(screen, (230, 189, 117), [x + 36 * scale, y + 48 * scale, 24 * scale, 6 * scale])
    pygame.draw.rect(screen, (230, 189, 117), [x + 42 * scale, y + 54 * scale, 12 * scale, 6 * scale])

    # legs
    pygame.draw.rect(screen, BLUE_JEANS, [x + 24 * scale, y + 120 * scale, 48 * scale, 72 * scale])
    pygame.draw.rect(screen, (80, 80, 80), [x + 24 * scale, y + 180 * scale, 48 * scale, 12 * scale])
    
    # eyes & nose
    pygame.draw.rect(screen, WHITE, [x + 30 * scale, y + 24 * scale, 12 * scale, 6 * scale])
    pygame.draw.rect(screen, WHITE, [x + 54 * scale, y + 24 * scale, 12 * scale, 6 * scale])
##    pygame.draw.rect(screen, (93, 80, 179), [x + 36 * scale, y + 24 * scale, 6 * scale, 6 * scale])
##    pygame.draw.rect(screen, (93, 80, 179), [x + 54 * scale, y + 24 * scale, 6 * scale, 6 * scale])
    pygame.draw.rect(screen, SKIN_NOSE, [x + 42 * scale, y + 30 * scale, 12 * scale, 6 * scale])

def cPoint(x, y, rect_x, rect_y, rectWidth, rectHeight):
    """ This function checks whether if a point is within a rectangle"""
    if x in range(int(rect_x), (int(rect_x) + rectWidth + 1)) and y in range(int(rect_y), (int(rect_y) + rectHeight + 1)):
        click_sound.play()
        return x, y
    else:
        miss_sound.play()
        return False

def getTimeLeft(frameTotal, frameCount, FPS, font):
    """ get how much time are left, and return it"""
    # Get total seconds
    timeSeconds_total = (frameTotal - frameCount) // FPS

    # get minutes
    timeMinutes = timeSeconds_total // 60

    # get seconds
    timeSeconds = timeSeconds_total % 60

    # asssemble the output string
    timeOutput = "Time left: {0:02}:{1:02}".format(timeMinutes, timeSeconds)

    # Blit the text to the screen
    timeReturn = font.render(timeOutput, True, CYAN)
    
    return (timeSeconds, timeReturn)

def displayScore(clickScore):
    """ displays the score on the screen """
    scoreOutput = "Score: {0:02}".format(clickScore)
    scoreReturn = font.render(scoreOutput, True, CYAN)

    return (scoreReturn)

# Evnet loops
pygame.mouse.set_visible(False)
while done == False:
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            clickPos = pygame.mouse.get_pressed()
            if clickPos[0] == True:
                checkPoint = cPoint(pos[0], pos[1], x, y, (96 * size), (192 * size))
                if checkPoint != False:
                    clickScore += 1
                    if delta_x < 0:
                        delta_x -= 1
                    else:
                        delta_x += 1
                    if delta_y > 0:
                        delta_y += 1
                    else:
                        delta_y -= 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                clickScore -= 10
                if delta_x > 0:
                    delta_x = 3
                elif delta_x < 0:
                    delta_x = -3
                if delta_y > 0:
                    delta_y = 3
                elif delta_y < 3:
                    delta_y = -3
            if event.key == pygame.K_ESCAPE:
                done = True
                
    screen.blit(background_image, background_position)

    timeInfo = getTimeLeft(frameTotal, frameCount, FPS, font)
    scoreInfo = displayScore(clickScore)
    
    if timeInfo[0] == 0:
        done = True
    else:
        screen.blit(timeInfo[1], [920, 10])
        screen.blit(scoreInfo, [10, 10])
    
    # Draws and moves the character
    drawChar(x, y, size)
    x += delta_x
    y += delta_y

    # Makes the character BOUNCE!
    if y > (SCREEN_HEIGHT - (charBox_y * size)) or y < 0:
        delta_y = delta_y  * -1
    if x > (SCREEN_WIDTH - (charBox_x * size)) or x < 0:
        delta_x = delta_x  * -1

    pointer_x = pos[0] - 16
    pointer_y = pos[1] - 16

    screen.blit(pointer, [pointer_x, pointer_y])
    
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
    frameCount += 1

    

    # Limit to FPS frames per second
    clock.tick(FPS)
# -------- End of Main Program Loop --------

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()

print("You got a score of", clickScore)
ask_score = str(input("Would you like to save your name and score? "))
if ask_score.lower() in "nopenahneinfalse":
    exit()
else:
    ask_name = str(input("What is your name? "))

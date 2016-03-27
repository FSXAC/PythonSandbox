import pygame
import math
import time
import random

# Needed to initialize pygame
pygame.init()

# Define some Constants
BLACK = (0, 0, 0)
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

# Position & scale ================================================================ Character position and scale
key_x = 0
key_y = 0
kDelta_x = 0
kDelta_y = 0
x = 100
y = 100
size = 1
delta_x = 3
delta_y = 3
charBox_x = 96
charBox_y = 192
v_rand = [(0, 6), (1, 5), (2, 4), (3, 3), (4, 2), (5, 1), (6, 0),
         (0, -6), (1, -5), (2, -4), (3, -3), (4, -2), (5, -1),
         (-1, 5), (-2, 4), (-3, 3), (-4, 2), (-5, 1), (-6, 0),
         (-1, -5), (-2, -4), (-3, -3), (-4, -2), (-5, -1)]

background_position = [0,0]

clickPos = (False, False, False)

pygame.mixer.music.load("call.mp3")
pygame.mixer.music.play()

background_image = pygame.image.load("stars.jpg").convert()

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
    print(x, y, rect_x, rect_y, rectWidth, rectHeight)
    """ This function checks whether if a point is within a rectangle"""
    if x in range(int(rect_x), (int(rect_x) + rectWidth + 1)) and y in range(int(rect_y), (int(rect_y) + rectHeight + 1)):
        return x, y
    else:
        return False

# Evnet loops
while done == False:
    screen.blit(background_image, background_position)
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
##        if event.type == pygame.KEYDOWN: 
##            if event.key == pygame.K_a:
##                kDelta_y = 0
##                kDelta_x = -3
##            if event.key == pygame.K_d:
##                kDelta_y = 0
##                kDelta_x = 3
##            if event.key == pygame.K_w:
##                kDelta_y = -3
##                kDelta_x = 0
##            if event.key == pygame.K_s:
##                kDelta_y = 3
##                kDelta_x = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            clickPos = pygame.mouse.get_pressed()
            if clickPos[0] == True:
                checkPoint = cPoint(pos[0], pos[1], x, y, (96 * size), (192 * size))
                if checkPoint != False:
##                    if delta_x < 0:
##                        delta_x -= 1
##                    else:
##                        delta_x += 1
##                    if delta_y > 0:
##                        delta_y += 1
##                    else:
##                        delta_y -= 1
                    delta_coord = random.choice(v_rand)
                    delta_x = delta_coord[0]
                    delta_y = delta_coord[1]
            
##        if event.type == pygame.KEYUP:
##            if event.key == pygame.K_a:
##                kDelta_x = 0
##            if event.key == pygame.K_d:
##                kDelta_x = 0
##            if event.key == pygame.K_w:
##                kDelta_y = 0
##            if event.key == pygame.K_s:
##                kDelta_y = 0
                
    screen.blit(background_image, background_position)

    # mouse
##    drawChar(pos[0] - (48 * size), pos[1] - (96 * size), size)

    # keyboard
##    key_x += kDelta_x
##    key_y += kDelta_y
##    drawChar(key_x, key_y, size)

    # Draws and moves the character
    drawChar(x, y, size)
    x += delta_x
    y += delta_y

    # Makes the character BOUNCE!
##    if y > (SCREEN_HEIGHT - (charBox_y * size)) or y < 0:
##        delta_y = delta_y * -1
##    if x > (SCREEN_WIDTH - (charBox_x * size)) or x < 0:
##        delta_x = delta_x  * -1
##
##    if key_y > (SCREEN_HEIGHT - (charBox_y * size)) or key_y < 0:
##        kDelta_y = 0
##    if key_x > (SCREEN_WIDTH - (charBox_x * size)) or key_x < 0:
##        kDelta_x = 0

    # Makes the character WARP around the screen
    if y > (SCREEN_HEIGHT + (charBox_y / 2 * size)):
        y = (0 - (charBox_y * size))
        delta_coord = random.choice(v_rand)
        delta_x = delta_coord[0]
        delta_y = delta_coord[1]
    if y < (0 - (charBox_y * size)):
        y = (SCREEN_HEIGHT + (charBox_y / 2 * size))
        delta_coord = random.choice(v_rand)
        delta_x = delta_coord[0]
        delta_y = delta_coord[1]
    if x > (SCREEN_WIDTH + (charBox_x / 2 * size)):
        x = (0 - (charBox_x * size))
        delta_coord = random.choice(v_rand)
        delta_x = delta_coord[0]
        delta_y = delta_coord[1]
    if x < (0 - (charBox_x * size)):
        x = (SCREEN_WIDTH + (charBox_x / 2 * size))
        delta_coord = random.choice(v_rand)
        delta_x = delta_coord[0]
        delta_y = delta_coord[1]
   
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to FPS frames per second
    clock.tick(FPS)
# -------- End of Main Program Loop --------

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()

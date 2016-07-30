import pygame
import random
import math
import time

# Load pygame engine
pygame.init()

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Frames per second
FPS = 60

# screen settings
screenSize = (1100, 720)
screen = pygame.display.set_mode(screenSize)

pygame.display.set_caption("Helicopter Game")

# imports images
player = pygame.image.load("heli.png").convert()
player.set_colorkey(WHITE)

# draw functions
def drawBlock(x, y):
    """ Draws a simple block """
    pygame.draw.rect(screen, GREEN, [x, y, 32, 128])

def youLose(startTime):
    """ displays death message and time"""
    totalTime = time.time() - startTime
    totalTime = int(totalTime)

text1 = pygame.image.load("text_careful.png").convert()
text1.set_colorkey(WHITE)

# how fast the screen updates
clock = pygame.time.Clock()

# loop until user clicks close button
done = False

# initial constants
x = 100
y = 360
delta_x = -5
delta_y = 0

x_block1 = 1100
x_block2 = 1100 + 250
x_block3 = 1100 + 500
x_block4 = 1100 + 750

y_block1 = random.randrange(720)
y_block2 = random.randrange(720)
y_block3 = random.randrange(720)
y_block4 = random.randrange(720)

startTime = time.time()

# Event and game loop
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                delta_y = -5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                delta_y = 5
                
    # fills the screen black
    screen.fill(BLACK)

    # draws character
    y += delta_y
    screen.blit(player, [x, y])

    x_block1 += delta_x
    x_block2 += delta_x
    x_block3 += delta_x
    x_block4 += delta_x
    
    drawBlock(x_block1, y_block1)
    drawBlock(x_block2, y_block2)
    drawBlock(x_block3, y_block3)
    drawBlock(x_block4, y_block4)
    
    if x_block1 <= -32:
        x_block1 = 1100
        y_block1 = random.randrange(720)
    if x_block2 <= -32:
        x_block2 = 1100
        y_block2 = random.randrange(720)
    if x_block3 <= -32:
        x_block3 = 1100
        y_block3 = random.randrange(720)
    if x_block4 <= -32:
        x_block4 = 1100
        y_block4 = random.randrange(720)

    if x_block1 in range(x, x + player.get_width()) and y_block1 in range(y, y + player.get_height()):
        break
    if x_block2 in range(x, x + player.get_width()) and y_block2 in range(y, y + player.get_height()):
        break
    if x_block3 in range(x, x + player.get_width()) and y_block3 in range(y, y + player.get_height()):
        break
    if x_block4 in range(x, x + player.get_width()) and y_block4 in range(y, y + player.get_height()):
        break
    
    # check if heli is touching the edge
    if y <= 0 or y >= 720:
        break
    
    # updates the screen
    pygame.display.flip()

    # limit to FPS
    clock.tick(FPS)

# unload pygame engine
pygame.quit()

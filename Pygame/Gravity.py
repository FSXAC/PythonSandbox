# Pygame gravity experiment
# Last edited by Mansur

import pygame
import math
import time
import random


# ==== Preperation work ====
# Pygame initialization
pygame.init()

# Color definition
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Frames per second
FPS = 60
# ==== ================ ====


# ==== Screen Settings ====
# Screen Sizes
screen_width = 1100
screen_height = 720

# Set the width and height to the screen
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

# Caption
pygame.display.set_caption("Gravity will pull you down")

# Screen update rates
clock = pygame.time.Clock()

# Loop condition checker
done = False
# ==== =============== ====


# ==== Manipulated variables ====
x = 100
y = 100
scale = 1
delta_x = 5
delta_y = 1
radius = 10

# ==== ===================== ====


# ==== Functions ====
# Function that draws the ball
def draw(x, y, scale = 1):
    """ This draws the object that will be affected by gravity """
    pygame.draw.circle(screen, RED, [x, y], radius * scale, 0)

def cPoint(x, y, rect_x, rect_y, rectWidth, rectHeight):
    """ This function checks whether if a point is within a rectangle"""
    if x in range(int(rect_x), int((rect_x + rectWidth + 1))) and y in range(int(rect_y), int((rect_y + rectHeight + 1))):
        return True
    else:
        return False
# ==== ========= ====


# ==== Event loop ====
while done == False:
    # Event checkings
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
            if cPoint((pygame.mouse.get_pos()[0]), (pygame.mouse.get_pos()[1]),
                   (x - radius), (y - radius), (radius * 2),
                      (radius * 2)) == True:
                delta_y -= 10

    # Screen fills black
    screen.fill(BLACK)


    # ---- Character Manipulation ----
    draw(int(x), int(y), scale)
    

    y += delta_y
    x += delta_x

    delta_y += 0.5
    
    if y >= (screen_height - (radius * scale)) or y <= 0:
        delta_y -= delta_y * 0.5
        delta_y = delta_y * -1
    if x >= (screen_width - (radius * scale)) or x <= 0:
        delta_x -= delta_x * 0.5
        delta_x = delta_x  * -1
    

    
    # ---- ---------------------- ----

    
    # Screen updates
    pygame.display.flip()

    # Limiting to FPS
    clock.tick(FPS)
# ==== ========== ====


# Unloads pygame
pygame.quit()

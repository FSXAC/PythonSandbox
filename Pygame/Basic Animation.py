# importing pygame lib
import pygame
import random
import math

# initialize pygame engine
pygame.init()

# defining colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
blue     = (   0,   0, 255)

# screen settings
size = (700, 500)
screen = pygame.display.set_mode(size)

# sets the title at the top
pygame.display.set_caption("This is a test caption")


# Loop until user click the close button
done = False

# used to manage how fast the screen updates (game tick)
clock = pygame.time.Clock()

# Main program loop
while done == False:
    # Event processing \/
    for event in pygame.event.get():  # user did something
        if event.type == pygame.QUIT: # if user clicks close button
            done = True               # Flag that we are done so we exit this loop
    # Event processing /\

    # Game logic \/

    # Game logic /\

    # Code to draw \/

    # clearing the screen to white, everything above this will be cleared
    screen.fill(black)

    # this draw a GREEN LINE from 0,0 to 700,500 that is 5 pixels wide
    pygame.draw.line(screen,green,[0,0],[500,500],5)

    # drawing a series of lines with WHILE loop
    y_offset = 0
    while y_offset < 100:
        pygame.draw.line(screen,green,[0,10+y_offset],[100,110+y_offset],5)
        y_offset = y_offset+10

    # drawing a series of lines with FOR loop
    for y_offset in range(0,100,10):
        pygame.draw.line(screen,red,[0,10+y_offset],[100,110+y_offset],2)

    # Complex offsets
    screen.fill(black)
    for i in range(200):
     
        radians_x = i/20
        radians_y = i/6
         
        x=int( 75 * math.tan(radians_x)) + random.randrange(195, 210)
        y=int( 75 * math.tan(radians_y)) + random.randrange(195, 210)

        pygame.draw.line(screen,blue,[x,y],[x+3,y], 3)

    for i in range(200):
     
        radians_x = i/20
        radians_y = i/6
         
        x=int( 75 * math.tan(radians_x)) + random.randrange(195, 200)
        y=int( 75 * math.cos(radians_y)) + random.randrange(195, 200)

        pygame.draw.line(screen,red,[x,y],[x+3,y], 3)

    for i in range(200):
     
        radians_x = i/20
        radians_y = i/6
         
        x=int( 75 * math.sin(radians_x)) + random.randrange(195, 200)
        y=int( 75 * math.tan(radians_y)) + random.randrange(195, 200)

        pygame.draw.line(screen,green,[x,y],[x+3,y], 3)
    
    # Code to draw /\

    # Updating the screen with what we've drawn
    
    pygame.display.flip()
    
    # Limit to 30 frams per second
    clock.tick(100)

# close the window and quit
# mustn't forget this line, or else the program will 'hang'
# on exit if running from IDLE
pygame.quit()

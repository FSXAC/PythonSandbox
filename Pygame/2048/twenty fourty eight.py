#### 2048 Python Pygame

#### Imports
import random;
import math;
import pygame;

#### Globalizations
global grid_size;
global grid_spcae;
global grid_margin;

global SCREEN;

#### Public variables
## Grid properties
grid = [];

grid_size = 120;
grid_space = 20;
grid_margin = 40;

box_size = 4 * grid_size + 5 * grid_space

## Pygame initialization
pygame.init();

## Pygame color variables

cBLACK = [0, 0, 0];
cWHITE = [255, 255, 255];
cBACKGROUND = [250, 248, 239];
cBOX = [187, 173, 160];
cGRID = [205, 193, 180];

## Pygame other variables
FPS = 30;

## Pygame window setup
WINDOW_SIZE = [4 * grid_size + 5 * grid_space + 2 * grid_margin, 4 * grid_size + 5 * grid_space + 2 * grid_margin];
SCREEN = pygame.display.set_mode(WINDOW_SIZE);

pygame.display.set_caption("2048");

## Pygame other setups
CLOCK = pygame.time.Clock();

## Pygame loading graphics
n2 = pygame.image.load("number_2.png");
n4 = pygame.image.load("number_4.png");
n8 = pygame.image.load("number_8.png");
n16 = pygame.image.load("number_16.png");

## Loop condition
program_done = False;

#### Functions
## Main grid setup
def gridInit(grid):
    """ This function generates a blank grid of 4 x 4 """;
    for x in range(4):
        grid.append([]);
        for y in range(4):
            grid[x].append(0);

    print("Grid Making Successful");

    numberGen = [2, 2, 2, 2, 4]

    ## Genreate 2 numbers on the grid
    for i in range(2):
        
        randomX = random.randint(0, 3);
        randomY = random.randint(0, 3);

        grid[randomX][randomY] = random.choice(numberGen);

def gridDraw(grid):
    """ This function will render whatever the value is as smaller grids on to the primary grid """
    for column in range(1, 5):
        
        for row in range(1, 5):

            # Cordinates calculation through the formula c = 140p - 80
            cord_x = 140 * row - 80;
            cord_y = 140 * column - 80;
            cord = [cord_x, cord_y];

            value = grid[column - 1][row - 1];
            
            if value == 0:
                pygame.draw.rect(SCREEN, cGRID, [cord_x, cord_y, grid_size, grid_size]);
            elif value == 2:
                SCREEN.blit(n2, cord);
            elif value == 4:
                SCREEN.blit(n4, cord);
            elif value == 8:
                SCREEN.blit(n8, cord);
            elif value == 16:
                SCREEN.blit(n16, cord);

def moveGrid(grid, direction):
    """ This function will move the grid left, right, up or down, and will also add the numbers if grid is adequate """
    if direction == "left":
        for column in range(4):
            for row in range(4):
                if row == 0:
                    if grid[column][range - 1] == 0:
                        test= 0;

    return grid;
#### Main Program setups
gridInit(grid);

grid[0][3] = 4;

#### Main Program Loop
while program_done == False:
    
    ## Events
    for EVENT in pygame.event.get():

        # If event is to quit
        if EVENT.type == pygame.QUIT:
            program_done = True;

        if EVENT.type == pygame.KEYDOWN:
            if EVENT.key == pygame.K_LEFT:
                print("left");

                grid = moveGrid(grid, "left");
                
            elif EVENT.key == pygame.K_RIGHT:
                print("right");
            elif EVENT.key == pygame.K_DOWN:
                print("down");
            elif EVENT.key == pygame.K_UP:
                print("up");

    ## Main Program Actions and Events

    # Color the background
    pygame.draw.rect(SCREEN, cBACKGROUND, [0, 0, WINDOW_SIZE[0], WINDOW_SIZE[1]]);

    # Draws the primary box
    pygame.draw.rect(SCREEN, cBOX, [grid_margin, grid_margin, box_size, box_size]);

    # Draws the 16 smaller rectangles inside the primary box
    gridDraw(grid);

    ## Screen updates
    CLOCK.tick(FPS);
    pygame.display.flip();

#### End of program
pygame.quit();
        

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
    
    game = MainGame()
    game.setFPS(10)
    game.setCaption("Minesweeper")

    # run
    game.run()

# cell class
class Cell():
    
    def __init__(self, pos):
        """ constructor """
        self.cell_pos_x = pos[0]
        self.cell_pos_y = pos[1]
        self.type = 0
        self.scale = 50

        # types:
        # 0 - blank cell
        # 9 - bomb cell
        # 1-8 - number cell

        self.grid_size = (10, 10)

    def getCellPos(self):
        return (self.cell_pos_x, self.cell_pos_y)

    def getType(self):
        return self.type

    def setMine(self):
        self.type = 9

    def setNumber(self, grid_list):
        """ sets number on itself depended on the surrounding numebers """
        
        # only checks if self is not a mine
        if self.type != 9:       
            # check the 8 grids surrounding the grid
            number = 0             
            surround_coords = []

            # for loops that add coords
            for y in range(-1, 2):
                for x in range(-1, 2):
                    surround_coords.append([self.cell_pos_x + x, self.cell_pos_y + y])

            print(surround_coords)
            # check all coords
            for coord in surround_coords:
                
                # if theres a bomb around, then set to that number
                if coord[0] in range(self.grid_size[0]):
                    if coord[1] in range(self.grid_size[1]):
                        if grid_list[coord[0]][coord[1]].getType() == 9:
                            number += 1

            self.type = number
            print("Number set at " + str((self.cell_pos_x, self.cell_pos_y)) + " || " + str(number))

    def draw(self, screen):
        sub = self.type * 25
        pygame.draw.rect(screen, [255 - sub, 255 - sub, 255 - sub],
                        [self.cell_pos_x * self.scale, self.cell_pos_y * self.scale,
                         self.scale, self.scale])
                        
class Minesweeper():
    """ class for the logic of the game """

    def __init__(self, size):
        self.width = size[0]
        self.height = size[1]
        self.grid = []
        self.mines_amount = 10

    def getGrid(self):
        return self.grid
    
    def setMinesAmount(self, new_amount):
        self.mines_amount = new_amount
        
    def start(self):
        # create grids
        for height in range(self.height + 1):
            self.grid.append([])
            for width in range(self.width + 1):
                new_cell = Cell((width, height))
                self.grid[height].append(new_cell)

    def plantMines(self):
        # spawn random bomb
        for i in range(self.mines_amount):
            # create random list of coords where the minewill spawn
            spawn_list = []
            while len(spawn_list) < self.mines_amount:
                random_x = random.randint(0, self.width - 1)
                random_y = random.randint(0, self.height - 1)

                random_coord = (random_x, random_y)

                if random_coord not in spawn_list:
                    spawn_list.append(random_coord)

        # assign random list of coords to mines
        for mine_coord in spawn_list:
            self.grid[mine_coord[0]][mine_coord[1]].setMine()

            print("Mine set at (" + str(mine_coord[0]) + "," + str(mine_coord[1]) + ")")

    def checkGridNumbers(self):
        """ check all cells in the grid """
        for y_list in self.grid:
            for x in y_list:
                x.setNumber(self.grid)

#### MAIN CLASS
class MainGame():
    " main class for the game and its properties"
    
    def __init__(self):
        """ constructor """
        # Setup
        pygame.init()

        # initialize all variables that will be used later
        self.FPS = 1
        self.isFinished = False
        self.scale = 50

        # pygame variables
        self.pyClock = pygame.time.Clock()
        self.pyFont = pygame.font.Font(None, 80)

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
        # game
        self.game_size = (10, 10)
        self.game = Minesweeper(self.game_size)
        self.setScreen((self.game_size[0] * self.scale, self.game_size[1] * self.scale))

        self.game.start()
        self.game.plantMines()
        self.game.checkGridNumbers()
                        

    ### GETTERS and SETTERS
    # Set
    def setFPS(self, fps):
        self.FPS = fps

    def setCaption(self, cap):
        pygame.display.set_caption(cap)

    def setScreen(self, size):
        self.pyScreen = pygame.display.set_mode(size)

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
            for cell_row in self.game.getGrid():
                for cells in cell_row:
                    cells.draw(self.pyScreen)
            
            ### Screen update
            pygame.display.flip()

        ### Terminating pygame
        pygame.quit()        

#### Runs the main program
main()

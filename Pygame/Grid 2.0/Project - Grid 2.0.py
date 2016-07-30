# grid 2.0
# contains clicking and color changing functions

from helLib import *

# colors
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GREEN = [0, 255, 0]
RED =   [255, 0, 0]
BLUE =  [0, 0, 255]
CYAN =  [0, 255, 255]
MAGENTA =   [255, 0, 255]

# other variables
FPS = 15

grid_sidelength = 30
grid_space = 1
grid_repeat = 10

mouse_column = 0
mouse_row = 0

# screen size
screen_side = grid_space + ((grid_space + grid_sidelength) * grid_repeat)
screen_size = [screen_side, screen_side]

# create list of squares
grid = []

for row in range(grid_repeat):
    grid.append([])
    for column in range(grid_repeat):
        grid[row].append(0)

# pygame
pygame.init()

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Grid 2.0")

clock = pygame.time.Clock()

# loop condition
done = False

# main program loop
while done == False:

    mouse_on_row = False
    mouse_on_column = False
    
    # event checking
    for event in pygame.event.get():

        # event checking for quitting
        if event.type == pygame.QUIT:
            done = True

        # event checking for mouse clicking
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            margin_min = grid_space / (grid_space + grid_sidelength)
            
            actual_div_x = mouse_pos[0] / (grid_sidelength + grid_space)
            actual_dec_x = actual_div_x - int(actual_div_x)
            actual_div_y = mouse_pos[1] / (grid_sidelength + grid_space)
            actual_dec_y = actual_div_y - int(actual_div_y)
            
            # find column of mouse
            if actual_dec_x >= margin_min:
                mouse_column = mouse_pos[0] // (grid_sidelength + grid_space)
                mouse_on_column = True

            # find row of mouse
            if actual_dec_y >= margin_min:
                mouse_row = mouse_pos[1] // (grid_sidelength + grid_space)
                mouse_on_row = True

            # set colors everytime its clicked
            if mouse_on_row == True and mouse_on_column == True:
                if grid[mouse_row][mouse_column] == 0:
                    grid[mouse_row][mouse_column] = 1
                elif grid[mouse_row][mouse_column] == 1:
                    grid[mouse_row][mouse_column] = 2
                elif grid[mouse_row][mouse_column] == 2:
                    grid[mouse_row][mouse_column] = 0

    # draws the grid

    screen.fill(BLACK)
    
    for row in range(grid_repeat):
        for column in range(grid_repeat):
            grid_color = WHITE
            if grid[row][column] == 1:
                grid_color = GREEN
            elif grid[row][column] == 2:
                grid_color = RED

            # actually draws them
            pygame.draw.rect(screen,grid_color,[(grid_space + grid_sidelength) * column + grid_space,
                                                (grid_space + grid_sidelength) * row + grid_space,
                                                grid_sidelength, grid_sidelength])

    # screen updates
    clock.tick(FPS)
    pygame.display.flip()

# quit
pygame.quit()



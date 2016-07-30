# Dance Grid

from helLib import *

# starts the pygame
pygame.init()

# get colors
colors = [0, 0, 0] # a place holder for color generation later
colors_list = [[0, 0, 0], [0, 0, 255], [0, 255, 0],
               [0, 255, 255], [255, 0, 0], [255, 0, 255],
               [255, 255, 0], [255, 255, 255]]

FPS = 30

screen_size = (960, 960)

screen = pygame.display.set_mode(screen_size)

pygame.display.set_caption("Grid")

clock = pygame.time.Clock()

done = False

cube_list = []
cube_repeat = 96
cube_size = 8.3

grid_space = 1.7

hyper = False

frameCount = 0

def createCube(cube_list, repeat):
    """ will create a grid of cubes"""
    x = grid_space
    y = grid_space
    for i in range(repeat):
        for i in range(repeat):
            cube_list.append([x, y])
            x += (cube_size + grid_space)
        y += (cube_size + grid_space)
        x = grid_space
    return cube_list

def createColor(colors):
    """ generates random colors """
    for i in range(3):
        colors[i] = (random.randint(0, 255))
    return colors

# new_cube_list will be a list of coords for the cubes
new_cube_list = createCube(cube_list, cube_repeat)

while done == False:
    # event checking
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.mouse.get_pressed():
            mouse_pos = pygame.mouse.get_pos()
        
    screen.fill((0, 0, 0))

    random_colors = createColor(colors)

    # hyper mode
    if hyper == False:
        for i in range(len(new_cube_list)):
            pygame.draw.rect(screen, random_colors, [new_cube_list[i][0], new_cube_list[i][1], cube_size, cube_size])
    else:
        for i in range(len(new_cube_list)):
            pygame.draw.rect(screen, random.choice(colors_list), [new_cube_list[i][0], new_cube_list[i][1], cube_size, cube_size])

    frameCount += 1

    # hyper mode checking
    if frameCount >= 75:
        hyper = True
    if frameCount >= 150:
        hyper = False
        frameCount = 0

    pygame.display.flip()
    clock.tick(FPS)

# closes the game
pygame.quit()

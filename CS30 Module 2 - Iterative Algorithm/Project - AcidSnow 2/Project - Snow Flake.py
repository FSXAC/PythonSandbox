# snow flakes program

from helLib import *


# Function
def createSnow(amount, snow_list, size):
    for i in range(amount):
        new_flake_x = random.randint(0, size[0] - 5)
        new_flake_y = random.randint(0, size[1] - 5)
        snow_list.append([new_flake_x, new_flake_y])

def drawSnow(snow_list, size, color):
    for flake in snow_list:
        pygame.draw.ellipse(screen, color,[flake[0], flake[1], size, size])

def drawChar(position):
    pygame.draw.rect(screen, GREEN, [position[0], position[1], char_size, char_size])

def moveSnow(snow_list, fallspeed):
    for i in range(len(snow_list)):
        if snow_list[i][1] < SCREEN_HEIGHT:
            snow_list[i][1] = snow_list[i][1] + fallspeed
        else:
            snow_list[i][1] = random.randint(-20, 0)
            snow_list[i][0] = random.randint(0, SCREEN_WIDTH - 5)

# constant definitions
## color definitions
BLACK = [0, 0, 0,]
WHITE = [255, 255, 255]
GREY  = [155, 155, 155]
GREEN = [0, 255, 0]

## screen size
SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 720
SIZE = [SCREEN_WIDTH, SCREEN_HEIGHT]

## FPS
FPS = 60

frame_count = 0

## Game loop
loop = True
started = False

# create snow flakes
char_size = 10

snow_flakes = []
snow_flakes_front = []
snow_flakes_back = []

flake_size = 12
flake_size_front = 20
flake_size_back = 10

createSnow(50, snow_flakes, SIZE)
createSnow(10, snow_flakes_front, SIZE)
createSnow(20, snow_flakes_back, SIZE)

# pygame
## engine initialization
pygame.init()

## Score Text
font = pygame.font.Font(None, 50)

## create screen
screen_back = pygame.display.set_mode(SIZE)
screen = pygame.display.set_mode(SIZE)
screen_front = pygame.display.set_mode(SIZE)

pygame.display.set_caption("ACIDSNOW")

## clock
clock = pygame.time.Clock()

while loop == True:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    mouse_pos = pygame.mouse.get_pos()

    # Draw graphics
    screen.fill(BLACK)

    drawChar(mouse_pos)

    drawSnow(snow_flakes_back, flake_size_back, GREY)
    drawSnow(snow_flakes, flake_size, WHITE)
    drawSnow(snow_flakes_front, flake_size_front, WHITE)

    # move the snowflakes
    moveSnow(snow_flakes, 4)
    moveSnow(snow_flakes_front, 8)
    moveSnow(snow_flakes_back, 1)

    mouse_state = [mouse_pos[0], mouse_pos[1], mouse_pos[0] + char_size, mouse_pos[1] + char_size]
    
    if checkCollide(mouse_state, snow_flakes_front, flake_size_front) and started:
        loop = False
    if checkCollide(mouse_state, snow_flakes_back, flake_size_back) and started:
        loop = False
    if checkCollide(mouse_state, snow_flakes, flake_size) and started:
        loop = False

    frame_count += 1
    
    if (frame_count // FPS) >= 3:
        started = True

    new_caption = "ACIDSNOW - Score :" + str(frame_count)
    pygame.display.set_caption(new_caption)

    screen.blit(font.render("Score: " + str(frame_count * 7), True, WHITE), [7, 7])

    # screen update
    pygame.display.flip()

    # frames
    clock.tick(FPS)

## Quit pygame
pygame.quit()

print("You have a score of", frame_count * 7)
input()
    

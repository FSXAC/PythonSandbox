import pygame

white = (255, 255, 255)
black = (0, 0, 0)

pygame.init()

screen = pygame.display.set_mode([800, 600])

pygame.display.set_caption('dammit')

clock = pygame.time.Clock()

click_sound = pygame.mixer.Sound("Click.wav")

background_position = [0,0]

background_image = pygame.image.load("stars.jpg").convert()
player_image = pygame.image.load("food.png").convert()
player_image.set_colorkey(white)

done = False

while done == False:
    clock.tick(30)
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play() 
             
    # Copy image to screen:
    screen.blit(background_image, background_position)
 
    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    player_position = pygame.mouse.get_pos()
    x = player_position[0] - 25
    y = player_position[1] - 25
     
    # Copy image to screen:
    screen.blit(player_image, [x,y])
     
    pygame.display.flip()
    clock.tick(120)
 
pygame.quit ()

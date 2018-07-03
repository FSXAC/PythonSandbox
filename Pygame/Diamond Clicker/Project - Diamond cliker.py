#                 /
# diamond clicker recreation in pygame
# last edited by Mansur

from helLib import *

# colors
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GREEN = [0, 255, 0]
BLUE =  [0, 0, 255]
CYAN =  [0, 255, 255]
MAGENTA =   [255, 0, 255]

# other variables
FPS = 30
screen_size = [1200, 720]

# pygame
pygame.init()
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Diamond Clicker")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 40)
font2 = pygame.font.Font(None, 80)

# game variables
diamonds_total = 0
diamond_rate = 10000

rate_pickaxe = 0.2
rate_turtle = 2.0
rate_generator = 5.0
rate_macerator = 10.0
rate_quarry = 50.0
rate_rocket = 100.0
rate_portal = 150.0
rate_massfab = 200.0
rate_uum = 320.0

cost_pickaxe = 20
cost_turtle = 200
cost_generator = 500
cost_macerator = 1000
cost_quarry = 5000
cost_rocket = 10000
cost_portal = 15000
cost_massfab = 20000
cost_uum = 32000

num_pickaxe = 0
num_turtle = 0
num_generator = 0
num_macerator = 0
num_quarry = 0
num_rocket = 0
num_portal = 0
num_massfab = 0
num_uum = 0

buy_rate = 1.05

clicks_total = 0

done = False

# loadings
# button graphics
pickaxe = pygame.image.load("pickaxe.png").convert()
turtle = pygame.image.load("turtle.png").convert()
generator = pygame.image.load("generator.png").convert()
macerator = pygame.image.load("macerator.png").convert()
quarry = pygame.image.load("quarry.png").convert()
rocket = pygame.image.load("rocket.png").convert()
portal = pygame.image.load("portal.png").convert()
massfab = pygame.image.load("massfab.png").convert()
uum = pygame.image.load("uum.png").convert()

diamond = pygame.image.load("diamond.png").convert()
diamond.set_colorkey(BLACK)

text_back = pygame.image.load("text_back.png").convert()
text_back.set_alpha(50)

back = pygame.image.load("background.jpg").convert()
back_y = 0
back_y2 = -720

# import achievements
##ach_first_diamond = pygame.image.load("first_diamond.png").convert()
##ach_first_rocket = pygame.image.load("first_rocket.png").convert()
##ach_first_generator = pygame.image.load("first_generator.png").convert()
##ach_first_macerator = pygame.image.load("first_macerator.png").convert()
##ach_first_massfab = pygame.image.load("first_massfab.png").convert()
##ach_first_portal = pygame.image.load("first_portal.png").convert()
##ach_first_quarry = pygame.image.load("first_quarry.png").convert()
##ach_first_turtle = pygame.image.load("first_turtle.png").convert()
##ach_ten_pickaxes = pygame.image.load("ten_pickaxes.png").convert()
##ach_first_uum = pygame.image.load("first_uum.png").convert()
##ach_click_3000 = pygame.image.load("click_3000.png").convert()
##ach_click_5000 = pygame.image.load("click_5000.png").convert()
##ach_total_500k = pygame.image.load("total_500k.png").convert()
##ach_total_1m = pygame.image.load("total_1m.png").convert()

# achievement variables
##ach_timer = 90
##ach_y = -64
##
##ach_x = random.randrange(0, 320)
##
##ach_drop_speed = 4
##
##ach_first_diamond_get = False
##ach_click_3000_get = False


# sound
buy_sound = pygame.mixer.Sound("buy.wav")

def checkButton(mouse):
    if mouse[1] in range(0, 80):
        return "pickaxe"
    elif mouse[1] in range(80, 160):
        return "turtle"
    elif mouse[1] in range(160, 240):
        return "generator"
    elif mouse[1] in range(240, 320):
        return "macerator"
    elif mouse[1] in range(320, 400):
        return "quarry"
    elif mouse[1] in range(400, 480):
        return "rocket"
    elif mouse[1] in range(480, 560):
        return "portal"
    elif mouse[1] in range(560, 640):
        return "massfab"
    else:
        return "uum"

def blitCost(cost):
    x = 760
    y = 45
    for item in cost:
        screen.blit(font.render("Cost: {:.0f}".format(item), True, WHITE), [x, y])
        y += 80

while done == False:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            # check clicking on diamond
            if containsPoint(mouse_pos[0], mouse_pos[1], 80, 200, 480, 480) == True:
                diamonds_total += 1
                clicks_total += 1
            # check clicking on the buttons
            if mouse_pos[0] in range(640, 1200):
                button = checkButton(mouse_pos)
                if button == "pickaxe" and diamonds_total >= cost_pickaxe:
                    buy_sound.play()
                    diamonds_total -= cost_pickaxe
                    num_pickaxe += 1
                    cost_pickaxe *= buy_rate
                    diamond_rate += rate_pickaxe
                elif button == "turtle" and diamonds_total >= cost_turtle:
                    buy_sound.play()
                    diamonds_total -= cost_turtle
                    num_turtle += 1
                    cost_turtle *= buy_rate
                    diamond_rate += rate_turtle
                elif button == "generator" and diamonds_total >= cost_generator:
                    buy_sound.play()
                    diamonds_total -= cost_generator
                    num_generator += 1
                    cost_generator *= buy_rate
                    diamond_rate += rate_generator
                elif button == "macerator" and diamonds_total >= cost_macerator:
                    buy_sound.play()
                    diamonds_total -= cost_macerator
                    num_macerator += 1
                    cost_macerator *= buy_rate
                    diamond_rate += rate_macerator
                elif button == "quarry" and diamonds_total >= cost_quarry:
                    buy_sound.play()
                    diamonds_total -= cost_quarry
                    num_quarry += 1
                    cost_quarry *= buy_rate
                    diamond_rate += rate_quarry
                elif button == "rocket" and diamonds_total >= cost_rocket:
                    buy_sound.play()
                    diamonds_total -= cost_rocket
                    num_rocket += 1
                    cost_rocket *= buy_rate
                    diamond_rate += rate_rocket
                elif button == "portal" and diamonds_total >= cost_portal:
                    buy_sound.play()
                    diamonds_total -= cost_portal
                    num_portal += 1
                    cost_portal *= buy_rate
                    diamond_rate += rate_portal
                elif button == "massfab" and diamonds_total >= cost_massfab:
                    buy_sound.play()
                    diamonds_total -= cost_massfab
                    num_massfab += 1
                    cost_massfab *= buy_rate
                    diamond_rate += rate_massfab
                elif button == "uum" and diamonds_total >= cost_uum:
                    buy_sound.play()
                    diamonds_total -= cost_uum
                    num_uum += 1
                    cost_uum *= buy_rate
                    diamond_rate += rate_uum
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                if diamonds_total >= 10:
                    diamond_rate += 0.5
                    diamonds_total -= 10

    diamonds_total += (diamond_rate / FPS)
    
    screen.fill(BLACK)

    screen.blit(back, [0, back_y])
    screen.blit(back, [0, back_y2])

    if back_y >= 720:
        back_y = -720
    else:
        back_y += 5

    if back_y2 >= 720:
        back_y2 = -720
    else:
        back_y2 += 5

    # achievement checker
##    if diamonds_total > 0 and ach_first_diamond_get == False:
##        ach_first_diamond_get = True
##
##    if clicks_total == 3000 and ach_click_3000_get == False:
##        ach_click_3000_get = True

    # render text box
    screen.blit(text_back, [0, 75])

    # render diamond
    screen.blit(diamond, [80, 200])

    # render achievement
##    if ach_first_diamond_get == True:
##        screen.blit(ach_first_diamond, [ach_x , ach_y])
##        ach_y += ach_drop_speed
##        if ach_y == 0:
##            ach_first_diamond_get = False
##
##    if ach_click_3000_get == True:
##        screen.blit(ach_click_3000, [ach_x , ach_y])
##        ach_y += ach_drop_speed
##        if ach_y == 0:
##            ach_click_3000_get = False

    # render text
    screen.blit(font.render("{:,} Diamonds!".format(int(diamonds_total)), True, CYAN), [240, 80])
    screen.blit(font.render("{:.1f}".format(diamond_rate) + " /s", True, CYAN), [240, 120])
    
    # blit button graphics
    screen.blit(pickaxe, [640, 0])
    screen.blit(turtle, [640, 80])
    screen.blit(generator, [640, 160])
    screen.blit(macerator, [640, 240])
    screen.blit(quarry, [640, 320])
    screen.blit(rocket, [640, 400])
    screen.blit(portal, [640, 480])
    screen.blit(massfab, [640, 560])
    screen.blit(uum, [640, 640])

    # render costs
    screen.blit(font.render("Cost: {:.0f}".format(cost_pickaxe), True, WHITE), [760, 45])
    screen.blit(font.render("Cost: {:.0f}".format(cost_turtle), True, WHITE), [760, 125])
    screen.blit(font.render("Cost: {:.0f}".format(cost_generator), True, WHITE), [760, 205])
    screen.blit(font.render("Cost: {:.0f}".format(cost_macerator), True, WHITE), [760, 285])
    screen.blit(font.render("Cost: {:.0f}".format(cost_quarry), True, WHITE), [760, 365])
    screen.blit(font.render("Cost: {:.0f}".format(cost_rocket), True, WHITE), [760, 445])
    screen.blit(font.render("Cost: {:.0f}".format(cost_portal), True, WHITE), [760, 525])
    screen.blit(font.render("Cost: {:.0f}".format(cost_massfab), True, WHITE), [760, 605])
    screen.blit(font.render("Cost: {:.0f}".format(cost_uum), True, WHITE), [760, 685])

    # render amount
    screen.blit(font2.render("{:.0f}".format(num_pickaxe), True, WHITE), [1100, 10])
    screen.blit(font2.render("{:.0f}".format(num_turtle), True, WHITE), [1100, 90])
    screen.blit(font2.render("{:.0f}".format(num_generator), True, WHITE), [1100, 170])
    screen.blit(font2.render("{:.0f}".format(num_macerator), True, WHITE), [1100, 250])
    screen.blit(font2.render("{:.0f}".format(num_quarry), True, WHITE), [1100, 330])
    screen.blit(font2.render("{:.0f}".format(num_rocket), True, WHITE), [1100, 410])
    screen.blit(font2.render("{:.0f}".format(num_portal), True, WHITE), [1100, 490])
    screen.blit(font2.render("{:.0f}".format(num_massfab), True, WHITE), [1100, 570])
    screen.blit(font2.render("{:.0f}".format(num_uum), True, WHITE), [1100, 650]) 
    
    pygame.display.flip()
    
pygame.quit()

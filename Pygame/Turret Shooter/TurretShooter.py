__author__ = 'Mansur'

# Imports
import pygame
import math
import random

# Global variables
global SCREEN_SIZE, CENTERX, CENTERY, FPS, VERSION

SCREEN_SIZE = [1280, 720]
CENTERX, CENTERY = SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] / 2
FPS = 60
VERSION  = "0.2"

class Main:
    def __init__(self):
        game = Game()
        game.setCaption("TurretShooter " + VERSION)
        game.run()

# Main Game
class Game:
    def __init__(self):
        pygame.init()

        # Game functioning variables
        self.running = True
        self.pyclock = pygame.time.Clock()
        self.pyScreen = pygame.display.set_mode(SCREEN_SIZE)

        # Graphic variables
        self.colors = Colors()
        #self.font = pygame.font.Font(None, 30)
        self.font = pygame.font.SysFont("arial", 30)

        # Object variables
        self.allObjectsList = pygame.sprite.Group()
        self.bulletList = pygame.sprite.Group()

        # Gameplay variables
        self.isMouseButtonDown = False
        # length of the aim line
        self.aimRadius = 30

        # Debug variables
        self.isBorderCollidable = False
        self.isDebug = False

        # Add player into the game
        self.allObjectsList.add(Player())

    def run(self):
        """Main Game Loop"""

        # Bullet creation pos
        shootPos = (0, 0)

        while self.running:
            self.pyclock.tick(FPS)

            # Mouse Position
            mousePos = pygame.mouse.get_pos()

            # Events
            for events in pygame.event.get():
                # Exit the game
                if events.type == pygame.QUIT:
                    self.running = False

                # Enable gun
                if events.type == pygame.MOUSEBUTTONDOWN:
                    self.isMouseButtonDown = True

                # Disable gun
                if events.type == pygame.MOUSEBUTTONUP:
                    self.isMouseButtonDown = False

                # Keyboard controls
                if events.type == pygame.KEYDOWN:

                    # Toggle debug
                    if events.key == pygame.K_F1:
                        if self.isDebug: self.isDebug = False
                        else: self.isDebug = True

                    # Toggle collidable borders
                    if events.key == pygame.K_F2:
                        if self.isBorderCollidable: self.isBorderCollidable = False
                        else: self.isBorderCollidable = True

            # Add bullets if the mouse button is down
            if self.isMouseButtonDown:
                newBullet = Bullet(shootPos)
                self.allObjectsList.add(newBullet)
                self.bulletList.add(newBullet)

            # Clears the screen to black
            self.pyScreen.fill(self.colors.black)

            # Draw all objects in the sprites list
            self.allObjectsList.draw(self.pyScreen)

            # Draw extra debug functions
            if self.isDebug:
                # Object count
                self.pyScreen.blit(self.font.render(
                    "E:" + str(len(self.allObjectsList)),
                True, self.colors.white), (20, 20))

            # Update all objects in the sprites list
            self.allObjectsList.update()

            # Calculate where the bullets will be created
            shootPos = self.aim(mousePos)

            # Bullet actions in bullet list
            for bullet in self.bulletList:

                # Delete object if off screen
                if (bullet.rect.x > SCREEN_SIZE[0]) or (bullet.rect.x < 0):
                    if self.isBorderCollidable:
                        bullet.movex *= -1
                    else:
                        self.bulletList.remove(bullet)
                        self.allObjectsList.remove(bullet)
                        print("H border collision", bullet.health)
                if (bullet.rect.y > SCREEN_SIZE[1]) or (bullet.rect.y < 0):
                    if self.isBorderCollidable:
                        bullet.movey *= -1
                    else:
                        self.bulletList.remove(bullet)
                        self.allObjectsList.remove(bullet)
                        print("V border collision", bullet.health)

                # Delete object if decayed
                if bullet.inactive:
                    self.bulletList.remove(bullet)
                    self.allObjectsList.remove(bullet)
                    print("decayed")

                if self.isDebug:
                    # Bullet trails in debug
                    pygame.draw.line(self.pyScreen, self.colors.red,
                                     (bullet.rect.x, bullet.rect.y),
                                     (bullet.rect.x + bullet.movex * 10,
                                      bullet.rect.y + bullet.movey * 10), 1)

            # updates pygame display
            pygame.display.update()

        # stops the engine when the game loop is done
        pygame.quit()

    def aim(self, mousePos):
        """
        draws the red line that helps player to aim based on mouse positon
        :param mousePos: current mouse position
        :return: (int)
        """

        # x and y from current mouse position
        mousex = mousePos[0] - CENTERX
        mousey = mousePos[1] - CENTERY

        # hypotenous
        d = math.sqrt(mousex**2 + mousey**2)

        # math :)
        # if mouse is at the center of the screen, d would be 0
        try:
            dRatio = self.aimRadius / d
        except:
            dRatio = 0

        x = mousex * dRatio + CENTERX
        y = mousey * dRatio + CENTERY

        # new cords that is within the radius (maximum line length complies with aimRadius)
        newPos = (x, y)

        # draws line
        pygame.draw.line(self.pyScreen, self.colors.red, (CENTERX, CENTERY), newPos, 2)

        return newPos

    def setCaption(self, caption):
        """
        Simple sets the caption of the window
        :param caption: caption of the window
        :return: none
        """
        pygame.display.set_caption(caption)

class Colors:
    def __init__(self):
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.dark_blue = (0 ,20 ,50)
        self.diamond = (150, 170, 250)

class Player(pygame.sprite.Sprite):
    """ Main Player Class
    """
    def __init__(self):
        # sprite creation
        super().__init__()

        # setup graphics
        self.image = pygame.Surface([40, 40])
        self.image.fill((0, 150, 0))

        self.rect = self.image.get_rect()

        # setup cordinates
        self.rect.centerx = SCREEN_SIZE[0] / 2
        self.rect.centery = SCREEN_SIZE[1] / 2

        # gameplay variables
        self.health = 100

class Bullet(pygame.sprite.Sprite):
    """ Main bullet class
    """
    def __init__(self, position):
        # sprite creation
        super().__init__()

        self.image = pygame.Surface([3, 3])
        self.image.fill((255, 255, 255))

        self.rect = self.image.get_rect()

        # setup cordinates
        self.rect.centerx = position[0]
        self.rect.centery = position[1]

        # gameplay varables
        self.inaccuracy = 5

        self.inactive = False
        self.decay = 4

        self.health = 255

        # calculate the velocity of the bullet relative to the center of the screen
        self.movex = ((self.rect.centerx - CENTERX + random.randint(-1 * self.inaccuracy,
                                                                    self.inaccuracy)) / 3)
        self.movey = ((self.rect.centery - CENTERY + random.randint(-1 * self.inaccuracy,
                                                                    self.inaccuracy)) / 3)

    def update(self):
        """
        Update the bullet's variables: position, speed, etc.
        :return:
        """

        # move the bullet
        self.rect.centerx += self.movex
        self.rect.centery += self.movey

        # decay the bullet
        if self.health >= self.decay:
            self.health -= self.decay
        else:
            self.inactive = True

        self.image.fill((self.health, self.health, self.health))

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([10, 10])
        self.image.fill((150, 20, 20))

        self.rect = self.image.get_rect()

        self.health = 100

        spawnRange = 300
        # setup position
        #x, y = random.randrange(0 - spawnRange, SCREEN_SIZE[0] + spawnRange), \
        #       random.randRange(0 - spawnRange, SCREEN_SIZE[1] + spawnRange)

        self.rect.centerx, self.rect.centery = random.randrange(0 - spawnRange, SCREEN_SIZE[0] + spawnRange), \
                                               random.randRange(0 - spawnRange, SCREEN_SIZE[1] + spawnRange)

        self.movex = self.rect.centerx - CENTERX
        self.movey = self.rect.centery - CENTERY

    def update(self):
        self.rect.centerx += self.movex
        self.rect.centery += self.movey

    def damage(self, damage):
        self.health -= damage

Main()
__author__ = 'Mansur'
import pygame
import random

class Drone:
    """ Player Class
    """
    def __init__(self):
        self.health = 100
        self.inertia = 10
        self.size = (200, 80)

        self.image = pygame.image.load("drone.png").convert()
        self.image.set_colorkey((255, 255, 255))

        self.x, self.y = 0, 0

        #self.gunSound = pygame.mixer.Sound("gun.ogg")

    def draw(self, screen, mousePosition):
        moveX = (mousePosition[0] - self.x) / self.inertia
        moveY = (mousePosition[1] - self.y) / self.inertia

        self.x += moveX
        self.y += moveY

        screen.blit(self.image, [self.x - self.size[0] / 2, self.y - self.size[1] / 2])

    def shoot(self):
        "Play sound and create bullet sprite"
        #self.gunSound.play()

    def getBulletPosition(self):
        return (self.x + 73, self.y + 12)

    def setRotation(self, direction):
        if direction == "left":
            self.image = pygame.transform.rotate(self.image, -10)
        else:
            self.image = pygame.transform.rotate(self.image, 10)

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # set background color to be a bullet color
        self.image = pygame.Surface([100, 2])
        self.image.fill((random.randrange(200, 255),
                         random.randrange(150, 220),
                         random.randrange(0, 100)))

        self.rect = self.image.get_rect()

        self.moveX = 50
        self.moveY = random.randrange(-5, 5)

    def update(self):
        self.rect.x += self.moveX
        self.rect.y += self.moveY
        self.moveY += 0.5

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # set background image to Harper
        self.image = pygame.image.load("enemy.png").convert()
        self.image.set_colorkey((255, 255, 255))

        self.rect = self.image.get_rect()

        self.rect.x = 1300
        self.rect.y = random.randrange(20, 500)

        self.health = 5
        self.moveY = 0
        self.moveX = random.randrange(-12, -8)
        self.gravity = 0

    def update(self):
        self.rect.x += self.moveX
        self.rect.y += self.moveY
        self.moveY += self.gravity

    def die(self):
        self.gravity = 5
        self.image = pygame.image.load("enemy_dead.png").convert()
        self.image.set_colorkey((255, 255, 255))

class Smoke(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()

        self.color = 200
        self.size = 30

        self.image = pygame.Surface([self.size, self.size])
        self.image.fill((self.color, self.color, self.color))

        self.rect = self.image.get_rect()
        self.rect.x = position[0] - 95
        self.rect.y = position[1] - 20

        self.active = True

    def update(self):
        if self.size > 1:
            self.size -= 1
            self.image = pygame.transform.scale(self.image, (self.size, self.size))
        else:
            self.active = False

class Main:
    def __init__(self):
        global SCREEN_SIZE, FPS, COLORS

        SCREEN_SIZE = [1280, 720]
        FPS = 60
        COLORS = [(255, 0, 0),
                  (0, 255, 0),
                  (0, 0, 255),
                  (255, 255, 0),
                  (255, 0, 255),
                  (0, 255, 255),
                  (255, 255, 255)]

        game = MainGame()
        game.setCaption("Drone Shooter V0.12")

        if (game.run() == 1):
            game.run()

class MainGame:

    def __init__(self):
        pygame.init()

        self.running = True

        # pygame variables
        self.pyClock = pygame.time.Clock()
        self.pyFont = pygame.font.SysFont("arial", 40)
        self.pyScreen = pygame.display.set_mode(SCREEN_SIZE)

        # game background
        # self.background = pygame.image.load("res\\background.jpg").convert()

        # game music
        #pygame.mixer.music.load("whisper.ogg")
        #pygame.mixer.music.play()

        # gameplay objects
        self.player = Drone()
        self.bullet_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.particle_list = pygame.sprite.Group()

        # gameplay variables
        self.score = 0
        self.scoreColor = (255, 255, 255)

        self.returnVal = 0

    def setCaption(self, cap):
        pygame.display.set_caption(cap)

    def run(self):

        # Game states
        isGunFiring = False

        # WHILE RUNNING
        while self.running:
            self.pyClock.tick(FPS)

            # EVENTS
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    self.running = False

                if events.type == pygame.MOUSEBUTTONDOWN:
                    if events.button == 1:
                        isGunFiring = True
                if events.type == pygame.MOUSEBUTTONUP:
                    if events.button == 1:
                        isGunFiring = False

                if events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_ESCAPE:
                        self.running = False
                        self.returnVal = 1

            # Instantaneous Variables
            mousePosition = pygame.mouse.get_pos()
            pygame.transform.rotate(self.pyScreen, 1)

            # Background
            #self.pyScreen.blit(self.background, [0, 0])
            self.pyScreen.fill((0, 20, 50))

            self.pyScreen.blit(self.pyFont.render("Liberal +" + str(self.score), True, self.scoreColor), (20, 20))

            self.particle_list.draw(self.pyScreen)
            self.particle_list.update()

            # Draw Player
            self.player.draw(self.pyScreen, mousePosition)

            # Spawn enemy
            if random.randint(0, 15) == 1:
                self.enemy_list.add(Enemy())

            # Weapon
            if isGunFiring:
                #self.player.shoot()

                bullet = Bullet()
                bulletPosition = self.player.getBulletPosition()

                bullet.rect.x = bulletPosition[0]
                bullet.rect.y = bulletPosition[1]

                self.bullet_list.add(bullet)

            self.particle_list.add(Smoke(self.player.getBulletPosition()))

            self.bullet_list.draw(self.pyScreen)
            self.bullet_list.update()

            self.enemy_list.draw(self.pyScreen)
            self.enemy_list.update()

            # Bullet interatctions
            for bullet in self.bullet_list:

                # collision
                enemy_hit_list = pygame.sprite.spritecollide(bullet, self.enemy_list, False)

                # delete upon collision
                for enemy in enemy_hit_list:
                    self.bullet_list.remove(bullet)

                    if enemy.health > 0:
                        enemy.health -= 1
                    else:
                        enemy.die()

                    self.score += 1
                    self.scoreColor = random.choice(COLORS)

                if bullet.rect.x > SCREEN_SIZE[0]:
                    self.bullet_list.remove(bullet)

            for enemy in self.enemy_list:
                if enemy.rect.y > SCREEN_SIZE[1] or enemy.rect.x < -100:
                    self.enemy_list.remove(enemy)
                    print("bye")

            for smoke in self.particle_list:
                if not smoke.active:
                    self.particle_list.remove(smoke)

            # Update the game screen
            pygame.display.update()

        pygame.quit()

        return self.returnVal
Main()
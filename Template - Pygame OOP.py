#### ESSENTIAL IMPORTS
import pygame

class Main:
    def __init__(self):
        global SCREEN_SIZE, FPS

        SCREEN_SIZE = [1280, 800]
        FPS = 60

        game = MainGame()
        game.setCaption("TEMPLATE")

        game.run()

class MainGame:

    def __init__(self):
        pygame.init()

        self.running = True

        # pygame variables
        self.pyClock = pygame.time.Clock()
        self.pyFont = pygame.font.Font(None, 80)
        self.pyScreen = pygame.display.set_mode(SCREEN_SIZE)

    def setCaption(self, cap):
        pygame.display.set_caption(cap)

    def run(self):

        while self.running:
            self.pyClock.tick(FPS)

            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    self.running = False

            pygame.display.update()

        pygame.quit()

Main()

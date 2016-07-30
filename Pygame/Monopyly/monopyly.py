__author__ = 'Mansur'
import pygame
import random

# Global variables
global SCREEN_SIZE, CENTERX, CENTERY, FPS, VERSION, COLORS

SCREEN_SIZE = [1440, 900]
CENTERX = SCREEN_SIZE[0] / 2
CENTERY = SCREEN_SIZE[1] / 2
FPS = 30
VERSION  = "0.0"
COLORS = {"BLACK" : (0, 0, 0),
          "WHITE" : (255, 255, 255),
          "R" : (255, 0, 0),
          "G" : (0 ,255, 0),
          "B" : (0, 0 ,255),
          "RG" : (255, 255, 0),
          "RB" : (255, 0, 255),
          "GB" : (0, 255, 255)}

class Game:
    def __init__(self):
        pygame.init()

        # 0 = main menu
        # 1 = start menu
        # 2 = game
        # 3 = end game menu
        self.state = 0

        self.pyClock = pygame.time.Clock()
        self.pyScreen = pygame.display.set_mode(SCREEN_SIZE)

        self.font = pygame.font.SysFont("arial", 16)
        self.fontTitle = pygame.font.SysFont("arial", 96)
        self.fontButton = pygame.font.SysFont("arial", 40)

        self.mousePos = 0

    def run(self):
        running = True
        while running:
            print("current state:", self.state)
            if self.state == 0:
                # returns boolean
                # True = start the game > move on to start menu
                # False = quit the game
                proceed = self.mainMenu()
                if proceed:
                    self.state = 1
                    print("0 -> 1")
                else:
                    print("END")
                    running = False
            if self.state == 1:
                # returns boolean
                # True = play the game
                # False = go back to the main menu
                proceed = "self.startMenu"
                if proceed:
                    print("1 -> 2")
                    self.state = 2
                else:
                    print("1 -> 0")
                    self.state = 0
            if self.state == 2:
                # run the game
                proceed = self.runGame()
                # after the game is finished > go to end menu
                # returns int
                # 0 = close program
                # 1 = main menu
                # 2 = proceed to the end screen
                if proceed == 0:
                    print("END")
                    running = False
                elif proceed == 1:
                    print("2 -> 0")
                    self.state = 0
                else:
                    print("2 -> 3")
                    self.state = 3
            if self.state == 3:
                proceed = "self.endMenu"
                # returns boolean
                # True = return to main menu
                # False = quit the game
                if proceed:
                    print("3 -> 0")
                    self.state = 0
                else:
                    print("END")
                    running = False
        pygame.quit()

    def mainMenu(self):
        onMainMenu = True

        # manipulatable values
        button_x1 = 200
        button_x2 = 50
        button_y = 150
        button_h = 100
        button_w = 2

        # calculates the points for the rectangle
        button_p1 = (button_x1, CENTERY + button_y)
        button_p2 = (CENTERX - button_x1 - button_x2, button_h)
        button_p3 = (CENTERX + button_x2, CENTERY + button_y)
        button_p4 = (CENTERX - button_x1 - button_x2, button_h)

        # creates rect objs
        startRect = pygame.Rect(button_p1, button_p2)
        quitRect = pygame.Rect(button_p3, button_p4)

        while onMainMenu:
            # pygame shit
            self.pyClock.tick(FPS)
            self.mousePos = pygame.mouse.get_pos()

            # calculate if mouse position is on button
            if startRect.collidepoint(self.mousePos):
                hoverStart = True
            elif quitRect.collidepoint(self.mousePos):
                hoverQuit = True
            else:
                hoverStart = False
                hoverQuit = False

            # draw shit
            self.pyScreen.fill(COLORS["BLACK"])

            if hoverStart:
                pygame.draw.rect(self.pyScreen, COLORS["WHITE"], quitRect, button_w)
                pygame.draw.rect(self.pyScreen, COLORS["G"], startRect, button_w)
            elif hoverQuit:
                pygame.draw.rect(self.pyScreen, COLORS["WHITE"], startRect, button_w)
                pygame.draw.rect(self.pyScreen, COLORS["R"], quitRect, button_w)
            else:
                pygame.draw.rect(self.pyScreen, COLORS["WHITE"], startRect, button_w)
                pygame.draw.rect(self.pyScreen, COLORS["WHITE"], quitRect, button_w)

            # text

            start = "{:^30}".format("LET'S START")
            quit = "{:^30}".format("QUIT")

            self.pyScreen.blit(self.fontButton.render(start, True, COLORS["RG"]),
                               (startRect.x, startRect.y))
            self.pyScreen.blit(self.fontButton.render(quit, True, COLORS["RG"]),
                               (quitRect.x, quitRect.y))

            pygame.display.update()

            for events in pygame.event.get():
                # Exit the game
                if events.type == pygame.QUIT:
                    self.onMainMenu = False
                    return False

                if events.type == pygame.MOUSEBUTTONDOWN:
                    if hoverQuit:
                        print("QUIT SELECTED")
                        self.onMainMenu = False
                        return False
                    if hoverStart:
                        print("START SELECTED")
                        self.onMainMenu = False
                        return True

    def runGame(self):
        running = True
        while running:
            self.pyClock.tick(FPS)
            self.mousePos = pygame.mouse.get_pos()

            self.pyScreen.fill(COLORS["BLACK"])

            #### Draw here
            self.pyScreen.blit(self.font.render("TEST", True, COLORS["WHITE"]), (20, 20))

            # updates pygame display
            pygame.display.update()

            # events
            for events in pygame.event.get():
                # Exit the game
                if events.type == pygame.QUIT:
                    running = False
                    return 0

                if events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_SPACE:
                        "roll the dice when you can"

                    if events.key == pygame.K_ESCAPE:
                        running = False
                        return 1

game = Game()
game.run()

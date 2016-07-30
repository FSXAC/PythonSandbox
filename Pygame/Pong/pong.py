import pygame

class Main:
    def __init__(self):
        """
        :return: none
        """
        global SCREEN_SIZE, FPS

        SCREEN_SIZE = [1100, 800]
        FPS = 60

        game = MainGame()
        game.setCaption("PeNG")

        game.run()

class Paddle:
    def __init__(self, id, objects):
        """
        :param id: ID of the object in the game
        :return: none
        """
        self.width = 100
        self.height = 10
        self.orientation = 0 # 0 being horizontal, 1 being verticle
        self.type = 0 # 0 being human, 1 being AI
        self.id = id
        self.isVisible = True
        self.isMouseControlled = True

        self.objects = objects

        self.setRail()
        self.paddleRect = pygame.Rect(0, 0, self.width, self.height)

    def draw(self, screen, mousePosition):
        """
        :param screen: pyScreen
        :param mousePosition: mousePosition
        :return: none
        """

        if self.id == "playerPaddle":
            moveX = (mousePosition[0] - self.paddleRect.centerx) / 10

            # set boundaries on the paddle
            if (self.paddleRect.centerx < (self.width / 2)):
                self.paddleRect.centerx = self.width / 2
            elif (self.paddleRect.centerx > 800 - self.width / 2):
                self.paddleRect.centerx = 800 - self.width / 2

            self.paddleRect.y = self.rail

            self.paddleRect.move_ip(moveX, 0)
            pygame.draw.rect(screen, (255, 255, 255), self.paddleRect)

        if self.id == "paddle2":
            # set boundaries on the paddle
            if (self.paddleRect.centerx < (self.width / 2)):
                self.paddleRect.centerx = self.width / 2
            elif (self.paddleRect.centerx > 800 - self.width / 2):
                self.paddleRect.centerx = 800 - self.width / 2

    def setRail(self):
        """
        :return: none
        """
        if self.id == "playerPaddle":
            self.rail = SCREEN_SIZE[1] - 30

        if self.id == "paddle2":
            self.rail = 30

        if self.id == "paddle3":
            self.rail = 30

        if self.id == "paddle4":
            self.rail = SCREEN_SIZE[0] - 30

    def getRect(self):
        return self.paddleRect

class Ball:
    def __init__(self, id = 0):
        """
        :param id: id of the object in the game
        :return: none
        """
        self.id = id
        self.radius = 5
        self.velocity = [0, 10]
        self.position = [400, 400]
        self.mode = 0 #0 being practice, 1 being scored game
        self.isVisible = True
        self.isMouseControlled = False

    def draw(self, screen, collidable_objs):
        """
        :param screen: pygame pyscreen
        :param paddle: list of classes that contains Rect objects
        :return: none
        """
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius)

        # move
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

        for object in collidable_objs:
            if object.getRect().collidepoint(self.position):
                if object.id == "playerGoal":
                    self.velocity[1] *= -1
                if object.id == "playerPaddle":
                    self.velocity[0] = int(100 * ((self.position[0] - object.getRect().centerx) /
                                        object.width / 2) + self.velocity[0])
                    self.velocity[1] *= -1

    def getPosition(self):
        """
        :return:self.position
        """
        return self.position

    def getType(self):
        return "ball"

class Goal:
    def __init__(self, id):
        self.id = id
        self.orientation = 0 #0 being horizontal, 1 being vertical
        self.isVisible = False
        self.isMouseControlled = False

        if self.orientation == 0:
            self.goalRect = pygame.Rect(0, 0, 800, 10)
        else:
            self.goalRect = pygame.Rect(0, 0, 10, 800)

        self.setPosition()

    def setPosition(self):
        if self.id == "playerGoal":
            # player
            self.goalRect.x, self.goalRect.y = 0, 800

    def getRect(self):
        return self.goalRect

class MainGame:

    def __init__(self):
        """
        :return: none
        """

        pygame.init()

        self.running = True

        # pygame variables
        self.pyClock = pygame.time.Clock()
        self.pyFont = pygame.font.Font(None, 80)
        self.pyScreen = pygame.display.set_mode(SCREEN_SIZE)

        self.balls = []

        # adds player paddle and goal detector
        player = Paddle("playerPaddle", self.balls)
        playerGoal = Goal("playerGoal")

        paddle2 = Paddle("paddle2", self.balls)
        paddle3 = Paddle("paddle3", self.balls)
        paddle4 = Paddle("paddle4", self.balls)

        goal2 = Goal("goal2")
        goal3 = Goal("goal3")
        goal4 = Goal("goal4")

        self.objects = [player, playerGoal, paddle2, paddle3, paddle4, goal2, goal3,
                        goal4]
        self.collidable_objs = [player, playerGoal, paddle2, paddle3, paddle4, goal2, goal3,
                        goal4]

        print(self.objects)

    def setCaption(self, cap):
        """
        :param cap: caption
        :return: none
        sets the caption / title of the window
        """
        pygame.display.set_caption(cap)

    def run(self):
        """
        :return: none
        runs the game
        """

        # Run loop
        while self.running:

            # refresh rate
            self.pyClock.tick(FPS)

            # Events
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    self.running = False

                if events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_SPACE:
                        self.balls.append(Ball("ball"))

                    if events.key == pygame.K_DELETE:
                        del self.balls[:]

            # Mouse position stuff
            mousePosition = pygame.mouse.get_pos()
            self.balls.append(Ball("ball"))

            # Hide mouse if it is in game, show when in the menu
            # if mousePosition[0] < 800:
            #     pygame.mouse.set_visible(False)
            # else:
            #     pygame.mouse.set_visible(True)

            # clears the screen to black
            self.pyScreen.fill((0, 0, 0))

            # draws objects
            for object in self.objects:
                if object.isVisible:
                    if object.isMouseControlled:
                        object.draw(self.pyScreen, mousePosition)
                    else:
                        object.draw(self.pyScreen)

            for ball in self.balls:
                ball.draw(self.pyScreen, self.collidable_objs)

            # show side menu
            pygame.draw.rect(self.pyScreen, (150, 150, 150), (800, 0, 300, 800))

            # show / update the screen
            pygame.display.update()

        pygame.quit()

Main()

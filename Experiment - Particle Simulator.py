import random, pygame

class Main:
    def __init__(self):
        #### DISPLAY SETTING

        #### GLOBAL CONSTANTS
        global SCREEN_SIZE
        global FPS_LIMIT

        SCREEN_SIZE = [1280, 800]
        FPS_LIMIT = 60
        self.gravity = 0.5

        #### Setup the game
        game = MainGame(self.gravity)
        game.setFPS(FPS_LIMIT)
        game.setCaption("Particles / Fluid Simulator")

        #### Run the game
        game.run()

class Circle:
    def __init__(self, initialPosition, screen, gravity):
        """
        :param initialPosition: where the circle is to be created
        :param screen: the screen of pygame
        :return: none
        """
        self.screen = screen
        self.radius = random.randint(20, 30)
        self.position = initialPosition
        self.color = random.randint(100, 255)

        # self.speedX = float(random.randint(-20, 20)) * 0.1
        # self.speedY = float(random.randint(-20, 20)) * 0.1
        self.speedX = 5
        self.speedY = 0.2
        self.elasticity = 1
        self.gravity = gravity
        self.growth = 0 #float(randomint(-1, 1))/100

    def draw(self):
        """
        :return:none
        Displays self to the screen
        """

        # Draw the shape
        pygame.draw.circle(self.screen, self.color, self.position, self.radius, 0)

        # Move the object
        self.position[0] = int(self.position[0] + self.speedX)
        self.position[1] = int(self.position[1] + self.speedY)

        self.speedY += self.gravity

        self.radius += self.growth

        # # bounce
        # if ((self.position[0] + self.radius) >= SCREEN_SIZE[0]) or ((self.position[0] - self.radius) <= 0):
        #     self.speedX *= -1
        #     if (self.position[0] <= 0):
        #         self.position[0] = self.radius
        #     else:
        #         self.position[0] = SCREEN_SIZE[0] - self.radius
        #
        # if ((self.position[1] + self.radius) >= SCREEN_SIZE[1]) or ((self.position[1] - self.radius) <= 0):
        #     self.speedY *= -1
        #     if (self.position[1] <= 0):
        #         self.position[1] = self.radius
        #     else:
        #         self.position[1] = SCREEN_SIZE[1] - self.radius

        # destroys itself
        # if (self.position[1] > 2000): del(self)

    def generateRandom(self, lower, upper, factor, exception = []):
        """
        :param lower: Minimum value generated
        :param upper: Maximum balue generated
        :param factor: Multiplied by a factor of...
        :param exception: Generated numbers that are not excepted
        :return: float
        Generates numbers
        """
        number = float(random.randint(lower, upper)) * factor
        while (number in exception):
            float(random.randint(lower, upper)) * factor

        return number

    #### GETTER
    def getPostion(self):
        """
        :return:list
        """
        return self.position

    def getVelocity(self):
        """
        :return:tuple
        """
        return (self.speed_x, self.speed_y)

    #### SETTER
    def setPosition(self, position):
        """
        :param position:list
        :return:none
        """
        self.position = position

class MainGame:
    """Main class for pygame"""

    #### CONSTRUCTOR
    def __init__(self, gravity):
        """Constructor"""

        #### Setup
        pygame.init()

        self.FPS = 1
        self.running = True
        self.addCircle = False
        self.gravity = gravity

        #### Pygame variables
        self.pyClock = pygame.time.Clock()
        self.pyFont = pygame.font.Font(None, 80)
        self.pyScreen = pygame.display.set_mode(SCREEN_SIZE)

        #### COLOR COLLECION
        self.COLORS = {"RED": [255, 0, 0],
                       "BLACK": [0, 0, 0]}

        self.circles = []
        self.circleID = 0

    #### GETTER


    #### SETTER
    def setFPS(self, fps):
        self.FPS = fps

    def setCaption(self, caption):
        pygame.display.set_caption(caption)

    #### MAIN METHOD
    def run(self):

        while self.running:
            self.pyClock.tick(self.FPS)

            #### EVENTS
            for events in pygame.event.get():

                # Close the pygame when the program is quit
                if events.type == pygame.QUIT:
                    self.running = False

                # MOUSE EVENTS
                if events.type == pygame.MOUSEBUTTONDOWN:
                    self.addCircle = True

                if events.type == pygame.MOUSEBUTTONUP:
                    self.addCircle = False

                # KEYBOARD EVENTS
                if events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_SPACE:
                        del self.circles[:]

                    if events.key == pygame.K_g:
                        if self.gravity == 0:
                            self.gravity = 0.5
                        else:
                            self.gravity = 0

                        print(self.gravity)

            #### ADD CIRCLES
            if self.addCircle:
                mousePos = pygame.mouse.get_pos()
                self.circles.append(Circle([mousePos[0], mousePos[1]], self.pyScreen, self.gravity))

            #### SCREEN DRAW
            # Clears the screen
            self.pyScreen.fill(self.COLORS.get("BLACK"))

            # Draws the circle
            for circle in self.circles:
                circle.draw()

            #### SCREEN UPDATE
            pygame.display.flip()


        #### PROGRAM TERMINATION
        pygame.quit()


#### RUNS THE MAIN PROGRAM
Main()

import random


class Player():
    """ player class """
    def __init__(self, name):
        """ constructor """
        
        self.name = name
        self.stat_correct = 0
        self.stat_incorrect = 0
        self.round_pt = 0

    def __str__(self):
        """ return the stats of the player """
        stats = (self.name + " has " + str(self.stat_correct) + " wins and " + str(self.stat_incorrect) + " losses.")
        return stats

    # getters
    def getName(self):
        """ returns name """
        return self.name

    def getRoundPt(self):
        """ returns score for the round game mode """
        return self.round_pt

    # setters
    def increaseCorrect(self):
        """ increase the stat_correct by 1 """
        self.stat_correct += 1

    def increaseIncorrect(self):
        self.stat_incorrect += 1

    def increaseRoundPt(self):
        self.round_pt += 1

    def resetRoundPt(self):
        self.round_pt = 0

# this is responsible for the mathematical logic and function
class MathQuizzer():
    def __init__(self):
        """ constuctor """
        self.operation = "+"

    def askQuestion(self):
        """ ask the question. duh """

        # pick two differt numbers depends on the operation
##        if operation == "/":
##            self.num_2 = random.randint(1, 12)
##            factor = random.randint(1, 10)
##            self.num_1 = int(factor + self.num_2)
##
##        else:
##            self.num_1 = random.randint(0, 12)
##            self.num_2 = random.randint(0, 12)

        self.num_1 = random.randint(0, 12)
        self.num_2 = random.randint(0, 12)
        

        # print qustion here
        print("What is " + str(self.num_1) + " " + self.operation + " "
              + str(self.num_2) + "?")

    def isAnswer(self, user_answer):

        isCorrect = False


        # for different operations, they do different comparisons depends on differnt solution
        if self.operation == "+":
            if user_answer == self.num_1 + self.num_2:
                isCorrect = True
        elif self.operation == "-":
            if user_answer == self.num_1 - self.num_2:
                isCorrect = True
        elif self.operation == "*":
            if user_answer == self.num_1 * self.num_2:
                isCorrect = True
        elif self.operation == "/":
            if user_answer == self.num_1 / self.num_2:
                isCorrect = True
        else:
            print("an error has occured")
        
        return isCorrect

    # sets the operation 
    def setOperation(self, operation):
        self.operation = operation

        

# Vector adding program

class Vector:
    def __init__(self):
        self.position = [0, 0, 0]
        self.vector = [0, 0, 0]

    # setters
    def setPos(self, x, y, z):
        self.position = [x, y, z]

    def setUVec(self, x, y, z):
        self.vector = [x, y, z]

    def getPos(self):
        return self.position

    def getVec(self):
        return self.vector

class Force(Vector):
    def __init__(self, magnitude = 0):
        self.magnitude = magnitude
        self.

def getCommand(userInput):
    # turn input string to a list
    userStream = []
    word = ""

    for index in range(len(userInput)):
        # not the last character
        if (index != len(userInput) - 1):
            if (userInput[index] != " "):
                word += userInput[index]
            else:
                # add word + reset word buffer
                userStream.append(word)
                word = ""
        else:
            # add the last word
            word += userInput[index]
            userStream.append(word.lower())

    return userStream

def main():
    continueSuperLoop = True

    forces = []
    moments = []

    while continueSuperLoop:
        commandStream = getCommand(input(">: "))

        if (commandStream[0]== "add"):
            if (len(commandStream) != 5):
                print("Invalid use of 'add' command.\n")
            else:
                print("Adding: " + commandStream[1] + " with parameters:" +
                      "\nx: " + commandStream[2] +
                      "\ny: " + commandStream[3] +
                      "\nz: " + commandStream[4] + "\n")
        if (commandStream[0] == "quit"):
            continueSuperLoop = False
        else:
            print("'" + commandStream[0] + "' is an invalid command.\n")

main()

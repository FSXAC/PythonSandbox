# vector program

# imports

# vector class
class Vector:
    def __init__(self, vectorID, dimension = -1):
        self.ID = vectorID;
        self.unitVector = [];

        if dimension == -1:
            self.askDimensions();
        else:
            self.dimensions = dimension;

        self.askComponents();

    def askDimensions(self):
        self.dimensions = 0;
        while self.dimensions not in range(1, 10):
            self.dimensions = int(input("Enter a valid dimension: "));

        print("Dimension entered:", self.dimensions);

    def askComponents(self):
        for i in range(self.dimensions):
            self.unitVector.append(int(input("Enter component " +
                                            str(i + 1) + " for vector " + str(self.ID)
                                             + ": ")));

        print(self.unitVector);

    def getDimension(self):
        return self.dimensions;

    def getVector(self):
        return self.unitVector;

# calculator functions
def dotP():
    vector1 = Vector(1);
    vector2 = Vector(2, vector1.getDimension());

    product = 0

    vector1_ = vector1.getVector();
    vector2_ = vector2.getVector();

    for i in range(len(vector1_)):
        product += vector1_[i] * vector2_[i];

    print(product);

def crossP():
    print("NOTE: This only works with 3 dimensions right now")
    vector1 = Vector(1, 3);
    vector2 = Vector(2, 3);

# main function
def main():
    menuChoices = "12345Qq";
    isDone = False;

    while not isDone:
        userInput = "none";

        print("Welcome to Hupert, a vector calculation program that may or may not work");
        print("""\nPlease select an option below:
[1]\tPhysics stuff
[2]\tCross product
[3]\tDot product
[4]\tProjection
[5]\tUnit vector
        \n[Q]\tQUIT""");

        while ((userInput == "") or (userInput not in menuChoices)):
            userInput = input("Enter Option: ");

        print("Choice " + userInput + " selected");

        # choice selection
        if userInput == "1":
            # Physics menu
            "physics()";
        elif userInput == "2":
            # Cross product
            "crossP()";
        elif userInput == "3":
            # Dot product
            dotP();
        else:
            print("Error: you are drunk. 'go home' expected before 'your ass beaten' token")
            isDone = True;

    input("\nPress any key to continue . . .");

main();

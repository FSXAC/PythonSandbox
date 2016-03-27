# MANLAB
# AUTHOR: MANSUR HE
# DATE: 2016-02-07

import math

class Matrix:
    def __init__(self, x, y):
        self.size_x = x
        self.size_y = y
        self.matrix = []

        self.create();
        self.printMat();
        
    def create(self):
        for row in range(self.size_y):
            self.matrix.append([]);
            for col in range(self.size_x):
                self.matrix[row].append(0)

    def printMat(self):
        print("     [\t", end = "");
        
        for row in range(len(self.matrix)):
            for col in self.matrix[row]:
                print(col, end = " ");

            if row != len(self.matrix) - 1:
                print("\n", end = "\t")
            else:
                print("\t]");

def main():
    variables = []
    
    while True:
        # list the existing vars
        for i in variables:
            print(i);

        user = ""
        while user == "":
            user = input(">: ");

        if user == "mkmat":
            # create a new matrix
            x = int(input("new matrix\nwidth >: "))
            y = int(input("height: >: "))
            variables.append(Matrix(x, y));


main()

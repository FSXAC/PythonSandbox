# area and volume calculator
import math
def menu():
    print( \
        """
===================================================================
    [0] Area of a circle
    [1] Area of an ellipse
    [2] Area of an equilateral triangle
    [3] Volume of a cone
    [4] Volume of a sphere
    [5] Arae of an arbitrary triangle
    [6] Solve quadratic in standard form
    [Q] Quit program
===================================================================
        """)
menu()
selection = str(input("Your option: "))
while selection != "Q":
    if selection == "0":
        r = float(input("\nRadius: "))
        A = math.pi * (r ** 2)
        print ("\nThe area of the circle is", A)
    elif selection == "1":
        r1 = float(input("\nRadius 1: "))
        r2 = float(input("Radius 2; "))
        A = math.pi * r1 * r2
        print ("\nThe area of the ellipse is", A)
    elif selection == "2":
        h = float(input("\nHeight: "))
        A = ((h ** 2) * (math.sqrt(3))) / 3
        print("\nThe area of the equilateral triangle is", A)
    elif selection == "3":
        r = float(input("\nRadius: "))
        h = float(input("Height: "))
        V = (math.pi * (r ** 2) * h) / 3
        print("\nThe volume of the cone is", V)
    elif selection == "4":
        r = float(input("\nRadius: "))
        V = (4 * math.pi * (r ** 3)) / 3
        print("\nThe volume of the sphere is", V)
    elif selection == "5":
        a = float(input("\nLength of 'a': "))
        b = float(input("Length of 'b': "))
        C = float(input("Angle of 'C': "))
        A = 0.5 * a * b * (math.sin(C))
        print("\nThe area of the arbitrary triangle is", A)
    elif selection == "6":
        print("\nax^2 + bx + c")
        a = float(input("A: "))
        b = float(input("B: "))
        c = float(input("C: "))
        discriminant = float((b ** 2) - (4 * a * c))
        if discriminant > 0:
            xint1 = ((0 - b) + math.sqrt(discriminant)) / (2 * a)
            xint2 = ((0 - b) - math.sqrt(discriminant)) / (2 * a)
            print("\nThere are 2 solutions in this equation")
            print("x =", xint1, "\tx =", xint2)
        elif discriminant == 0:
            xint1 = ((0 - b) + math.sqrt(discriminant)) / (2 * a)
            print("\nThere is 1 solution in this equation")
            print("x =", xint1)
        elif discriminant < 0:
            print("\nThere is no real solution in this equation")
    else:
        print("That is not a valid input")
    input("\nPress the enter key to continue")
    menu()
    selection = str(input("\nYour option: "))
exit()

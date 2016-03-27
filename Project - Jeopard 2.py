# Fake Jeopardy recreation in python
# didn't work quite so well
# questions not implented yet

from HelLib import *

# LISTS AND VARIABLES

# this is effective if program was ran in cmd window                      ##
os.system("color 0F")                                                       #
os.system("cls")                                                            #
                                                                            #
# default lists                                                             #
grid = []                                                                   #
categories = ["MATH", "SCIENCE", "HISTORY", "INTERNET", "LIFE"]             #
difficulty = ["100", "200", "300", "400", "500"]                            #
                                                                            #
# GUI formats                                                               #
board_mid   = "|--------------------------------------------|"              #
board_sep   = " | "                                                          #
                                                                              ## Creates a new clean board on start
# creates the default grid pad                                               #
for category in range(5):                                                   #
    grid.append([])                                                         #
    money = 100                                                             #
    for diff in range(5):                                                   #
        grid[category].append(money)                                        #
        money += 100                                                        #
                                                                            #
# adds a $ sign in front of every element in the list                       #
for category in grid:                                                       #
    for diff in category:                                                   #
        grid[grid.index(category)][category.index(diff)] = "$"+str(diff)  ##


# the title Just for Fun
title = """
+==+ +==+   =====   +==+ +==+ +=======+ +==+ +==+ +=======+
|   V   |  /  =  \  |  | |  | |   ____| |  | |  | |  ___  |
|       | /  |_|  \ |  |\\|  | |  |      |  | |  | | |___| |
|       | |       | |       | |  +====+ |  | |  | |      _+
|  |V|  | |   =   | |       | +====+  | |  / \  | |  ||  |
|  | |  | |  | |  | |  |\   |  ____|  | |  \\_/  | |  |\  \\
|  | |  | |  | |  | |  | |  | |       | |       | |  | \  |
+==+ +==+ +==+ +==+ +==+ +==+ +=======+ +=======+ +==+ +==+

+==+ +==+ +=======+
|  | |  | |  _____/
|  |_|  | |  |____
|	| |  _____|
|  |=|  | |  |____
|  | |  | |       \\
+==+ +==+ +=======+

LOADING ..."""

# FUNCTIONS
def loading(title):
    """ doesn't actually load, but just for fun """

    load_time = [0.05, 0.1, 0.15, 0.5]    
    load_box = "+=========================================================+"
    load_list = []
    load_str = ""

    for dot in range(57):
        load_list.append(" ")

    for dots in range(57):
        load_str = ""
        
        for load in load_list:
            load_str += load
            
        print(title)
        print(load_box)
        print("|" + load_str + "|")
        print(load_box)

        load_list[dots] = "#"

        time.sleep(random.choice(load_time))
        os.system("cls")

def sorry(original = ""):
    """ prints a random message that will convey the message of "invalid input" """

    # the list of phrases
    msg_list = ["I\'m sorry?", "Pardon?", "I\'m sorry, I didn't quite catch that",
                "I\'m sorry, I don't understand \"" + original + "\"", "\"" + original + "\"" + " is not the answer I\'m looking for",
                "Try again", "Please try again if you don't mind", "I\'m not Google, please do not enter random things here"]

    # prints out the random chosen phrase
    print(random.choice(msg_list))

def start():
    """ asks the user if they want to play directly or read the instruction first """

    done = False

    os.system("cls")
    checkUser = str(input(\
        """
HELLO THERE!

I highly recommend you read the instructions first.

Would you like to read the instruction for this program?

[CHOICE] > """))
    while done == False:
        if str(checkUser).lower() in ["yes", "y", "please", "sure", "fine", "true", "ok"]:
            return_bool = True
            break
        elif str(checkUser).lower() in ["no", "n", "nah", "meh", "false", "nope"]:
            return_bool = False
            print("\n")
            break
        else:
            sorry(checkUser)
            checkUser = str(input("\n[CHOICE] > "))

    return return_bool

def instruction():
    print(\
        """
\nThis is a question answering game
A board will show up and you can pick the category you want to answer
For example, if I want to pick the category of INTERNET for $400
I will enter "Internet 400"
You will be then taken to an answering area
If you get the question right, you will win that amound of money
If you get it wrong, no prize will be given

Have Fun\n""")
    input("Press the Enter Key To Continue")

def getGrid(grid):
    """ prints out the board """
    print(board_mid)
    print("| ", categories[0], " |" + categories[1], "|" + categories[2],
          "|" + categories[3] + "| ", categories[4], board_sep)
    print(board_mid)

    # prints the money from the grid
    for cate in range(len(grid)):
        print("| ", grid[0][cate], board_sep, grid[1][cate], board_sep, grid[2][cate], board_sep,
              grid[3][cate], board_sep, grid[4][cate], board_sep)
        print(board_mid)

def getUserInput(cate_list, diff_list):
    """ Gets user input from the grid """
    
    while True:
        try:
            category, diff = str(input("\n[YOUR CHOICE] > ")).split()
            
            if category.upper() in cate_list and str(diff) in diff_list:
                temp_list = [category, diff]
                break
        except:
            print("That is not a valid input")

    return temp_list

def checkDoneGrid(grid):
    """ Checks if all of the squares in the board is used """
    temp_check = True

    # using for loop to test each element
    for cate in grid:
        for diff in cate:
            if diff != "----":
                temp_check = False
                break
                
    return temp_check

# MAIN PROGRAM

# useless title
loading(title)

# clears the screen if in cmd window
os.system("cls")

# displays instructions if use agreed
if start() == True:
    instruction()

# loop
# if the board is not all filled / used

while checkDoneGrid(grid) == False:

    # clears the screen everytime before the board gets displayed
    os.system("cls")

    # displays the grid
    getGrid(grid)

    # get user input
    input_user = getUserInput(categories, difficulty)
    cate = input_user[0]
    diff = input_user[1]
    del input_user

    # check if user input square is taken or not
    if grid[categories.index(cate.upper())][difficulty.index(diff)] != "----":
        grid[categories.index(cate.upper())][difficulty.index(diff)] = "----"
    else:
        print("This is already taken")

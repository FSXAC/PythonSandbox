import random

money = 0

c_forest_day = ("\a You have spawned in a forest",
                "[1] - Get wood",
                "[2] - Get Food",
                "[3] - Find Shelter",
                "[4] - Explore")

def getName():
    name = str(input("\n>> Please Enter Your Name >> "))
    name = name.title()
    return name

def intro(name):
    print( \
        """
This is a survival game
Collect resources to survive
Gain money to buy upgrades""")
    print("\nGood luck!", name)
    input()

def display_menu(conditions, money):
    print("You have", money, "coins")
    for i in range(len(conditions)):
        print(conditions[i])
    selection = input("\nYour choice: ")
    return selection

display_menu(c_forest_day, money)

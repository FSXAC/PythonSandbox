# Rock paper scissors game
# featuring 3 modes
# last edited by Mansur at 19:17 10/09/2013

# imports
import time
import random
import os

# function defining
def start():
    print("\nRock....")
    time.sleep(0.5)
    print("Paper....")
    time.sleep(0.5)
    print("Scissors....\n")

# intro
print("Welcome to Rock-Paper-Scissors game!\n")

# os.system("mode con: cols=160 lines=78")
os.system("color 1F")

# game loop
while True:

    # declaring important variables
    mode = input("\nPlease select a mode (Noob / Normal / Pro), or 'Q' to quit: ")
    done = False
    g = ("rock", "paper", "scissors")
    no = ("nopestopfalsenahmeh")
    yes = ("yesurefinegoyupyepleaseyeahokay")

    # normal mode loop
    if mode.lower() == "normal":
        while done == False:

            # getting variables
            user = input("\nYour Move? ")
            cpu = random.choice(g)
            user = user.upper()
            cpu = cpu.upper()
            start()
            print("YOU:", user)
            print("CPU:", cpu)

            # comparing mech
            if user == cpu:
                print("IT'S A TIE")
            elif user == "ROCK":
                if cpu == "PAPER":
                    print("YOU LOSE!")
                else:
                    print("YOU WIN!")
                    os.system("start \\\\fs-059\\studuser$\\Gr11\\m.he3\\music\\winlogonsound.wav >nul")
            elif user == "PAPER":
                if cpu == "ROCK":
                    print("YOU WIN!")
                    os.system("start \\\\fs-059\\studuser$\\Gr11\\m.he3\\music\\winlogonsound.wav >nul")
                else:
                    print("YOU LOSE!")
            elif user == "SCISSORS":
                if cpu == "ROCK":
                    print("YOU LOSE!")
                else:
                    print("YOU WIN")
                    os.system("start \\\\fs-059\\studuser$\\Gr11\\m.he3\\music\\winlogonsound.wav >nul")
            else:
                print("THAT IS NOT A VALID MOVE!")

            # choice at the end of each round
            choice = input("\nWould you like to go again? ")
            if choice.lower() in no:
                done = True
            elif choice.lower() in yes:
                None
            else:
                print("Invalid input, choosing 'yes' by default")

    # pro mode loop
    elif mode.lower() == "pro":
        while done == False:
            user = input("\nYour move? ")
            user = user.upper()
            if user == "ROCK":
                cpu = "PAPER"
            elif user == "PAPER":
                cpu = "SCISSORS"
            elif user == "SCISSORS":
                cpu = "ROCK"
            else:
                continue
            start()
            print("YOU:", user)
            print("CPU:", cpu)
            print("YOU LOSE!")
            choice = input("\nWould you like to go again? ")
            if choice.lower() in no:
                done = True
            elif choice.lower() in yes:
                None
            else:
                print("Invalid input, choosing 'yes' by default")

    # noob mode loop
    elif mode.lower() == "noob":
        while done == False:
            user = input("\nYour move? ")
            user = user.upper()
            if user == "ROCK":
                cpu = "SCISSORS"
            elif user == "PAPER":
                cpu = "ROCK"
            elif user == "SCISSORS":
                cpu = "PAPER"
            else:
                continue
            start()
            print("YOU:", user)
            print("CPU:", cpu)
            print("YOU WIN!")
            os.system("start \\\\fs-059\\studuser$\\Gr11\\m.he3\\music\\winlogonsound.wav >nul")
            choice = input("\nWould you like to go again? ")
            if choice.lower() in no:
                done = True
            elif choice.lower() in yes:
                None
            else:
                print("Invalid input, choosing 'yes' by default")

    # choice of quitting the program
    elif mode.lower() == "q":
        break
    else:
        print("Please enter a valid input!\n")

# outro
input("\n\nThanks for playing. Press the enter key to exit")
            

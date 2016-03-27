# OFFENSIVE FORTUNE TELLER
# AUTHOR: MANSUR HE
# LAST EDITED: 2016-01-13
# PURPOSE: GENERATE RANDOM OFFENSIVE STATEMENTS - OFFENSIVE FORTUNE TELLER

import random

def main():
    role = ["a prostitude", "a dyke", "a sex slave", "a terrorist", "a bank robber",
            "a theif", "an outlaw", "a criminal", "a drug addict", "a traitor",
            "a homeless person", "a drug dealer", "a slave", "a cow", "a corpse",
            "a piece of shit", "a fucking loser", "a disgrace to your family",
            "the worst person on Earth", "an anus", "an alien", "a douchebag",
            "Bruce Wayne", "a bitch"]

    prof = ["for ISIS", "for Kony", "for Donald Trump", "as a dictator",
            "on a terrorist plot", "for satan", "on your failing company",
            "for your evil aunt", "as technician", "garbage man", "executioner",
            "for Nazi Germany", "for the cartels", "as a bus driver",
            "as a professor", "to build a nuke", "janitor"]

    location = ["in hell", "at McDonald's for the past 4 years", "on Pluto",
                "at a gay bar", "at Shit McFucking town", "in Detroit", "in deep space",
                "in your parents' basement", "in your closet", "in a bunker",
                "in a treehouse", "on the magic schoolbus"]


    while True:
        print("In", random.randint(5, 25), "years, you are", random.choice(role),
              "working", random.choice(prof), random.choice(location) + ".")

        input()

main()

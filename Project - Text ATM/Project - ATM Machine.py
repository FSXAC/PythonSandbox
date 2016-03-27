#### ATM MACHINE PROGRAM TEXT   ####
#### SEPT 20 2014               ####

import os
import math
import time
import random

import Account
import Admin
import Client

def main():
    """ main methods """

    main_admin = Admin.Admin()
    main_admin.displaySplash()
    main_admin.displayMenu()

main()

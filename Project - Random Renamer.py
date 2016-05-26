#### This program will randomly rename all items in a folder

import os
import random

# random characters
random_chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# ask for size
size = int(input("Name length: "))

# goes through all the files
for filename in os.listdir("."):

    # setup string for final renaming
    rename = ""

    # add random characters
    for i in range(size):
        rename += random_chars[random.randrange(len(random_chars))]
    
    # add extension
    ext = os.path.splitext(filename)[1]
    rename += ext 

    # rename the actual file
    if filename[-3:] != ".py":
        os.rename(filename, rename)

#### This program will rename a folder of files in series of numbers

import os

prefix = str(input("Prefix: "))
start = str(input("Start Offset: "))
suffix = str(input("Suffix: "))

interval = 0

if start != "":
    interval = int(start)

# goes through all the files
for filename in os.listdir("."):

    # setup string for final renaming
    rename = ""

    # add prefix
    if prefix != "":
        rename += prefix
        print("\t" + rename)

    # add number    
    rename += str(interval)
    print("\t" + rename)

    # add suffix
    if suffix != "":
        rename += suffix
        print("\t" + rename)

    # add extension
    ext = os.path.splitext(filename)[1]
    
    rename += ext 
    print("\t" + rename)

    # rename the actual file
    if filename[-3:] != ".py":
        os.rename(filename, rename)

    # count up and move on
    interval += 1

    print(rename)

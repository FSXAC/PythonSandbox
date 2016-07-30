#### Assignment - Linear Search ####
#### Sept 29 2014 ####

def searchFor(key, search_list):
    position = -1
    for i in range(len(search_list)):
        if search_list[i] == key:
            position = i
            break

    return position

def search_while(key, search_list):
    i = 0
    while i < len(search_list) and search_list[i] != key:
        i += 1

    if i < len(search_list):
        return i
    else:
        return -1

def search_2(key, search_list):
    if key in search_list:
        return search_list.index(key)
    else:
        return -1

# list of names
names = []

# ask user
username = str(input("What will your name be? ")).lower()

# open and run through the file
file = open("F:\\CS30\\Python\\Module 2 - Iterative Algorithm\\Assignment - Linear Search\\villans.txt", "r")
for line in file:
    names.append(line.strip().lower())

# close the file
file.close()

if (search(username, names) != -1 and
    search_1(username, names) != -1 and
    search_2(username, names) != -1):
    print("we don’t serve super villain’s here")
else:
    print("hello")

input()

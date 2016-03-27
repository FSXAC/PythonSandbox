# Class lab: doubles an existing list

def doubleList_for(aList):
    """Will take any list and double each part of it, then returns as a list"""
    for i in range(len(aList)):
        aList[i] = aList[i] * 2
    return aList

def doubleList_while(aList):
    """Do the samething as above, except with a while loop"""
    i = 1
    while i <= len(aList):
        aList[i - 1] = aList[i - 1] * 2
        i += 1
    return aList

num_list = [1, 5, 7, 10, 15]
print("Original List:\t\t", num_list)

num_list = doubleList_for(num_list)
print("Doubled (f) List:\t", num_list)

num_list = doubleList_while(num_list)
print("Doubled (w) List:\t", num_list)

input()

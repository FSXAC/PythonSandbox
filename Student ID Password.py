#!python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 19:54:34 2016

@author: Muchen
"""

#Password creator based on student ID


list1 = ["confident","backward","lasso","bless","absent","boarder",
"awesome","pragmatic","aerodynamic","magnetic"]
list2 = [6, 9, 0, 4, 2, 1, 5, 7, 3, 8]
list3 = ["!", "&", "*", "$", "#", "-", "_", "?", ".", ";"]
list4 = [0, 1, 0, 4, 5, 3, 2, 1, 2, 5]

def getPassword(inputID):
    password = ""
    studentID = []

    for char in inputID:
        studentID.append(int(char))
    
    # first digit
    password += list1[studentID[0]]    
    
    # second digit
    password += str(list2[studentID[1]])
    
    # third and forth digit
    try:
        password += list1[abs(list2[studentID[2]] - studentID[3])].upper()
    except:
        ""
    
    # fifth digit
    password += str(foo(studentID[4], list1))
    
    # sixth digit
    password += list3[studentID[5]]
    
    # seventh digit
    password += list1[9 - studentID[6]].upper()
    
    # eighth digit
    password += list1[list4[list2[studentID[7]]]]
    
    return password
    
def foo(number, words):
    value = 0
    for item in words:
        if len(item) < number:
            value += 1
    return value
    
while True:
    userID = input(">")
    userID += "0" * (8 - len(userID))
    print(getPassword(userID))

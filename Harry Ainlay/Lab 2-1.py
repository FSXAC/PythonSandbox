# Intro
print("LOL welcome to my stupid test, you moron!\n\n")
input("Press the enter key to continue")

# Question list
q1 = ("A country under the control of an empire", "colony")
q2 = ("a group of countries under a single authority ruled by a powerful dominant country", "empire")
m1 = ("The minority group in Rwanda that was victimized in the 1994 genocide", "Hutus", "Slaves", "Tutsis", "Plantation workers")
m2 = ("What is British colonial rule over India", "Maharshus Brownus", "Legacy", "Ghandi", "The Raj")
m3 = ("What does NGO stand for?", "Non General Obesity", "Non Governmental Organization", "No Gambling Organization", "Nine Gag Operators")

# Declaring variables
multiDone = False
corrects = 0
qNum = 0

# Multiple choice question 1
print("\n\n\nMultiple Choice 1:", m1[0])
print("a)", m1[1], "\nb)", m1[2], "\nc)", m1[3], "\nd)", m1[4])
response = input("\nAnswer > ")
qNum += 1
if response.lower() == "c":
    print("Correct")
    corrects += 1
else:
    print("Incorrect")
    print("The correct answer is C:", m1[3])

# Multiple choice question 2
print(corrects, "out of", qNum, "questions correct\n\n")
print("Multiple Choice 2:", m2[0])
print("a)", m2[1], "\nb)", m2[2], "\nc)", m2[3], "\nd)", m2[4])
response = input("\nAnswer > ")
qNum += 1
if response.lower() == "d":
    print("Correct")
    corrects += 1
else:
    print("Incorrect")
    print("The correct answer is D:", m2[4])

# Multiple choice question 3
print(corrects, "out of", qNum, "questions correct\n\n")
print("Multiple Choice 3:", m3[0])
print("a)", m3[1], "\nb)", m3[2], "\nc)", m3[3], "\nd)", m3[4])
response = input("\nAnswer > ")
qNum += 1
if response.lower() == "b":
    print("Correct")
    corrects += 1
else:
    print("Incorrect")
    print("The correct answer is B:", m3[2])

# Short answer question 1
print(corrects, "out of", qNum, "questions correct\n\n")
print("Short Answer 1:", q1[0])
response = input("\nAnswer > ")
qNum += 1
if response.lower() == q1[1]:
    print("Correct")
    corrects += 1
else:
    print("Incorrect")
    print("The correct answer is:", q1[1])

# Short answer question 2
print(corrects, "out of", qNum, "questions correct\n\n")
print("Short Answer 2:", q2[0])
response = input("\nAnswer > ")
qNum += 1
if response.lower() == q2[1]:
    print("Correct")
    corrects += 1
else:
    print("Incorrect")
    print("The correct answer is:", q2[1])

# End of quiz, mark calculator
perc = float((corrects / qNum) * 100)

# Mark displayer
print("\n\n\nThe quiz is now finished!")
print("You got", corrects, "out of", qNum,", which is", perc, "percent")
if perc < 50:
    print("\nYou are a failure!")
elif perc < 100:
    print("\nNot too shabby")
else:
    print("\nAmazing, I call hacks")

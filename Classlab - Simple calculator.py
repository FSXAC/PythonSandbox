# Simple calculator

# functions
def getOp():
    ops = input("Select operator (+ , - , * , /), or enter 'Q' to quit: ")
    while ops not in "+-*/qQ":
        print("Not a valid input, you dumbass!")
        ops = input("Select operator (+ , - , * , /), or enter 'Q' to quit: ")
    return ops

def getInput(prompt):
    done = False
    while done == False:
        userInput = input(prompt)
        try:
            userInput = float(userInput)
            done = True
        except:
            None
    return userInput
    
def calculate(ops, firstNum, secondNum): # This uses operation, and 2 numbers ad get an answer
    if ops == "+":
        print("\nAnswer >", firstNum + secondNum) # then the answer is outputted
    elif ops == "-":
        print("\nAnswer >", firstNum - secondNum)
    elif ops == "*":
        print("\nAnswer >", firstNum * secondNum)
    elif ops == "/":
        try:
            print("\nAnswer >", firstNum / secondNum)
        except:
            print("Cannot divide by zero!")

# displaying intro
print("Welcome to my calculator. You monster!\n")

# get numbers, process & output loop
ops = None
while True:
    ops = getOp()
    if ops in "qQ": # if the input is Q then the program will quit
        break
    
    firstNum = getInput("First Nunber > ") 
    secondNum = getInput("Second Number > ")
    
    calculate(ops, firstNum, secondNum)
    ops = input("\nSelect operator (+ , - , * , /), or enter 'Q' to quit: ")

# end of loop
input("\nFuck you for quitting this calculator.")
    

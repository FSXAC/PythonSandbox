#### Project - Automatic number guesser using binary search ####
#### 2014 - 09 - 30 ####

# guess an number that is between 0 and 4294967296 (2^32) (32 bit)

def main():
    while True:
        guess = Guesser()
        guess.guess(guess.askNumber())

    
class Guesser():
    def __init__(self):
        ""

    def askNumber(self):
        loop = True
        while loop:
            input_number = input("Enter a number between 0 and 4294967296: ")
            try:
                number = int(input_number)
                loop = False
            except:
                print("What the heck is this!?")

        return number
        
    def guess(self, number):
        lower = 0
        upper = 4294967296
        correct = False
        tries = 0

        while lower <= upper and not correct:
            guess = (lower + upper) // 2
            tries += 1
            if guess < number:
                lower = guess + 1
            elif guess > number:
                upper = guess - 1
            else:
                correct = True

            print("\n==== Trial " + str(tries) + " ====\nguess: " + str(guess))
            #print("lower: " + str(lower) + "\nupper: " + str(upper))

        if correct:
            print("\n\n" + str(guess))
                
main()

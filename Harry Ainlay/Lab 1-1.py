# temperature converter

done = False

while done == False:
    a = input("Enter the temperature unit(C/F), or Q to quit: ")
    if a == "Q" or a == "q":
        exit()
        
    b = float(input("Enter the temperature: "))
    
    c = 0
    
    if a.lower() == "c":
        c = (b * 1.8) + 32
        print (c, "degrees fahrenheit\n")
    elif a.lower() == "f":
        c = (b - 32) / 1.8
        print (c, "degrees celcius\n")
    else:
        print("That is not a valid input")

    

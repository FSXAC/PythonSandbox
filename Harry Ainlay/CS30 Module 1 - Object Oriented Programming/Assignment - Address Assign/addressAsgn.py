# Defining Classes Assignment - Addresses
#
# This program imports an Address class that students will have to code in order
# for the program to function.  The program asks the user for their address,
# generates a number of fake addresses, and then randomly chooses an address to
# win a prize.
#
# Mr. V  August 2014

import random, time
from addressClass import Address

def main():
    """ Main function"""

    # Initialization - Generate some fake addresses and add to an addressList
    addressList = []

    fakeAd1 = Address("Humpty Dumpty", "24 Sunnyside St.", "Kingstown", "AB", "T7R 532")
    addressList.append(fakeAd1)
    
    fakeAd2 = Address("Pink Panther", "42 Dead Ant St.", "Clouseaville", "AB", "T6V 293")
    addressList.append(fakeAd2)

    # Ask the user for address information, add them to the addressList and tell them they're in a draw for a prize
    name = input("Please enter your full name: ")
    strAddress = input("Please enter your street address: ")
    city = input("Please enter your city: ")
    province = input("Please enter your province: ")
    postalCode = input("Please enter your postal code: ")

    print("Thank you for your address.  You have been automatically entered into a draw for a grand prize!")

    userAd = Address(name, strAddress, city, province, postalCode)
    addressList.append(userAd)

    # Randomly draw for a prize by generating a random index for addressList
    
    winIndex = random.randrange(0,len(addressList))
    print()
    print("The winner of the grand prize is...")
    time.sleep(2)

    winnerAddress = addressList[winIndex]
    print(winnerAddress)    # Printing the address object will call the __str__ method
    print()
    print("Congratulations", winnerAddress.getName(), "you have won a N64!")
    
# end main()


# Call main() to begin program
main()

    
    

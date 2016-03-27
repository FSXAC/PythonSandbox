# ASCII Encryption

def encrypt(msg):
    """ This Function will encrypt a message"""

    ecry_msg = "";

    for char in msg:
        ord_v = ord(char);
        ord_v += 10;
        ecry_msg += chr(ord_v);

    return ecry_msg;

def decrypt(msg):
    """ This function will decrypt the input message """

    dcry_msg = "";

    for char in msg:
        ord_v = ord(char);
        ord_v -= 10;
        dcry_msg += chr(ord_v);

    return dcry_msg;

done = False;

while done == False:
    ask = input("Do you want to [Encrypt] or [Decrypt] a message? ");
    if ask.lower() == "encrypt" or ask.lower() == "e":
        print(encrypt(str(input("\nPlease Enter Your Message: "))), "\n");
    elif ask.lower() == "decrypt" or ask.lower() == "d":
        print(decrypt(str(input("\nPlease Enter Encrypted Message: "))), "\n");
    elif ask.lower() == "quit" or ask.lower() == "q":
        done = True;
    else:
        print("Invalid Option");
        ask = input("\nDo you want to [Encrypt] or [Decrypt] a message? ");
        
        

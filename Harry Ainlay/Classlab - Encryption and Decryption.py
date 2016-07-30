# encryption
import random

alphabet = "abcdefghijklmnopqrstuvwxyz";

cipher_list = ["qwertyuiopasdfghjklzxcvbnm",
               "plmoknijbuhvygctfxrdzeswaq",
               "qplazmwoksnxiejdcbruhfvtyg",
               "zyxwvutsrqponmlkjihgfedcba"];
cipher = random.choice(cipher_list);
ecry_msg = "";
dcry_msg = "";

user_msg = str(input("Enter a message to encrypt: "));

for char in user_msg:
    if char == " ":
        ecry_msg += char;
    elif char in "1234567890":
        None;
    else:
        char_pos = alphabet.index(char);
        ecry_msg += cipher[char_pos];

for char in ecry_msg:
    if char == " ":
        dcry_msg += char;
    elif char in "1234567890":
        None;
    else:
        char_pos = cipher.index(char);
        dcry_msg += alphabet[char_pos];

print(ecry_msg);
print(dcry_msg);

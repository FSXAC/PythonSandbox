# Anagram Generator

from helLib import *

def get_word(message):
    while True:
        word = input(message)
        if " " in word:
            falseInput("<<< PLEASE ONLY ENTER ONE WORD >>>")
            None
        else:
            break
    return word

user_word = get_word("Enter a word: ")
a = []
b = []
for i in range(len(user_word)):
    a.append(user_word[i])

for i in a:
    b.append(random.choice(a))

for i in b:
    print(i ,) \
    

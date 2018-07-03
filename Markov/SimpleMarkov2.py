"""
This the second prototype with a bit more space optimization
and a bunch of more extra features...

By Muchen He
On 2018-06-30
"""

import random
import sys

defaultFile = './test_quotes.txt'

punctuations = '!\'":;.,?-()'
symbols = '@#$%^&*_+=[]\{\}\\/<>'

def readFile(fname, removeLines=False):
    with open(fname, 'r', encoding='utf8') as f:
        if removeLines:
            content = f.read().replace('\r', '').replace('\n', ' ')
        else:
            content = f.read()
        return content
    return None

def removePunctuations(string):
    newString = ''
    for char in string:
        if char not in punctuations:
            newString += char

    return newString

def buildChain(text, chain={}):
    words = text.split(' ')
    index = 1
    for word in words[index:]:
        key = removePunctuations(words[index - 1]).lower()
        if key in chain:
            chain[key].append(word)
        else:
            chain[key] = {word: 1}

if __name__ == '__main__':
    if len(sys.argv) > 1:
        "Use file from argument"
    else:
        "Use default file"
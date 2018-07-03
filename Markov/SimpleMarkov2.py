"""
This the second prototype with a bit more space optimization
and a bunch of more extra features...

By Muchen He
On 2018-06-30
"""

import random
import sys

defaultFile = './test_quotes.txt'

punctuations = '!\'":;.,?()[]\{\}'
symbols = '@#$%^&*_+=\\/<>'

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

	def addToChain(key, token, chain):
		if key in chain:
			tokenList = chain[key]['token']
			if token in tokenList:
				index = tokenList.index(token)
				chain[key]['weight'][index] += 1
			else:
				tokenList.append(token)
				chain[key]['weight'].append(1)
		else:
			chain[key] = {
				'token': [token],
				'weight': [1]
			}

	tokens = text.split(' ')
	index = 1

	for token in tokens[index:]:
		if len(token) < 1:
			continue

		word = removePunctuations(token.lower())

		# Check for token edge cases
		# Token start with punctuation (i.e. "Hello)
		if token[0] in punctuations:
			addToChain(token[0], word, chain)

		# Token end with punctuation (i.e. Hello")
		if len(word) >= 3:
			if token[-1] in punctuations:
				addToChain(word, token[-1], chain)
		
		# Token end with multiple punctuation (i.e. "Hello!" or "Hello".)
		if len(word) >= 4:
			if token[-2] in punctuations and token[-1] in punctuations:
				addToChain(token[-2], token[-1], chain)
			elif token[-2] in punctuations:
				addToChain(word, token[-2], chain)
			elif token[-1] in punctuations:
				addToChain(word, token[-1], chain)
		
		
		key = removePunctuations(tokens[index - 1].lower())
		addToChain(key, word, chain)
		index += 1

	return chain

def generate(chain, maxLength):
	currentWord = random.choice(list(chain.keys()))
	message = currentWord.capitalize()
	length = 1

	while length < maxLength:
		if currentWord not in chain:
			currentWord = random.choice(list(chain.keys()))
			continue
		
		newWord = random.choices(
			chain[currentWord]['token'], weights=chain[currentWord]['weight'], k=1)[0]
		currentWord = newWord
		message += ' ' + currentWord

		if currentWord in '.!':
			break
		else:
			length += 1
	
	message = message.replace('\n', ' ')
	return message

if __name__ == '__main__':
	if len(sys.argv) > 1:
		"Use file from argument"
		chain = buildChain(readFile(sys.argv[1], removeLines=True))
		while input() != 'q':
			print(generate(chain, random.randint(20, 50)))
	else:
		"Use default file"

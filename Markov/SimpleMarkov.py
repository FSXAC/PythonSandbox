import random
import sys

def readFile(fname, removeLines = False):
	with open(fname, 'r', encoding='utf8') as f:
		if removeLines:
			content = f.read().replace('/r/n', ' ')
		else:
			content = f.read()
		return content

def buildChain(text, chain = {}):
	words = text.split(' ')
	index = 1
	for word in words[index:]:
		key = words[index - 1]
		if key in chain:
			chain[key].append(word)
		else:
			chain[key] = [word]
		
		index += 1

	return chain

def generate(chain, count):
	currentWord = random.choice(list(chain.keys()))
	message = currentWord.capitalize()
	length = 1

	while length < count:
		if currentWord not in chain:
			currentWord = random.choice(list(chain.keys()))
			continue

		newWord = random.choice(chain[currentWord])
		currentWord = newWord
		message += ' ' + currentWord
		length += 1

	message += '.'
	message = message.replace('\n', ' ')

	return message

if __name__ == '__main__':
	chain = buildChain(readFile(sys.argv[1], removeLines=False))

	while input() != 'q':
		print(generate(chain, random.randint(5, 15)))

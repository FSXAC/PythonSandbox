# Dictionary Assignment Class
# Mr. V

import time

class Main():
    """ main program - includes menu and stuff """
    def __init__(self):
        # loads the dictionary
        self.search = SearchTools(self.loadDictionary())

    def run(self):
        main_loop = True
        while main_loop:
            print("""
Dictionary Menu:
[1]\tCheck a word
[2]\tSpell chekc a document (Linear)
[3]\tSpell check a document (Binary)
[4]\tExit""")
            selection = input("Please enter a number from the menu above: ")

            if selection == "1":
                self.search.checkWord()

            elif selection == "2":
                self.search.checkDoc(False)

            elif selection == "3":
                self.search.checkDoc(True)

            elif selection == "4":
                input("Goodbye")
                main_loop = False
            else:
                print("Invalid Selection")


    def loadDictionary(self):
        """ Load dictionary file into a list.  Return the list."""
        word_list = []
        
        file = open("dictionary.txt","r")

        # Add the word on each line into wordList
        for line in file:
            line = line.strip()
            word_list.append(line)

        file.close()

        return word_list

class SearchTools():
    """ this will contain all the functions about seaching """

    def __init__(self, word_list):
        """ constructor """
        self.word_list = word_list

    ## Linear search methods
    def searchLinearFor(self, key, search_list):
        """ search fucntion using linear search algorithms """
        position = -1
        for i in range(len(search_list)):
            if search_list[i] == key:
                position = i
                break
        return position

    def searchBinaryFor(self, key, search_list):
        """ search function that uses binary search algorithms """
        lower_bound = 0
        upper_bound = len(search_list) - 1
        position = -1
        while lower_bound <= upper_bound and not position != -1:
            search_pos = (lower_bound + upper_bound) // 2
            if search_list[search_pos] < key:
                lower_bound = search_pos + 1
            elif search_list[search_pos] > key:
                upper_bound = search_pos - 1
            else:
                position = search_pos

        return position
        
    
    def checkWord(self):
        """ check a single word to see if its inside the dictionary list """
        input_word = str(input("\nEnter a word: ")).upper()
        #if self.searchLinearFor(input_word, self.word_list) != -1:
        time_start = time.clock()
        if self.searchBinaryFor(input_word, self.word_list) != -1:
            print("\nYour word is valid, it is at position " + str(self.word_list.index(input_word)))
        else:
            print("\nYour word does not exist")
        time_end = time.clock()
        print(str(time_end - time_start) + " seconds elapsed to search the word")

    def checkDoc(self, isBinary):
        """ spell checks an entire document """
        # ask for file name
        file_name = input("\nEnter file directory: ") + ".txt".lower()

        # variables
        docIsOpen = False

        # lists
        lines = []
        words = []
        words_invalid = []

        # try to open the file
        while docIsOpen == False:
            try:
                doc = open(file_name)
                docIsOpen = True
            except:
                file_name = input("File directory does not exist.\nEnter file directory: ") + ".txt"

        # put all lines from a document into the list
        for line in doc:
            lines.append(line.strip())

        # put all lines from the list into words
        for i in lines:
            temp_words = i.split()
            for word in temp_words:
                words.append(word.upper())

        # check all words
        time_start = time.clock()
        for word in words:
            if isBinary:
                if self.searchBinaryFor(word.upper(), self.word_list) == -1:
                    words_invalid.append(word)
            else:  
                if self.searchLinearFor(word.upper(), self.word_list) == -1:
                    words_invalid.append(word)

        time_end = time.clock()

        # final output
        if words:
            #print("There are " + str(len(words_invalid)) + " incorrectly spelt words\nThey are:")
            #for word in words:
            #    print(word)
            print("There are " + str(len(words_invalid)) + " unregistered words.")
        else:
            print("All words are correct.")

        print(str(time_end - time_start) + " seconds elapsed to search the entire document")

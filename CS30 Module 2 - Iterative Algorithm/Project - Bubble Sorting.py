#### Project - Bubble Sort ####
#### 2014 - 10 - 06 ####

import random
import time

def main():
    sorter = Sorter()
    sorter.sort(generateRandomNumber())
    input()

def generateRandomNumber():
    random_list = []
    user_list = input("Custom List: ").split()

    # if user enters custom list
    if user_list:
        for n in user_list:
            user_list[user_list.index(n)] = int(n)

        return user_list
    
    else:
        # generate a random list
        for i in range(10):
            random_list.append(random.randint(1, 50))

        return random_list

class Sorter():
    def __init__(self):
        self.list = []

    def sort(self, sort_list):
        loop_interval = len(sort_list)

        print("unsorted:\t" + str(sort_list))

        # main sort
        time_start = time.clock()
        while loop_interval > 0:
            for i in range(loop_interval - 1):
                
                # compare if the second number is larger than the first one
                if sort_list[i] > sort_list[i + 1]:
                    temp_value = sort_list[i]
                    sort_list[i] = sort_list[i + 1]
                    sort_list[i + 1] = temp_value

            loop_interval -= 1

        time_end = time.clock() - time_start
        print("sorted:\t\t" + str(sort_list))
        print(time_end)
main()

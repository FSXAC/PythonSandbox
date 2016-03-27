class Score():

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return self.name + ", " + str(self.score) + "Pt"

    def getName(self):
        return self.name

    def getScore(self):
        return self.score
    
def main():

    # all scores
    scores = []
    
    # open file
    file = open("score.txt")

    for line in file:
        profile = line.strip().split("%")
        name = profile[0]
        score = int(profile[1])
        scores.append(Score(name, score))

    file.close()

    # sort by name
    loop_interval = len(scores)
    while loop_interval > 0:
        maximum = None
        maximum_pos = 0
        maximum_name = ""
        
        for i in range(loop_interval):
            # find the biggest number
            if scores[i].getName() > maximum_name:
                maximum = scores[i]
                maximum_name = scores[i].getName()
                maximum_pos = i               

        # swap
        temp = scores[maximum_pos]
        scores[maximum_pos] = scores[loop_interval - 1]
        scores[loop_interval - 1] = maximum

        loop_interval -= 1

    print("=== sort by name ===")
    for i in scores:
        print(i)
    input()

    # sort by score
    loop_interval = len(scores)
    while loop_interval > 0:
        maximum = None
        maximum_pos = 0
        maximum_score = 2e16
        
        for i in range(loop_interval):
            # find the biggest number
            if scores[i].getScore() < maximum_score:
                maximum = scores[i]
                maximum_score = scores[i].getScore()
                maximum_pos = i               

        # swap
        temp = scores[maximum_pos]
        scores[maximum_pos] = scores[loop_interval - 1]
        scores[loop_interval - 1] = maximum

        loop_interval -= 1

    print("=== sort by score ===")
    for i in scores:
        print(i)

    input()
    
main()

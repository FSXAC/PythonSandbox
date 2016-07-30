class Character():

    def __init__(self, initName):
        self.name = initName
        self.health = 20
        self.numVictories = 0

    def __str__(self):
        return_str = self.name + "\t||    " + str(self.health) + " HP    ||    " + str(self.numVictories) + " wins"
        return return_str

    def getName(self):
        return self.name

    def strongAttack(self):
        self.health -= 5

    def quickAttack(self):
        self.health -= 2

    def isDead(self):
        if self.health <= 0:
            return True
        else:
            return False

    def addVictory(self):
        self.numVictories += 1

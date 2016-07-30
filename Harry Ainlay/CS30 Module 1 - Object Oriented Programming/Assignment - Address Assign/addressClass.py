class Address:
    def __init__(self, initName, initStrAddress, initCity, initProv, initPC):
        self.name = initName
        self.strAddress = initStrAddress
        self.city = initCity
        self.province = initProv
        self.postalCode = initPC

    def __str__(self):
        return self.getName()

    def getName(self):
        return self.name

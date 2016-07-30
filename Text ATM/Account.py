#### ATM MACHINE PROGRAM TEXT ACCOUNT CLASS  ####
#### SEPT 25 2014                            ####

class Account(): 
    def __init__(self, account_number):
        
        self.cannot_change = "Sorry sir, we cannot change that for you"
        self.info_dir = "accounts\\" + str(account_number) + "\\info.txt"
        
        self.loadInfo()

    def setName(self):
        response = input("NAME (Enter \"..\" to go back)> ")
        if response != "..":
            while not response:
                respones = input("PLEASE ENTER YOUR NAME > ")
                
            self.change("name", response)
            changed = True
        else:
            changed = False
            
        return changed

    def setPassword(self):
        # ask for old password
        security_loop = True
        password_changed = False

        while security_loop:
            input_password = input("OLD PASSWORD > ")

            # if use enters old password wrong
            if input_password != self.getPassword():

                print("\n[A]\tTry Again\n[B]\tBack")
                incorrect_password_choice = input("> ").lower()
                
                while incorrect_password_choice not in ("a", "b"):
                    incorrect_password_choice = input("> ").lower()

                if incorrect_password_choice == "b":
                    security_loop = True
                    
            else:
                # if it's correct
                # ask for new password
                new_password = input("NEW PASSWORD > ")
                while not new_password:
                    new_password = input("PLEASE ENTER A NEW PASSWORD > ")

                self.change("password", new_password)
                
                security_loop = True
                password_changed = True

        return password_changed

    def getAccNumber(self):
        return self.acc_number

    def getName(self):
        return self.name

    def getPassword(self):
        return self.password

    def getPhone(self):
        if self.phone != "nophone":
            return self.phone
        else:
            return "NO PHONE"

    def getAddress(self):
        if self.address != "noaddress":
            return self.address
        else:
            return "NO ADDRESS"

    def getEmail(self):
        if self.email != "noemail":
            return self.phone
        else:
            return "NO EMAIL"

    def getBalance(self):
        try:
            return float(self.balance) / 100
        except:
            return "Unexpected Error"

    def getCannotChange(self):
        return self.cannot_change

    def loadInfo(self):
        file = open(self.info_dir, "r")
        
        self.acc_number = file.readline().strip()
        self.password = file.readline().strip()
        self.name = file.readline().strip()
        self.phone = file.readline().strip()
        self.address = file.readline().strip()
        self.email = file.readline().strip()
        self.balance = (file.readline().strip())

        file.close()
    
    def change(self, profile, new_value):
        file = open(self.info_dir, "w")
        file.truncate()

        file.write(self.acc_number + "\n")

        if profile == "password":
            file.write(new_value + "\n")
        else:
            file.write(self.password + "\n")

        if profile == "name":
            file.write(new_value + "\n")
        else:
            file.write(self.name + "\n")

        if profile == "phone":
            file.write(new_value + "\n")
        else:
            file.write(self.phone + "\n")

        if profile == "address":
            file.write(new_value + "\n")
        else:
            file.write(self.address + "\n")

        if profile == "email":
            file.write(new_value + "\n")
        else:
            file.write(self.email + "\n")

        if profile == "balance":
            file.write(new_value + "\n")
        else:
            file.write(self.balance)

        file.close()
        self.loadInfo()
        


#### ATM MACHINE PROGRAM TEXT ADMIN CLASS   ####
#### SEPT 25 2014                           ####

import os
import math
import time
import random

import Account
import Client
import Search

class Admin():
    def __init__(self):
        """ admin constructor """
        self.search = Search.SearchTools()
        self.accounts = []
        self.updateDir()
        self.updateAcc()

    def ask(self, prompt, whitelist = (), exception = "Try Again "):

        if "***" in whitelist:
            temp_response = input(prompt).lower()
        else:
            temp_response = input(prompt)

        # if a list of response is requsted
        if whitelist and "." not in whitelist:
            while temp_response not in whitelist:
                if "***" in whitelist:
                    temp_response = input(exception + prompt).lower()
                else:
                    temp_response = input(exception + prompt)

            return temp_response

        # any response not empty is requested
        elif whitelist and "." in whitelist:
            while not temp_response:
                if "***" in whitelist:
                    temp_response = input(exception + prompt).lower()
                else:
                    temp_response = input(exception + prompt)

            return temp_response
            
        # any response
        return temp_response

    def updateDir(self):
        """ updates the account library """
        self.account_dir = next(os.walk("accounts"))[1]

    def updateAcc(self):
        """ refreshes the account object list """
        self.accounts = []
        for account in self.account_dir:
            self.accounts.append(Account.Account(account))
    
    ## admin functions
    def adminAdd(self):
        """ add an account """
    
        os.system("cls")
        print("""
============================================================================
|                               ADD AN ACCOUNT                             |
============================================================================
PLEASE FILL OUT THE FOLLOWING FORM. YOU CAN LEAVE EMPTY FOR OPTIONALS\n""")
              
        # ask for profiles to create
        new_name = self.ask("FULL NAME > ", ( "."), "PLEASE ENTER YOUR ")
        new_phone = self.ask("PHONE NUMBER (optional) > ")
        new_email = self.ask("E-MAIL (optional) > ")
        new_address = self.ask("ADDRESS (optional) > ")
        new_password = self.ask("PASSWORD > ", ("."), "PLEASE ENTER A ")
        #self.ask("CONFIRM PASSWORD > ", (new_password), "PASSWORDS DOES NOT MATCH. PLEASE ")

        # optional field corrections
        if new_phone == "":
            new_phone = "nophone"
        if new_address == "":
            new_address = "noaddress"
        if "@" not in new_email:
            new_email = "noemail"
        
        # account number generation
        new_account_number = "4906"
        created = False
        while not created:
            for i in range(4, 16):
                new_account_number += str(random.randint(0, 9))

            # avoid repeating account numbers even though its nearly impossible
            if new_account_number not in self.account_dir:
                created = True

        # create new directory and profile
        try:
            os.system("mkdir accounts\\" + new_account_number)
            os.system("echo. 2>accounts\\" + new_account_number + "\\info.txt")
            os.system("echo. 2>accounts\\" + new_account_number + "\\history.txt")
        except:
            print("ERROR CREATING PROFILE")

        # write all the profile onto a separate text file
        # [[[info.txt]]]
        # [0] Account number
        # [1] Password
        # [2] Full name
        # [3] Phone
        # [4] Address
        # [5] Email
        # [6] Balance

        # write info to profile text file
        try:
            profile = open("accounts\\" + new_account_number + "\\info.txt", "w")
            profile.write(new_account_number + "\n")
            profile.write(new_password + "\n")
            profile.write(new_name + "\n")
            profile.write(new_phone + "\n")
            profile.write(new_address + "\n")
            profile.write(new_email + "\n")
            profile.write("0")
            profile.close()
        except:
            print("ERROR WRITING PROFILE")

        # give user a done screen
        os.system("cls")
        
        print("""
============================================================================
|                                 SUCCESS                                  |
============================================================================
CONGRATULATIONS! YOUR NEW ACCOUNT HAS BEEN CREATED!""")
        print("Your account number is " + new_account_number + ". Please Remember it\n")

        # return to admin menu
        input("Press [Enter] to go back to Admin Menu")

        # updates the library
        self.updateDir()
        
    def adminEdit(self):
        """ remove an account """

        isEditAccountsDone = False

        while isEditAccountsDone == False:
            os.system("cls")
            print("""
============================================================================
|                              EDIT AN ACCOUNT                             |
============================================================================
YOU CAN ENTER THE NUMBER TO EDIT AN ACCOUNT\n""")

            # print options
            input_dir = []
            for i in range(len(self.account_dir)):
                print("[" + str(i + 1) + "]\t" + self.account_dir[i])
                input_dir.append(str(i + 1))

            input_dir.append("b")
            input_dir.append("a")
            input_dir.append("***")
            print("\n[A]    Search")
            print("[B]    Back")

            # ask for options and convert it to accounts
            selection = self.ask("> ", input_dir)

            if selection == "b":
                # break out of the loop
                isEditAccountsDone = True
            elif selection == "a":
                # searching an account
                os.system("cls")
                print("""
============================================================================
|                               SEARCH ACCOUNT                             |
============================================================================
SEARCH AN ACCOUNT
[1]     Search by account number
[2]     Search by name
[3]     Search by phone number

[B]     Back""")
                results_banner = """
============================================================================
|                                   RESULTS                                |
============================================================================"""
                
                search_selection = self.ask("> ", ("***", "1", "2", "3", "b"))

                if search_selection == "b":
                    # if the selection is back
                    ""
                elif search_selection == "1":
                    # search by account number
                    # ask for number
                    search_input = self.ask("\nNUMBER > ", ".")
                    
                    search_list = self.search.searchList(search_input, self.account_dir)
                    input_list = []

                    # out put the results
                    os.system("cls")
                    print(results_banner)
                    if serach_list:
                        for i in range(len(search_list)):
                            print("[" + str(i + 1) + "]\t" + search_list[i])
                            input_list.append(str(i + 1))

                        selection = self.ask("> ", input_list)
                    else:
                        print("No results\n")
                        selection = "-1"

                    # edit
                    if selection != "-1":
                        self.adminEditDetails(selection)
                        
                elif search_selection == "2":
                    # serach by name
                    # ask for name
                    search_input = self.ask("NAME > ", (".", "***"))

                    # get all names
                    search_list = self.search.searchName(search_input, self.accounts)
                    input_list = []

                    # out put the results
                    os.system("cls")
                    print(results_banner)
                    if search_list:
                        for i in range(len(search_list)):
                            print("[" + str(i + 1) + "]\t" + search_list[i])
                            input_list.append(str(i + 1))

                        selection = self.ask("> ", input_list)
                
            else:
                self.adminEditDetails(selection)

        # update directory
        self.updateDir()

    def adminEditDetails(self, selection): ##### IMPORTANT!!! CHANGE SELECTION TO ACC NUM

        # once an account is selected
        isEditAccountDone = False
        edit_account = self.accounts[int(selection) - 1]
        
        while isEditAccountDone == False:
            os.system("cls")
            print("""
============================================================================
|                              EDIT AN ACCOUNT                             |
============================================================================
REVIEW, EDIT OR DELETE THE PROFILE
[1]     Name\t\t""" + str(edit_account.getName()) + """
(2)     Account Number\t""" + str(edit_account.getAccNumber()) + """
[3]     Password\t""" + str(edit_account.getPassword()) + """
[4]     Phone Number\t""" + str(edit_account.getPhone()) + """
[5]     Address\t\t""" + str(edit_account.getAddress()) + """
[6]     E-Mail\t\t""" + str(edit_account.getEmail()) + """
(7)     Balance\t\t$""" + str(edit_account.getBalance()) + """

[A]     Delete this account
[B]     Back\n""")
            
            # profile option selection
            edit_option = self.ask("> ", ("***", "1", "2" "3", "4", "5", "6", "7", "a", "b"))
            print(edit_option)

            # name
            if edit_option == "1":
                if edit_account.setName():
                    print("Name change successful")
                else:
                    print("Name change cancelled by user")

                time.sleep(1)

            # acc number or balance cannot be changed
            elif edit_option in ("2", "7"):
                input(edit_account.getCannotChange())

            # password change
            elif edit_option == "3":
                if edit_account.setPassword():
                    print("Password change successful")
                else:
                    print("Password change cancelled by user")

                time.sleep(1)

            elif edit_option == "b":
                # go back to the previous menu
                isEditAccountDone = True

        # update dir
        self.updateDir()

    def adminOff(self):
        # close the program
        os.system("cls")
        input("GOOD BYE")
        
    def displayMenu(self):
        """ The main menu displayed """
        
        os.system("cls")

        print("""
============================================================================
|                               ADMIN SETTINGS                             |
============================================================================
[1]     Add an account
[2]     Edit an account
[3]     Start client-mode
[4]     Admin options
[5]     Shutdown\n""")

        response = self.ask("> ", ("1", "2", "3", "4", "5"))

        if response == "1":
            self.adminAdd()
            self.displayMenu()
        elif response == "2":
            self.adminEdit()
            self.displayMenu()
        elif response == "3":
            self.adminStart()
        elif response == "4":
            self.adminOption()
        elif response == "5":
            self.adminOff()
        else:
            print("ERROR! Response not properly registered")
        
    def displaySplash(self):
        print("""
SPONSOR MESSAGES:
    ..........     ..........      .uoedWWWeou.             ............
   <$$$$$$$$$F     $$$$$$$$$F   u@$$$$$$$$$$$$$$o.         .$$$$$$$$$$$N
   9$$$$$$$$$     J$$$$$$$$$  .$$$$$$$$$$$$$$$$$$$e        $$$$$$$$$$$$$
   $$$$$$$$$$     8$$$$$$$$$  $$$$$$$$$$$$$$$$$$$$"       @$$$$$$$$$$$$$
  :$$$$$$$$$F     $$$$$$$$$F 8$$$$$$$$$$***$$$$$$`       @$$$$$$$$$$$$$$L
  9$$$$$$$$$     J$$$$$$$$$  $$$$$$$$$$k    ^#$P        d$$$$$$$$$$$$$$$&
  $$$$$$$$$$     8$$$$$$$$$  $$$$$$$$$$$o.    ^        u$$$$$$$$$$$$$$$$$
 :$$$$$$$$$F     $$$$$$$$$F  R$$$$$$$$$$$$$$u.        x$$$$$$$$$$$$$$$$$$
 9$$$$$$$$$     J$$$$$$$$$    *$$$$$$$$$$$$$$$o      :$$$$$$$$$R$$$$$$$$>
 $$$$$$$$$$     8$$$$$$$$$     "R$$$$$$$$$$$$$$$    .$$$$$$$$$F9$$$$$$$$k
:$$$$$$$$$E     $$$$$$$$$F   L   `"*$$$$$$$$$$$$N   $$$$$$$$$$ '$$$$$$$$$
'$$$$$$$$$N   .$$$$$$$$$$  .$$$u     ^$$$$$$$$$$$ $$$$$$$$$$NWW@$$$$$$$$$
'$$$$$$$$$$$W@$$$$$$$$$$F u$$$$$$ou...d$$$$$$$$$$@$$$$$$$$$$$$$$$$$$$$$$$
 $$$$$$$$$$$$$$$$$$$$$$$@$$$$$$$$$$$$$$$$$$$$$$\"d$$$$$$$$$$$$$$$$$$$$$$$$L
 \"$$$$$$$$$$$$$$$$$$$$P\"$$$$$$$$$$$$$$$$$$$$$$#d$$$$$$$$$$$$$$$$$$$$$$$$$&
  #$$$$$$$$$$$$$$$$$$#  '#$$$$$$$$$$$$$$$$$$$"x$$$$$$$$$$"``````$$$$$$$$$$
   "R$$$$$$$$$$$$$$#        "R$$$$$$$$$$$$$$# :$$$$$$$$$$"      9$$$$$$$$$
     `\"**R$$$R**\"\"             \"#***$$***#\"   \"\"\"\"\"\"\"\"\"\"\"       \"\"\"\"\"\"\"\"\"\"
============================================================================
|              \"We're Better Than Everyone Else, Even Canada!\"             |
============================================================================""")
        time.sleep(0.5)

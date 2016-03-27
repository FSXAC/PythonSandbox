### KSP Mission Manager ###
### Mansur He 2014-10-18 ###

import os
import time

def main():
    """ main function """

    os.system("mode 100")

    global MISSION_TYPE
    global CELESTIAL_BODIES
    global LOCATIONS

    # explore: bodies
    # science: science around {bodies}
    # test: equipments
    # rescue: kerbal
    MISSION_TYPE = ["EXPLORE", "COLLECT", "TEST", "RESCUE"]
    
    CELESTIAL_BODIES = ["KERBOL", "MOHO", "EVE", "GILLY", "KERBIN",
                        "MUN", "MINMUS", "DUNA", "IKE", "DRES",
                        "JOOL", "LAYTHE", "VALL", "TYLO", "BOP ",
                        "POL ", "EELOO"]
    
    LOCATIONS = ["LANDED", "SPLASHDOWN", "ORBIT", "IN-FLIGHT", "SUB-ORBIT",
                 "ESCAPE_TRAJ"]

    mission_manager = Manager()
    mission_manager.display()


class Manager(): 
    def __init__(self):

        # global variables
        global MISSION_TYPE
        global CELESTIAL_BODIES
        global LOCATIONS

        self.types = MISSION_TYPE
        self.bodies = CELESTIAL_BODIES
        self.loc = LOCATIONS
        
        self.tasks = []
        
        # load up saved file
        file = open("Tasks.txt", "r")
        ident_counter = 1
        for task in file:
            t_attributes = task.strip().split("%")

            # create task object for each task in the file
##            if (t_attributes[1] in MISSION_TYPE) and (
##                t_attributes[3] in CELESTIAL_BODIES) and (
##                    t_attributes[4] in LOCATIONS):
                
            t_obj = Task(t_attributes[1], t_attributes[3], t_attributes[4])

            t_obj.setId(ident_counter)

            if t_attributes[2] != "NULL":
                t_obj.setEquipment(t_attributes[2])
                                            
            t_obj.setAlt((t_attributes[5], t_attributes[6]))
            t_obj.setSpeed((t_attributes[7], t_attributes[8]))
            t_obj.setReward((t_attributes[9], t_attributes[10]))

            self.tasks.append(t_obj)

            ident_counter += 1

        file.close()        

    def display(self):
        """ display all tasks and options """

        # save data
        self.saveData()
        
        # clear the screen
        os.system("cls")
        
        # all missions. main menu
        print("""========================================================================================
|                                      MISSION CONTROL                                 |
========================================================================================
|ID\t|TYPE\t|NAME\t|LOCATION\t|ALTITUDE RANGE\t|SPEED RANGE\t|SCI\t|FUNDS""")
        for task in self.tasks:
            print(task)

        # menu selection
        print("""\n
[1]\tADD A TASK
[2]\tREMOVE A TASK
[3]\tSORT
[4]\tSAVE AND QUIT

[5]\tRESET""")

        # ask for options
        user_selection = input("> ")

        while user_selection not in ("1", "2", "3", "4", "5"):
            user_selection = input("Try again > ")

        # add a task
        if user_selection == "1":
            self.addTask()
        elif user_selection == "2":
            self.delTask()
        elif user_selection == "3":
            # sorting
            # by ID, Equipment, type, location, body, alt_min, alt_max, speed_min, speed_max,
            # science reward, funds reward

            print("""
SORY BY:
[1]\tID
[2]\tEQUIPMENT
[3]\tMISSION TYPE
[4]\tLOCATION
[5]\tCELESTIAL BODY
[6]\tALTITUDE RANGE
[7]\tSPEED RANGE
[8]\tSCIENCE REWARD
[9]\tFUNDS REWARD

[0]\tBACK""")

            # ask for input
            sort_selection = input("> ")

            while sort_selection not in ("1", "2", "3", "4", "5",
                                         "6", "7", "8", "9", "0"):
                sort_selection = input("> ")

            # actual sorting
            loops = len(self.tasks)
            
            if sort_selection == "1":
                # sort by ID
                while loops > 0:
                    for i in range(loops - 1):

                        # compare
                        if self.tasks[i].getId() > self.tasks[i + 1].getId():
                            temp_value = self.tasks[i]
                            self.tasks[i] = self.tasks[i + 1]
                            self.tasks[i + 1] = temp_value
                            
                    loops -= 1

            elif sort_selection == "5":
                # sort by celestial body
                while loops > 0:
                    for i in range(loops - 1):

                        # compare
                        if self.tasks[i].getBody() > self.tasks[i + 1].getBody():
                            temp_value = self.tasks[i]
                            self.tasks[i] = self.tasks[i + 1]
                            self.tasks[i + 1] = temp_value
                            
                    loops -= 1

            # return to main screen
            self.display()
            
        elif user_selection == "4":
            return True

        elif user_selection == "5":
            # resets the saved file
            file = open("Tasks.txt", "w")
            file.truncate()

            file.close()

            self.display()

    def addTask(self):
        """ add a new task to file here """
        print("""\n
========================================================
|                   ADD AN MISSION TASK                |
========================================================\n""")
        for i in range(len(self.types)):
            print("[" + str(i + 1) + "]\t" + self.types[i])

        # ask type
        new_mission_type = input("MISSION TYPE: ")
        
        while new_mission_type not in ("1", "2", "3", "4"):
            new_mission_type = input("MISSION TYPE: ")

        # default task attributes
        mission_type = "EXPLORE"
        name = "-------"
        location = "-------"
        body = "KERBIN"
        speed_min = "-------"
        speed_max = "-------"
        alt_min = "-------"
        alt_max = "-------"
        reward_sci = "0"
        reward_fund = "0"
        
        if new_mission_type == "1" or new_mission_type == "2":
            # Explore or science
            if new_mission_type == "2":
                mission_type = "COLLECT"
            
            # ask body
            body_inputs = self.askBody()      

            # body selection
            body = input("CELESTIAL BODY: ")
            while body not in body_inputs:
                body = input("CELESTIAL BODY: ")

            # ask reward
            reward_sci = input("SCIENCE REWARD: ")
            reward_fund = input("FUNDS REWARD: ")

            if not reward_sci:
                reward_sci = "------"

            if not reward_fund:
                reward_fund = "------"

        elif new_mission_type == "3":
            # ask equipment
            name = input("NAME: ").upper()
            if not name:
                name = "-------"

            # if name is longer than 7 characters
            if len(name) > 7:
                # remove vowels
                new_name = ""
                for letter in name:
                    if letter not in "aeiou":
                        new_name += letter

                name = new_name

            # if name is still longer than 7 characters
            if len(name) > 7:
                name = name[0:7]


        # add to the list of missions
        new_task = Task(mission_type, self.bodies[int(body) - 1], location)
        new_task.setId(len(self.tasks) + 1)
        new_task.setEquipment(name)
        new_task.setAlt((alt_min, alt_max))
        new_task.setSpeed((speed_min, speed_max))
        new_task.setReward((reward_sci, reward_fund))

        self.tasks.append(new_task)
            
        print("\n----DONE-----")
        time.sleep(1)
        
        self.display()            
            
    def delTask(self):
        """ delete tasks here """

    def askBody(self):
        body_inputs = []
        for choices in range(len(self.bodies)):
            body_inputs.append(str(choices + 1))

        # display selection
        print("\n")          
        for i in range(-1, len(self.bodies), 3):
            string = ""
            
            for column in range(1, 4):
                try:
                    string += ("[" + str(i + column + 1) + "] " + self.bodies[i + column] +
                               "\t" * (6 // len(self.bodies[i + column])))
                except:
                    None                
            print(string)

        return body_inputs

    def saveData(self):
        # opens the task file and save the list

        file = open("Tasks.txt", "w")

        # deletes all the lines in the text file
        file.truncate()
        
        for task in self.tasks:
            string = task.getFileLine()
            file.write(string + "\n")

        file.close()

class Task():
    def __init__(self, mission_type,
                 celestial_body, location):
        
        """ constructor """
        self.id = 0
        self.type = mission_type
        self.equipment = "-------"
        self.body = celestial_body
        self.location = location
        self.altitude = ("------", "------")
        self.speed = ("----", "----")
        self.reward = ("------", "------")

    def __str__(self):
        string = str(str(self.id) + "\t" + str(self.type) + "\t" +
                     str(self.equipment) + "\t" + str(self.location) + "\t" +
                     str(self.body) + "\t" + str(self.altitude[0]) + "\t" +
                     str(self.altitude[1]) + "\t" + str(self.speed[0]) + "\t" +
                     str(self.speed[1]) + "\t" + str(self.reward[0]) + "S\t" +
                     str(self.reward[1]) + "F")

        return string

    def getFileLine(self):
        string = (str(self.id) + "%" + self.type + "%" + self.equipment + "%" + 
                  self.body + "%" + self.location + "%" + self.altitude[0] + "%" +
                  self.altitude[1] + "%" + self.speed[0] + "%" + self.speed[1] + "%" +
                  self.reward[0] + "%" + self.reward[1])

        return string

    def getId(self):
        return self.id

    def getBody(self):
        return self.body

    def setId(self, ident):
        self.id = ident

    def setEquipment(self, equipment):
        self.equipment = equipment

    def setAlt(self, alt):
        self.altitude = alt

    def setSpeed(self, speed):
        self.speed = speed

    def setReward(self, reward):
        self.reward = reward

main()

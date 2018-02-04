#Kyle Munoz
#Physicians Office Simulation

import random

#Names List
names =["joey","bobby","sueann","loretta","grant",\
        "jenny","billy","tucker","cletus","hunter",\
        "gunner","rose","amy","charlotte","duke",\
        "ricky","bo","luke","jesse"]


#Class Patient
class Patient:
    def __init__(self):
        #Give Name
        self.name = names[random.randint(0, len(names)-1)]\
                    + " " + names[random.randint(0, len(names)-1)]

        #Exam Room Treatment Time
        self.treatmentTime = random.randint(15,20)

        #Track time spent waiting
    def __str__(self):
        return self.name
    
    def enter(self, var):
        self.enterTime = var

    def getEnterTime(self):
        return self.enterTime
    
    def examRoomTime(self,var):
        self.examRoomEnterTime = var
        
    def getExamRoomEnterTime(self):
        return self.examRoomEnterTime
    
        #remove patient from simulation
    def exit(self, var):
        self.exitTime = var

    def getExitTime(self):
        return self.exitTime
        #Track time in pyshician room based of of time entering physicial room.
        #Track total time in doctors office
        #!!!!!Can use a while loop for minutes

#Nurse
#Nurses triage 1 person per minute
#Nurses should see all patients first, before doctor
def callNurse():
    """move patient from waiting room to triage room"""
    TriageRoom.append(WaitingRoom.pop(0))


def treatPatient():
    """move patient from triage room to exam room"""
    ExamRoom.append(TriageRoom.pop(0))
    
#Waiting Room for entering patients
WaitingRoom = []
#Triage Room for after visiting with a triage nurse
TriageRoom = []
#Exam Rooms
ExamRoom = []








def main():
    ExamRooms = 6#int(input("How many exam rooms are there? "))
    Physicians = 6#int(input("How many Doctors are working? "))
    Nurses = 6#int(input("How many nurses are working? "))
    HelpableNumber = min(Physicians, ExamRooms)
    patientsSeen = 0
    while True:
        #Add patients
        newPatients = int(input("How many new patients are there? "))
        for i in range(newPatients):

            patient= Patient()
            patientsSeen +=1
            WaitingRoom.append(patient)
        print("Waiting before nurses: ", WaitingRoom)
        print("Triage before nurses: ", TriageRoom)
        for i in range(Nurses):
            try:
                callNurse()
                
            except IndexError:
                break
        print("Waiting after nurses: ", WaitingRoom)
        print("Triage after nurses: ", TriageRoom)
        #Add patients to exam rooms if there are any available
        for i in range(HelpableNumber):
            if len(TriageRoom) > 0:
                treatPatient()
                HelpableNumber -=1
        print("Exam after doctors: ", ExamRoom)
        print("Triage after doctors: ", TriageRoom)
        for patients in ExamRoom:
            patients.treatmentTime -=1
            print(patients.name, patients.treatmentTime)
            if patients.treatmentTime == 0:
                HelpableNumber += 1
                del(patients)
    Minute += 1
main()

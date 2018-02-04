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
    
    def enterExamRoomTime(self,var):
        self.enterExamRoomTime = var
        
    def getEnterExamRoomTime(self):
        return self.enterExamRoomTime
    
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
    


WaitingRoom = []
TriageRoom = []
ExamRoom = []






def main():
    
    ExamRooms = int(input("How many exam rooms are there? "))
    Physicians = int(input("How many Doctors are working? "))
    Nurses = int(input("How many nurses are working? "))
    HelpableNumber = min(Physicians, ExamRooms)
    patientsSeen = 0
    Minute = 0
    TimeIn = 0
    WaitTime = 0
    ExamTime = 0
    while True:
       
        newPatients = input("How many new patients are there? ")
        if newPatients == "done" or newPatients == "Done":
            break
        elif newPatients == "":
            newPatients = 0
        else:
            newPatients = int(newPatients)
        for i in range(newPatients):
            patient = Patient()
            patient.enter(Minute)
            WaitingRoom.append(patient)
        ##print("Waiting before nurses: ", WaitingRoom, "\n")
        ##print("Triage before nurses: ", TriageRoom, "\n")
        for i in range(Nurses):
            try:
                callNurse() 
            except IndexError:
                break
        ##print("Waiting after nurses: ", WaitingRoom)
        ##print("Triage after nurses: ", TriageRoom)
        
        for i in range(HelpableNumber):
            if len(TriageRoom) > 0:
                TriageRoom[0].enterExamRoomTime(Minute)
                WaitTime = WaitTime + (TriageRoom[0].getEnterExamRoomTime() - TriageRoom[0].getEnterTime())
                treatPatient()
                HelpableNumber -=1
        ##print("Exam after doctors: ", ExamRoom, "\n")
        ##print("Triage after doctors: ", TriageRoom, "\n")
        print("\n")
        print("Patient Name and Time Left:")
        for patients in ExamRoom:
            patients.treatmentTime -=1
            
            print(patients.name, patients.treatmentTime)
            if patients.treatmentTime == 0:
                patients.exit(Minute)
                ExamRoom.remove(patients)
                ExamTime = ExamTime + (patients.getExitTime() - patients.getEnterExamRoomTime())
                TimeIn = TimeIn + (patients.getExitTime() - patients.getEnterTime())
                    
                patientsSeen += 1
                ##print("Patients Seen:", patientsSeen)
                HelpableNumber += 1
                del(patients)
        Minute += 1
        print("\n")
        print("Minutes Past:", Minute)
        print("\n")
        
    print("\n")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("\n")
    print("Time spent waiting for treatment: ", WaitTime)
    print("Time spent in Exam Rooms:", ExamTime)
    print("Time spent at the Physicians:", TimeIn)
    print("This office saw ", patientsSeen, " patients in ", Minute, " minutes.")
    averageVisitTime = (TimeIn/patientsSeen)
    print("The average time spent at the physician's was ", averageVisitTime, "minutes.")
    averageWaitTime = (WaitTime/patientsSeen)
    print("The average time spent waiting for an Exam Room was ", averageWaitTime, "minutes.")
    averageExamTime = (ExamTime/patientsSeen)
    print("The average time spent in an Exam Room was ", averageExamTime, "minutes.")
main()

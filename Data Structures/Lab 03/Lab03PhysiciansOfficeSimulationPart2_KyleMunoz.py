#Kyle Munoz
#Physicians Office Simulation

import random

#Class Physician
class Physician:
    def __init__(self, name):
        self.name = name
        Helping = 0

#Class Nurse
#Nurses triage 1 person per minute
#Nurses should see all patients first, before doctor
class Nurse:
    def __init__(self, name):
        self.name = name
        Helping = 0

#Class Patient
class Patient:
    def __init__(self, name, waitingroom):
        self.name = name
        waitingroom.append(name)
        self.DoctorHelpTime = int(random.randint(15, 20))
        HasBeenHelped = 0#0 means waiting, 1 means has been helped by a nurse, 2 means has seen a physician
        #Track time spent waiting
        #Track time in pyshician room based of of time entering physicial room.
        #Track total time in doctors office
        #!!!!!Can use a while loop for minutes
#Waiting Room
    #1 for entering patients
    #2 for after visiting with a triage nurse
Waitingroom1 = []
Waitingroom2 = []

#Exam Room
#0 indicates and empty room
ExamRooms = [0,0,0,0,0,0]
ExamRoomPatients = ["noone","noone","noone","noone","noone","noone"]




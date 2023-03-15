import numpy as np
import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
from random import randint
import constants as c
import os
import time
import create

class SOLUTION:

    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        self.Number_of_Links = randint(2, c.maxLinks)
        self.links = None
        self.joints = None
        self.weights = None

    def set_ID(self, newID):
        self.myID = newID
        
    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("start /B py simulate.py " + directOrGUI + " " + str(self.myID))
        
    def  Wait_For_Simulation_To_End(self):
        while True:
            while not os.path.exists("fitness" +str(self.myID)+ ".txt"):
                time.sleep(0.001)
            try:
                f = open("fitness" + str(self.myID) + ".txt", "r")
                break
            except Exception as e:
                print("Caught file permission race condition")
                time.sleep(0.01)
                continue;

        self.fitness = float(f.read())
        
        f.close()
        os.system(f"del fitness{str(self.myID)}.txt")
        os.system(f"del body{str(self.myID)}.urdf")
        

    def Create_World(self):

        if self.myID == 0:
            pyrosim.Start_SDF("world.sdf")

            length = 1
            width = 1
            height = 1
    
            pyrosim.Send_Cube(name="Box", pos=[3,3,0.5] , size=[length,width,height]) 

            pyrosim.End()

    def Create_Body(self):
        self.links, self.joints = create.Create_Body(self.myID, self.Number_of_Links, self.links, self.joints)

    def Create_Brain(self):
        self.weights = create.Create_Brain(self.myID, self.links, self.joints, self.weights)

    def Mutate(self):
        sensor = randint(0, self.weights.shape[0]-1)
        motor= randint(0, self.weights.shape[1]-1)

        self.weights[sensor, motor] = np.random.randn()

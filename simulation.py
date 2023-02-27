import pybullet as p
import time
import pybullet_data
import robot
import pyrosim.pyrosim as pyrosim
import sensor
import sys


class SIMULATION:

    def __init__(self, directOrGUI, solutionID):

        self.directOrGUI = directOrGUI

        if directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        p.setGravity(0,0,-9.8)
        p.loadURDF("plane.urdf")
        p.loadSDF("world.sdf")

        self.robot = robot.ROBOT(solutionID)

    def Run(self):
        for t in range(2500):

            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Think()
            self.robot.Act(t)
            
            
            if self.directOrGUI == "GUI":
                time.sleep(1/240)   
    
    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):

        p.disconnect()


        

        
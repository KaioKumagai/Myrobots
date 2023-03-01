import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
import constants as c
from tempfile import TemporaryFile
import sensor
import motor
import simulation
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os


class ROBOT:

    def __init__(self, solutionID):
        self.robotId = p.loadURDF("body.urdf")
        self.solutionID = solutionID
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

        # self.values = np.zeros(3500)
        self.values = np.zeros(c.timeofsimulation)
        brainID = 'brain' + str(solutionID) + '.nndf'
        self.nn = NEURAL_NETWORK(brainID)
        os.system(f"del brain{str(self.solutionID)}.nndf")
        
        pass

    def Prepare_To_Sense(self):
        self.sensor = {}
        for linkName in pyrosim.linkNamesToIndices:

            # print(linkName)
            self.sensor[linkName] = sensor.SENSOR(linkName)
    
    def Sense(self, t):
        for sensor_instance in self.sensor.values():
            sensor_instance.Get_Value(t)

    def Prepare_To_Act(self):
        self.motor = {}
        for jointName in pyrosim.jointNamesToIndices:

            self.motor[jointName] = motor.MOTOR(jointName)  

    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)*c.motorJointRange
                
                self.motor[jointName.encode('UTF-8')].Set_Value(self.robotId, desiredAngle )


        
    

    def Think(self):
        self.nn.Update()

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId,0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        f = open("tmp" + str(self.solutionID) + ".txt", "w")
        f.write(str(xCoordinateOfLinkZero))
        f.close()
        os.rename("tmp"+str(self.solutionID)+".txt" , "fitness"+str(self.solutionID)+".txt")
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

        self.values = np.zeros(2500)
        brainID = 'brain' + str(solutionID) + '.nndf'
        self.nn = NEURAL_NETWORK(brainID)
        os.system(f"del brain{str(self.solutionID)}.nndf")
        
        # self.targetAngles_backLeg = np.zeros(2500)
        # self.a = np.linspace(0, 2*np.pi, 2500)
        # for i in range(2500):
        #     self.targetAngles_backLeg[i] = c.amplitude_backLeg*np.sin(self.a[i]*c.frequency_backLeg + c.phaseOffset_backLeg)


        # self.targetAngles_frontLeg = np.zeros(2500)
        # self.a = np.linspace(0, 2*np.pi, 2500)
        # for i in range(2500):
        #     self.targetAngles_frontLeg[i] = c.amplitude_frontLeg*np.sin(self.a[i]*c.frequency_frontLeg + c.phaseOffset_frontLeg)

        # outfile = TemporaryFile()

        # for t in range(2500):
        #     p.stepSimulation()
    
        
        pass

    def Prepare_To_Sense(self):
        self.sensor = {}
        for linkName in pyrosim.linkNamesToIndices:

            # print(linkName)
            self.sensor[linkName] = sensor.SENSOR(linkName)
    
    def Sense(self, t):
        for sensor_instance in self.sensor.values():
            # print(self.sensor)
            # self.values[simulation.t] = sensor.Get_value[sensor]
            sensor_instance.Get_Value(t)
    #     self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    #     self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg") 
    # 
    def Prepare_To_Act(self):
        self.motor = {}
        for jointName in pyrosim.jointNamesToIndices:

            # print(linkName)
            self.motor[jointName] = motor.MOTOR(jointName)  

    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                # for motor_instance in self.motor.values():
                #     motor_instance.Set_Value(self.robotId, desiredAngle )
                # print(self.motor)
                
                self.motor[jointName.encode('UTF-8')].Set_Value(self.robotId, desiredAngle )

                # print("Neuron name Joint Name Desired Angle")
                # print(neuronName)
                # print(jointName)
                # print(desiredAngle)

        
            # for motor_instance in self.motor.values():
            #     motor_instance.Set_Value(self.robotId, t)
    

    def Think(self):
        self.nn.Update()
        # self.nn.Print()

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId,0)
        # print(f'This is {stateOfLinkZero}')
        positionOfLinkZero = stateOfLinkZero[0]
        # print(f'This is {positionOfLinkZero}')
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        # print(f'This is {xCoordinateOfLinkZero}')
        f = open("tmp" + str(self.solutionID) + ".txt", "w")
        # os.rename("tmp"+str(self.solutionID)+".txt" , "fitness"+str(self.solutionID)+".txt")
        # rename tmpID.txt fitnessID.txt
        f.write(str(xCoordinateOfLinkZero))
        f.close()
        os.rename("tmp"+str(self.solutionID)+".txt" , "fitness"+str(self.solutionID)+".txt")
        exit()

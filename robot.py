import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
import constants as c
from tempfile import TemporaryFile
import sensor

class ROBOT:

    def __init__(self):
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()

        # self.backLegSensorValues = np.zeros(1000)
        # self.frontLegSensorValues = np.zeros(1000)
        self.values = np.zeros(1000)
        # print(self.values)

        self.targetAngles_backLeg = np.zeros(1000)
        self.a = np.linspace(0, 2*np.pi, 1000)
        for i in range(1000):
            self.targetAngles_backLeg[i] = c.amplitude_backLeg*np.sin(self.a[i]*c.frequency_backLeg + c.phaseOffset_backLeg)


        self.targetAngles_frontLeg = np.zeros(1000)
        self.a = np.linspace(0, 2*np.pi, 1000)
        for i in range(1000):
            self.targetAngles_frontLeg[i] = c.amplitude_frontLeg*np.sin(self.a[i]*c.frequency_frontLeg + c.phaseOffset_frontLeg)

        # outfile = TemporaryFile()

        # for t in range(1000):
        #     p.stepSimulation()
        self.motors = {}
        
        pass

    def Prepare_To_Sense(self):
        self.sensor = {}
        for linkName in pyrosim.linkNamesToIndices:

            # print(linkName)
            self.sensor[linkName] = sensor.SENSOR(linkName)
    
    # def Sense(self):
    #     self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    #     self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")   

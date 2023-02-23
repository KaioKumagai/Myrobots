import pybullet as p
import time
import pybullet_data
import world
import robot
import pyrosim.pyrosim as pyrosim
import numpy as np
class SENSOR:

    def __init__(self, name):

        self.linkName = name
        self.values = np.zeros(2500)

    def Get_Value(self, t):
        # self.linkName = name

        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

        # print(f'{self.linkName=}: {self.values[t]=}')
        if t == 999:
            # print('World')
            g =+ 1
            # print(self.values)

    # def Save_Values(self, g):
    #     if g == 1:
    #         backLegSensorValues = self.values
    #         np.save('data/backLegSensorValues.npy',backLegSensorValues)
    #     if g == 2:
    #         TorsoSensorValues = self.values
    #         np.save('data/TorsoSensorValues.npy',TorsoSensorValues)
    #     if g == 3:
    #         frontLegSensorValues = self.values
    #         np.save('data/frontLegSensorValues.npy',frontLegSensorValues)

        def Save_Values(self, name):
            self.linkName = name
            if g == 1:
                backLegSensorValues = self.values
                np.save('data/backLegSensorValues.npy',backLegSensorValues)
            if g == 2:
                TorsoSensorValues = self.values
                np.save('data/TorsoSensorValues.npy',TorsoSensorValues)
            if g == 3:
                frontLegSensorValues = self.values
                np.save('data/frontLegSensorValues.npy',frontLegSensorValues)
      

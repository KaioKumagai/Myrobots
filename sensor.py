import pybullet as p
import time
import pybullet_data
# import world
import robot
import pyrosim.pyrosim as pyrosim
import numpy as np
class SENSOR:

    def __init__(self, name):

        self.linkName = name
        self.values = np.zeros(2500)

    def Get_Value(self, t):

        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

        if t == 999:
            g =+ 1

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
      

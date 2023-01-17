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
        self.values = np.zeros(1000)

    def Get_Value(self, t):
        # self.linkName = name

        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

        # print(f'{self.linkName=}: {self.values[t]=}')
        if t == 999:
            # print('World')
            print(self.values)

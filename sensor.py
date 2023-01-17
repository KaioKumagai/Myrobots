import pybullet as p
import time
import pybullet_data
import world
import robot
import pyrosim.pyrosim as pyrosim

class SENSOR:

    def __init__(self, name):

        self.linkName = name

        pass

    def Get_Value(self):
        self.robot.values = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
import numpy as np
import constants as c
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import robot

class MOTOR:

    def __init__(self, name):

        self.jointName = name
        self.Prepare_To_Act()

        self.amplitude_backLeg = c.amplitude_backLeg
        print(self.jointName)
        if self.jointName == b'Torso_FrontLeg':
            self.frequency_backLeg = (1/2)*c.frequency_backLeg
        else:
            self.frequency_backLeg = c.frequency_backLeg
        # self.frequency_backLeg = (1/2)*c.frequency_backLeg
        self.offset_backLeg = c.phaseOffset_backLeg
        self.targetAngles_backLeg = np.zeros(1000)
        a = np.linspace(0, 2*np.pi, 1000)
        for i in range(1000):
            self.targetAngles_backLeg[i] = self.amplitude_backLeg*np.sin(a[i]*self.frequency_backLeg + self.offset_backLeg)

        # self.amplitude_frontLeg = c.amplitude_frontLeg
        # self.frequency_frontLeg = c.frequency_frontLeg
        # self.offset_frontLeg = c.phaseOffset_frontLeg
        # self.targetAngles_frontLeg = np.zeros(1000)
        # a = np.linspace(0, 2*np.pi, 1000)
        # for i in range(1000):
        #     self.targetAngles_frontLeg[i] = self.amplitude_frontLeg*np.sin(a[i]*self.frequency_frontLeg + self.offset_frontLeg)
        # self.values = np.zeros(1000)

    def Prepare_To_Act(self):
        pass

    def Set_Value(self, robotId, t):
            
            pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition= self.targetAngles_backLeg[t],
            maxForce = 500)

            
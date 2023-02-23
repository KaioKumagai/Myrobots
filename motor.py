import numpy as np
import constants as c
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import robot

class MOTOR:

    def __init__(self, name):
        pass
        self.jointName = name
        # # self.Prepare_To_Act()

        # self.amplitude_backLeg = c.amplitude_backLeg
        # # print(self.jointName)
        # if self.jointName == "Torso_FrontLeg":
        #     self.frequency_backLeg = (1/2)*c.frequency_backLeg
        # else:
        #     self.frequency_backLeg = c.frequency_backLeg
        # # self.frequency_backLeg = (1/2)*c.frequency_backLeg
        # self.offset_backLeg = c.phaseOffset_backLeg
        # self.targetAngles_backLeg = np.zeros(2500)
        # a = np.linspace(0, 2*np.pi, 2500)
        # for i in range(2500):
        #     self.targetAngles_backLeg[i] = self.amplitude_backLeg*np.sin(a[i]*self.frequency_backLeg + self.offset_backLeg)




    def Set_Value(self, robotId, desiredAngle):
            
            pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            # targetPosition= self.targetAngles_backLeg[desiredAngle],
            targetPosition = desiredAngle,
            maxForce = 50)

            
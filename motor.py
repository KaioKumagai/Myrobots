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

    def Set_Value(self, robotId, desiredAngle):
            
            pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = desiredAngle,
            maxForce = 50)

            
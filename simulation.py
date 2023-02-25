import pybullet as p
import time
import pybullet_data
import world
import robot
import pyrosim.pyrosim as pyrosim
import sensor
import sys


# physicsClient = p.connect(p.GUI)

# p.setAdditionalSearchPath(pybullet_data.getDataPath())

# p.setGravity(0,0,-9.8)

# self.planeId = p.loadURDF("plane.urdf")
#         p.loadSDF("world.sdf")

class SIMULATION:

    def __init__(self, directOrGUI, solutionID):

        self.directOrGUI = directOrGUI

        if directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        p.setGravity(0,0,-9.8)

        self.world = world.WORLD()
        self.robot = robot.ROBOT(solutionID)
        # self.sensor = sensor.SENSOR()

    def Run(self):
        for t in range(2500):

            # print(t)
            # g = 0
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Think()
            self.robot.Act(t)
            
            
            # self.robot.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            # self.robot.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

            # pyrosim.Set_Motor_For_Joint(
            # bodyIndex = self.robot.robotId,
            # jointName = b'Torso_BackLeg',
            # controlMode = p.POSITION_CONTROL,
            # targetPosition= self.robot.targetAngles_backLeg[t],
            # maxForce = 500)

            # pyrosim.Set_Motor_For_Joint(
            # bodyIndex = self.robot.robotId,
            # jointName = b'Torso_FrontLeg',
            # controlMode = p.POSITION_CONTROL,
            # targetPosition= self.robot.targetAngles_frontLeg[t],
            # maxForce = 500)

            # self.sensor.Save_Values(self)
            if self.directOrGUI == "GUI":
                time.sleep(1/240)   
    
    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):

        p.disconnect()


        

        
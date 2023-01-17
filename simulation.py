import pybullet as p
import time
import pybullet_data
import world
import robot
import pyrosim.pyrosim as pyrosim

class SIMULATION:

    def __init__(self):

        physicsClient = p.connect(p.GUI)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        p.setGravity(0,0,-9.8)

        self.world = world.WORLD()
        self.robot = robot.ROBOT()

    def Run(self):
        for t in range(1000):

            # print(t)
            p.stepSimulation()
            self.robot.Sense(t)
            
            
            # self.robot.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            # self.robot.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

            pyrosim.Set_Motor_For_Joint(
            bodyIndex = self.robot.robotId,
            jointName = b'Torso_BackLeg',
            controlMode = p.POSITION_CONTROL,
            targetPosition= self.robot.targetAngles_backLeg[t],
            maxForce = 500)

            pyrosim.Set_Motor_For_Joint(
            bodyIndex = self.robot.robotId,
            jointName = b'Torso_FrontLeg',
            controlMode = p.POSITION_CONTROL,
            targetPosition= self.robot.targetAngles_frontLeg[t],
            maxForce = 500)

            time.sleep(1/60)

    def __del__(self):

        p.disconnect()


        

        
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
from tempfile import TemporaryFile

physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)

planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)

amplitude_backLeg = np.pi/4
frequency_backLeg = 15
phaseOffset_backLeg = np.pi/8
# targetAngles = (np.pi/4)*np.sin(np.linspace(0, 2*np.pi, 1000))
targetAngles_backLeg = np.zeros(1000)
a = np.linspace(0, 2*np.pi, 1000)
for i in range(1000):
    targetAngles_backLeg[i] = amplitude_backLeg*np.sin(a[i]*frequency_backLeg + phaseOffset_backLeg)
# print(targetAngles)

amplitude_frontLeg = np.pi/8
frequency_frontLeg = 15
phaseOffset_frontLeg = 0
# targetAngles = (np.pi/4)*np.sin(np.linspace(0, 2*np.pi, 1000))
targetAngles_frontLeg = np.zeros(1000)
a = np.linspace(0, 2*np.pi, 1000)
for i in range(1000):
    targetAngles_frontLeg[i] = amplitude_frontLeg*np.sin(a[i]*frequency_frontLeg + phaseOffset_frontLeg)

outfile = TemporaryFile()

for t in range(1000):
    p.stepSimulation()
    
    backLegSensorValues[t] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[t] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotId,
    jointName = b'Torso_BackLeg',
    controlMode = p.POSITION_CONTROL,
    # targetPosition = (random.random()-0.5)*np.pi/10,
    targetPosition= targetAngles_backLeg[t],
    maxForce = 500)

    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotId,
    jointName = b'Torso_FrontLeg',
    controlMode = p.POSITION_CONTROL,
    # targetPosition = (random.random()-0.5)*np.pi/10,
    targetPosition= targetAngles_frontLeg[t],
    maxForce = 500)

    time.sleep(1/60)
    # print (t)

# print(backLegSensorValues)
np.save('data/backLegSensorValues.npy', backLegSensorValues)
np.save('data/frontLegSensorValues.npy', frontLegSensorValues)
np.save('data/targetPosition_frontLeg.npy', targetAngles_frontLeg)
np.save('data/targetPosition_backLeg.npy', targetAngles_backLeg)
    

p.disconnect()
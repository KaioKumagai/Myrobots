import sys
from simulation import SIMULATION
from robot import ROBOT


# import pyrosim.pyrosim as pyrosim
# import numpy as np
# import random
# import constants as c
# from tempfile import TemporaryFile
if __name__ == '__main__':
    directOrGUI =  sys.argv[1]
    simulation = SIMULATION(directOrGUI)
    simulation.Run()
    simulation.Get_Fitness()

# directOrGUI =  sys.argv[1]
# simulation = SIMULATION(directOrGUI)
# simulation.Run()
# simulation.Get_Fitness()



# planeId = p.loadURDF("plane.urdf")
# robotId = p.loadURDF("body.urdf")

# p.loadSDF("world.sdf")
# pyrosim.Prepare_To_Simulate(robotId)

# backLegSensorValues = np.zeros(1000)
# frontLegSensorValues = np.zeros(1000)

# targetAngles_backLeg = np.zeros(1000)
# a = np.linspace(0, 2*np.pi, 1000)
# for i in range(1000):
#     targetAngles_backLeg[i] = c.amplitude_backLeg*np.sin(a[i]*c.frequency_backLeg + c.phaseOffset_backLeg)


# targetAngles_frontLeg = np.zeros(1000)
# a = np.linspace(0, 2*np.pi, 1000)
# for i in range(1000):
#     targetAngles_frontLeg[i] = c.amplitude_frontLeg*np.sin(a[i]*c.frequency_frontLeg + c.phaseOffset_frontLeg)

# outfile = TemporaryFile()

# for t in range(1000):
#     p.stepSimulation()
    
#     backLegSensorValues[t] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     frontLegSensorValues[t] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

#     pyrosim.Set_Motor_For_Joint(
#     bodyIndex = robotId,
#     jointName = b'Torso_BackLeg',
#     controlMode = p.POSITION_CONTROL,
#     targetPosition= targetAngles_backLeg[t],
#     maxForce = 500)

#     pyrosim.Set_Motor_For_Joint(
#     bodyIndex = robotId,
#     jointName = b'Torso_FrontLeg',
#     controlMode = p.POSITION_CONTROL,
#     targetPosition= targetAngles_frontLeg[t],
#     maxForce = 500)

#     time.sleep(1/60)

# np.save('data/backLegSensorValues.npy', backLegSensorValues)
# np.save('data/frontLegSensorValues.npy', frontLegSensorValues)
# np.save('data/targetPosition_frontLeg.npy', targetAngles_frontLeg)
# np.save('data/targetPosition_backLeg.npy', targetAngles_backLeg)
    

# p.disconnect()
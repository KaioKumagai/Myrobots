import numpy as np
import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import random
import constants as c
import os
import time

class SOLUTION:

    def __init__(self, nextAvailableID):

        self.weights = np.random.rand(c.numSensorNeurons,c.numMotorNeurons)
        # self.weights = np.random.rand(3,2)
        self.weights = self.weights * 2 - 1
        # print(self.weights)
        self.myID = nextAvailableID

    def set_ID(self, newID):
        self.myID = newID
        pass

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("start /B py simulate.py " + directOrGUI + " " + str(self.myID))
        

    def  Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness" +str(self.myID)+ ".txt"):

            time.sleep(0.02)

        f = open("fitness" + str(self.myID) + ".txt", "r")
        self.fitness = float(f.read())
        
        f.close()
        os.system(f"del fitness{str(self.myID)}.txt")
        

    def Create_World(self):

        if self.myID == 0:
            pyrosim.Start_SDF("world.sdf")

            

            length = 1
            width = 1
            height = 1
    
            pyrosim.Send_Cube(name="Box", pos=[3,3,0.5] , size=[length,width,height]) 

            pyrosim.End()

        while not os.path.exists("world.sdf"):
            time.sleep(0.01)

        pass

    def Create_Body(self):
        if self.myID == 0:
            pyrosim.Start_URDF("body.urdf")
            pyrosim.Send_Cube(name="Torso", pos=c.Link0 , size=[c.length,c.width,c.height])  
            pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = c.Link0_Link1)
            pyrosim.Send_Cube(name="BackLeg", pos=c.Link1 , size=[c.length,c.width,c.height]) 
            pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = c.Link0_Link2)
            pyrosim.Send_Cube(name="FrontLeg", pos=c.Link2 , size=[c.length,c.width,c.height]) 
            pyrosim.End()  
        
            
        while not os.path.exists("body.urdf"):
            time.sleep(0.01)
        

    def Create_Brain(self):
        brainID = 'brain' + str(self.myID) + '.nndf'
        pyrosim.Start_NeuralNetwork(brainID)
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")   
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")   
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")    
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")
        for currentRow in range(c.numSensorNeurons):
        # for currentRow in range(2):
            for currentColumn in range(c.numMotorNeurons ):
            # for currentColumn in range(1):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , 
                                    #  targetNeuronName = currentColumn + c.numSensorNeurons, 
                                      targetNeuronName = currentColumn + 3, 
                                     weight = self.weights[currentRow][currentColumn] )
       
        pyrosim.End()  
        

    def Mutate(self):
        randomRow =  random.randint(0,c.numSensorNeurons-1)
        randomColumn = random.randint(0,c.numMotorNeurons-1)
        # randomRow =  random.randint(0,2)
        # randomColumn = random.randint(0,1)
        self.weights[randomRow,randomColumn] =  random.gauss()
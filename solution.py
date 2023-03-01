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
            pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", 
                               position = c.Link0_Link1, jointAxis = "1 0 0")        
            pyrosim.Send_Cube(name="BackLeg", pos=c.Link1 , size=[c.backleglength,c.backlegwidth,c.backlegheight])

            pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute",
                               position = c.Link0_Link2, jointAxis = "1 0 0")            
            pyrosim.Send_Cube(name="FrontLeg", pos=c.Link2 , size=[c.frontleglength,c.frontlegwidth,c.frontlegheight]) 

            pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", 
                               position = c.Link0_Link3, jointAxis = "0 1 0")            
            pyrosim.Send_Cube(name="LeftLeg", pos=c.Link3 , size=[c.leftleglength,c.leftlegwidth,c.leftlegheight])

            pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", 
                               position = c.Link0_Link4, jointAxis = "0 1 0")            
            pyrosim.Send_Cube(name="RightLeg", pos=c.Link4 , size=[c.rightleglength,c.rightlegwidth,c.rightlegheight]) 

            pyrosim.Send_Joint( name = "FrontLeg_FrontLowerLeg" , parent= "FrontLeg" , child = "FrontLowerLeg" , type = "revolute", 
                               position = c.Link2_Link5, jointAxis = "1 0 0")            
            pyrosim.Send_Cube(name="FrontLowerLeg", pos=c.Link5 , size=[c.frontlowerleglength,c.frontlowerlegwidth,c.frontlowerlegheight]) 

            pyrosim.Send_Joint( name = "BackLeg_BackLowerLeg" , parent= "BackLeg" , child = "BackLowerLeg" , type = "revolute", 
                               position = c.Link1_Link6, jointAxis = "1 0 0")
            pyrosim.Send_Cube(name="BackLowerLeg", pos=c.Link6 , size=[c.backlowerleglength,c.backlowerlegwidth,c.backlowerlegheight]) 

            pyrosim.Send_Joint( name = "RightLeg_RightLowerLeg" , parent= "RightLeg" , child = "RightLowerLeg" , type = "revolute", 
                               position = c.Link4_Link7, jointAxis = "0 1 0")
            pyrosim.Send_Cube(name="RightLowerLeg", pos=c.Link7 , size=[c.rightlowerleglength,c.rightlowerlegwidth,c.rightlowerlegheight]) 

            pyrosim.Send_Joint( name = "LeftLeg_LeftLowerLeg" , parent= "LeftLeg" , child = "LeftLowerLeg" , type = "revolute", 
                               position = c.Link3_Link8, jointAxis = "0 1 0")
            pyrosim.Send_Cube(name="LeftLowerLeg", pos=c.Link8 , size=[c.leftlowerleglength,c.leftlowerlegwidth,c.leftlowerlegheight]) 

            pyrosim.End()  
        
            
        while not os.path.exists("body.urdf"):
            time.sleep(0.01)
        

    def Create_Brain(self):
        brainID = 'brain' + str(self.myID) + '.nndf'
        pyrosim.Start_NeuralNetwork(brainID)
        # pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")   
        # pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")   
        # pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")  
        # pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLeg") 
        # pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "RightLeg") 
        # pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "FrontLowerLeg") 
        # pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "BackLowerLeg") 
        # pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "RightLowerLeg") 
        # pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "LeftLowerLeg") 

        # pyrosim.Send_Motor_Neuron( name = 9 , jointName = "Torso_BackLeg")
        # pyrosim.Send_Motor_Neuron( name = 10 , jointName = "Torso_FrontLeg")
        # pyrosim.Send_Motor_Neuron( name = 11 , jointName = "Torso_LeftLeg")
        # pyrosim.Send_Motor_Neuron( name = 12 , jointName = "Torso_RightLeg")
        # pyrosim.Send_Motor_Neuron( name = 13 , jointName = "FrontLeg_FrontLowerLeg")
        # pyrosim.Send_Motor_Neuron( name = 14 , jointName = "BackLeg_BackLowerLeg")
        # pyrosim.Send_Motor_Neuron( name = 15 , jointName = "RightLeg_RightLowerLeg")
        # pyrosim.Send_Motor_Neuron( name = 16 , jointName = "LeftLeg_LeftLowerLeg")


        # pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")   
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "BackLowerLeg")   
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "FrontLowerLeg")  
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "LeftLowerLeg") 
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "RightLowerLeg") 
        # pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "FrontLowerLeg") 
        # pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "BackLowerLeg") 
        # pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "RightLowerLeg") 
        # pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "LeftLowerLeg") 

        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 5 , jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 6 , jointName = "Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron( name = 7 , jointName = "Torso_RightLeg")
        pyrosim.Send_Motor_Neuron( name = 8 , jointName = "FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 9 , jointName = "BackLeg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 10 , jointName = "RightLeg_RightLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 11 , jointName = "LeftLeg_LeftLowerLeg")

        for currentRow in range(c.numSensorNeurons):
        # for currentRow in range(2):
            for currentColumn in range(c.numMotorNeurons ):
            # for currentColumn in range(1):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , 
                                    #  targetNeuronName = currentColumn + c.numSensorNeurons, 
                                      targetNeuronName = currentColumn + c.numSensorNeurons, 
                                     weight = self.weights[currentRow][currentColumn] )
       
        pyrosim.End()  
        

    def Mutate(self):
        randomRow =  random.randint(0,c.numSensorNeurons-1)
        randomColumn = random.randint(0,c.numMotorNeurons-1)
        # randomRow =  random.randint(0,2)
        # randomColumn = random.randint(0,1)
        self.weights[randomRow,randomColumn] =  random.gauss()
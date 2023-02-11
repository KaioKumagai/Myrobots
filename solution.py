import numpy as np
import pyrosim.pyrosim as pyrosim
import pybullet_data
import pybullet as p
import random
import constants as c
import os

class SOLUTION:

    def __init__(self):

        self.weights = np.random.rand(3,2)
        # print(self.weights)
        self.weights = self.weights * 2 - 1

        # print(self.weights)
        # exit()

    def Evaluate(self):
        os.system("py simulate.py")
        f = open("fitness.txt", "r")
        self.fitness = float(f.read())
        # print(type(self.fitness))
        # print(self.fitness)
        f.close()
        

    def Create_World(self):
        # def __init__(self):

        pyrosim.Start_SDF("world.sdf")

        length = 1
        width = 1
        height = 1
    
        pyrosim.Send_Cube(name="Box", pos=[3,3,0.5] , size=[length,width,height]) 

        pyrosim.End()

        
        self.planeId = p.loadURDF("plane.urdf")
        p.loadSDF("world.sdf")
        
        

        pass

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=c.Link0 , size=[c.length,c.width,c.height])  
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = c.Link0_Link1)
        pyrosim.Send_Cube(name="BackLeg", pos=c.Link1 , size=[c.length,c.width,c.height]) 
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = c.Link0_Link2)
        pyrosim.Send_Cube(name="FrontLeg", pos=c.Link2 , size=[c.length,c.width,c.height]) 

        pyrosim.End()  

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")   
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")   
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")    
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")
        # for neuron in NEURON.neurons:
        for currentRow in [0,1,2]:
            for currentColumn in [0,1]:
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn +3, weight = self.weights[currentRow][currentColumn] )
       
        pyrosim.End()  
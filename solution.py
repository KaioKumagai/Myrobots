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

        self.weights = np.random.rand(3,2)
        # print(self.weights)
        self.weights = self.weights * 2 - 1
        self.myID = nextAvailableID

        # print(self.weights)
        # exit()

    def set_ID(self, newID):
        self.myID = newID
        pass

    def Evaluate(self, directOrGUI):
        
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        # os.system("py simulate.py " + directOrGUI)
        os.system("start /B py simulate.py " + directOrGUI + " " + str(self.myID))

        while not os.path.exists("fitness" +str(self.myID)+ ".txt"):

            time.sleep(0.01)

        f = open("fitness" +str(self.myID)+ ".txt", "r")
        self.fitness = float(f.read())
        print(f"fitness is {self.fitness}")
        # print(type(self.fitness))
        # print(self.fitness)
        f.close()

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        # os.system("py simulate.py " + directOrGUI)
        os.system("start /B py simulate.py " + directOrGUI + " " + str(self.myID))
        

    def  Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness" +str(self.myID)+ ".txt"):

            time.sleep(0.01)

        fitnessID = "fitness" +str(self.myID)+ ".txt"
        f = open("fitness" +str(self.myID)+ ".txt", "r")
        self.fitness = float(f.read())
        # print(f"fitness is {self.fitness}")
        
        f.close()
        # del "fitness" + str(self.myID) + ".txt"
        os.system(f"del fitness{str(self.myID)}.txt")
        # del fitnessID
        

    def Create_World(self):
        # def __init__(self):
        # physicsClient = p.connect(p.GUI)

        # p.setAdditionalSearchPath(pybullet_data.getDataPath())

        # p.setGravity(0,0,-9.8)

        pyrosim.Start_SDF("world.sdf")

        length = 1
        width = 1
        height = 1
    
        pyrosim.Send_Cube(name="Box", pos=[3,3,0.5] , size=[length,width,height]) 

        pyrosim.End()

        
        # self.planeId = p.loadURDF("plane.urdf")
        # p.loadSDF("world.sdf")
        
        

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
        brainID = 'brain' + str(self.myID) + '.nndf'
        # print(f'BrainID is {brainID}')
        pyrosim.Start_NeuralNetwork(brainID)
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")   
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")   
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")    
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")
        # for neuron in NEURON.neurons:
        for currentRow in [0,1,2]:
            for currentColumn in [0,1]:
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , 
                                     targetNeuronName = currentColumn +3, 
                                     weight = self.weights[currentRow][currentColumn] )
       
        pyrosim.End()  

    def Mutate(self):
        randomRow =  random.randint(0,2)
        randomColumn = random.randint(0,1)
        # self.weights[randomRow,randomColumn] =  random.random() * 2 - 1
        self.weights[randomRow,randomColumn] =  random.gauss()
        # print("this happened")
        # pass
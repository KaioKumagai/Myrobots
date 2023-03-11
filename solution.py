import numpy as np
import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import random
import constants as c
import os
import time

class SOLUTION:

    Links_with_Sensors = []
    Links_Dimensions = {}
    Links_Min_Max = {}
    
    def __init__(self, nextAvailableID):

        
        self.myID = nextAvailableID
        self.Links_with_Sensors = []
        self.Links_Dimensions = {}
        self.Number_of_Sensors = 0
        self.counter_for_motors = 0
        

    def set_ID(self, newID):
        self.myID = newID
        
    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("start /B py simulate.py " + directOrGUI + " " + str(self.myID))
        

    def  Wait_For_Simulation_To_End(self):
        while True:
            while not os.path.exists("fitness" +str(self.myID)+ ".txt"):
                time.sleep(0.001)

            try:
                f = open("fitness" + str(self.myID) + ".txt", "r")
                break
            except Exception as e:
                print("Caught file permission race condition")
                time.sleep(0.01)
                continue;

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


        pass
    

    def diff(awlf,prev, new):
                    dic = {'x': [1,0,0], 'y': [0,1,0], 'z': [0,0,1], '-x': [-1,0,0], '-y':[0,-1,0], '-z':[0,0,-1]}
                    prev = dic[prev]
                    new = dic[new]
                    if prev == new:
                        return new
                    if prev == [1,0,0] and new == [-1,0,0] or prev == [-1,0,0] and new == [1,0,0] or prev == [0,1,0] and new == [0,-1,0] or prev == [0,-1,0] and new == [0,1,0] or prev == [0,0,1] and new == [0,0,-1] or prev==[0,0,-1] and new == [0,0,1]:
                        return None
                    return [(prev[i]+new[i])/2 for i in [0,1,2]]

    def Create_Body(self):
        if self.myID == 0:
            length = 1
            width = 1
            height = 1
            altitude = 0.5
            type_movement = 'revolute'

            # First cube
            if random.randint(0,1):
                self.Links_with_Sensors.append(1)
            else:
                self.Links_with_Sensors.append(0)
            
            direction = random.choice(['x', 'y', 'z', '-x', '-y', '-z'])
            direction0 = direction
            pyrosim.Start_URDF("body.urdf")
            
            for i in range(1,c.Number_of_Links):
                Parent_Name = 'Link' + str(i)
                Child_Name = 'Link' + str(i+1)
                Joint_Name = Parent_Name + '_' + Child_Name
                
                jointAxis = "0 1 0"
                
                # child_length = 1
                # child_width = 1
                # child_height = 1
                child_length = random.random()
                child_width = random.random()
                child_height = random.random()


                for link in range(1,c.Number_of_Links):
                    if link == 0:
                        self.Links_Dimensions[0] = [length, width, altitude]
                    else:
                        self.Links_Dimensions[link] = [child_length,child_width,child_height]  
                
                parent_dimentions = self.Links_Dimensions[i]
                parent_length = parent_dimentions[0]
                parent_width = parent_dimentions[1]
                parent_height = parent_dimentions[2]                          

                if direction == 'x':
                    Link_position = [child_length/2,0,0]
                if direction =='-x':
                    Link_position = [-child_length/2,0,0]
                if direction == 'y':
                    Link_position = [0, child_width/2, 0]
                if direction == '-y':
                    Link_position = [0, -child_width/2, 0]
                if direction == 'z':
                    Link_position = [0,0,child_height/2]
                if direction == '-z':
                    Link_position = [0,0,-child_height/2]
                
                

                dif = self.diff(direction, direction:=random.choice(['x', 'y', 'z', '-x', '-y', '-z']))
                while dif == None:
                    print('Happening')
                    dif = self.diff(direction, direction:=random.choice(['x', 'y', 'z', '-x', '-y', '-z']))


                if direction == 'x':
                    Joint_position = [child_length * dif[i] for i in [0,1,2]]
                    Joint_position[1] = Joint_position[1] + random.uniform(-parent_width/2,parent_width/2)
                    Joint_position[2] = Joint_position[2] + random.uniform(-parent_height/2,parent_height/2)
                if direction =='-x':
                    Joint_position = [child_length * dif[i] for i in [0,1,2]]
                    Joint_position[1] = Joint_position[1] + random.uniform(-parent_width/2,parent_width/2)
                    Joint_position[2] = Joint_position[2] + random.uniform(-parent_height/2,parent_height/2)
                if direction == 'y':
                    Joint_position = [child_width * dif[i] for i in [0,1,2]]
                    Joint_position[0] = Joint_position[0] + random.uniform(-parent_length/2,parent_length/2)
                    Joint_position[2] = Joint_position[2] + random.uniform(-parent_height/2,parent_height/2)
                if direction == '-y':
                    Joint_position = [child_width * dif[i] for i in [0,1,2]]
                    Joint_position[0] = Joint_position[0] + random.uniform(-parent_length/2,parent_length/2)
                    Joint_position[2] = Joint_position[2] + random.uniform(-parent_height/2,parent_height/2)
                if direction == 'z':
                    Joint_position = [child_height * dif[i] for i in [0,1,2]]
                    Joint_position[0] = Joint_position[0] + random.uniform(-parent_length/2,parent_length/2)
                    Joint_position[1] = Joint_position[1] + random.uniform(-parent_width/2,parent_width/2)
                if direction == '-z':
                    Joint_position = [child_height * dif[i] for i in [0,1,2]]
                    Joint_position[0] = Joint_position[0] + random.uniform(-parent_length/2,parent_length/2)
                    Joint_position[1] = Joint_position[1] + random.uniform(-parent_width/2,parent_width/2)
                

                Link_size = [child_length, child_width, child_height]
                
                altitude = altitude - min(Joint_position[2],0)

                # nth Cube 
                if random.randint(0,1):
                    self.Links_with_Sensors.append(1) # sensor
                else:
                    self.Links_with_Sensors.append(0) # no sensor

                if self.Links_with_Sensors[i] == 1:
                    pyrosim.Send_Cube(  name = Parent_Name,
                                        pos = Link_position,
                                        size = Link_size,
                                        colorString = '    <color rgba="0 1 0 1.0"/>',
                                        colorName = '<material name="Green">') 
                    
                if self.Links_with_Sensors[i] == 0:
                    pyrosim.Send_Cube(  name = Parent_Name,
                                        pos = Link_position,
                                        size = Link_size,
                                        colorString = '    <color rgba="0 0 1 1.0"/>',
                                        colorName = '<material name="Blue">')   
                if i != c.Number_of_Links-1:    
                    pyrosim.Send_Joint( name = Joint_Name,
                                        parent = Parent_Name,
                                        child = Child_Name,
                                        type = type_movement, 
                                        position = Joint_position,
                                        jointAxis = jointAxis)
        
                # First Cube

                if direction0 == 'x':
                    Joint_position0 = [length/2,0,altitude]
                if direction0 == '-x':
                    Joint_position0 = [-length/2,0,altitude]
                if direction0 == 'y':
                    Joint_position0 = [0, width/2, altitude]
                if direction0 == '-y':
                    Joint_position0 = [0, -width/2, altitude]
                if direction0 == 'z':
                    Joint_position0 = [0,0,height/2+altitude]
                if direction0 == '-z':
                    Joint_position0 = [0,0,-height/2+altitude]
                    
                if self.Links_with_Sensors[0] == 1:
                    pyrosim.Send_Cube(  name = 'Link0',
                                        pos = [0, 0, altitude],
                                        size = [length, width, height],
                                        colorString = '    <color rgba="0 1 0 1.0"/>',
                                        colorName = '<material name="Green">') 
                    
                if self.Links_with_Sensors[0] == 0:
                    pyrosim.Send_Cube(  name = 'Link0',
                                        pos = [0, 0, altitude],
                                        size = [length, width, height],
                                        colorString = '    <color rgba="0 0 1 1.0"/>',
                                        colorName = '<material name="Blue">')   
                    
                pyrosim.Send_Joint(     name = 'Link0_Link1',
                                        parent = 'Link0',
                                        child = 'Link1',
                                        type = type_movement, 
                                        position = Joint_position0,
                                        jointAxis = jointAxis)
                pyrosim.End()  


    # def Create_Body(self):
    #     if self.myID == 0:
    #         for i in range(c.Number_of_Links):

    #             if random.randint(0,1) == 0:
    #                 self.Links_with_Sensors[i] = 1
    #             else:
    #                 self.Links_with_Sensors[i] = 0

    #             Parent_Name = 'Link' + str(i+1)
    #             Child_Name = 'Link' + str(i+2)
    #             Joint_Name = Parent_Name + '_' + Child_Name
    #             type = "revolute"
    #             jointAxis = "0 1 0"
    #             child_length = random.random()*5
    #             child_width = random.random()*5
    #             child_height = random.random()*5

    #             if i == 0:
    #                     Link_position = [0, 0, child_height]
    #                     Joint_position = [child_length/2,0,child_height]
    #             else:
    #                     Link_position = [child_length/2,0,0]
    #                     Joint_position = [child_length,0,0]
                
    #             parent_length = child_length
    #             parent_width = child_width 
    #             parent_height = child_height
    #             if self.Links_with_Sensors[i] == 1:
    #                 pyrosim.Send_Cube(name=Parent_Name, pos= Link_position , size=[parent_length, parent_width, parent_height],
    #                             colorString='    <color rgba="0 1 0 1.0"/>', colorName='<material name="Gren">') 
    #             if self.Links_with_Sensors[i] == 0:
    #                 pyrosim.Send_Cube(name=Parent_Name, pos= Link_position , size=[parent_length, parent_width, parent_height],
    #                             colorString='    <color rgba="0 0 1 1.0"/>', colorName='<material name="Blue">')  
                
                
    #             if i != c.Number_of_Links-1:
    #                 pyrosim.Send_Joint( name = Joint_Name , parent= Parent_Name , child = Child_Name , type = type, 
    #                                     position = Joint_position, jointAxis = jointAxis)  
    #         pyrosim.End()  

    def Create_Brain(self):
        brainID = 'brain' + str(self.myID) + '.nndf'
        pyrosim.Start_NeuralNetwork(brainID)
        

        for i in range(c.Number_of_Links):
            
            if self.Links_with_Sensors[i] == 1:
                name = str(self.counter_for_motors)
                self.counter_for_motors += 1
                linkName = "Link" + str(i)
                self.Number_of_Sensors += 1
                pyrosim.Send_Sensor_Neuron(name = name , linkName = linkName)
                          
        for i in range(c.Number_of_Links-1):
            name =self.counter_for_motors+i
            Parent_Name = 'Link' + str(i)
            Child_Name = 'Link' + str(i+1)
            Joint_Name = Parent_Name + '_' + Child_Name
            pyrosim.Send_Motor_Neuron( name = name , jointName = Joint_Name)
            
        self.weights = np.random.rand(self.Number_of_Sensors,c.Number_of_Links-1)
        for currentRow in range(self.Number_of_Sensors):
            for currentColumn in range(c.Number_of_Links-1 ):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , 
                                     targetNeuronName = currentColumn + self.Number_of_Sensors, 
                                     weight = self.weights[currentRow][currentColumn] )
       
        pyrosim.End()  
   
    # def Create_Brain(self):
    #     brainID = 'brain' + str(self.myID) + '.nndf'
    #     pyrosim.Start_NeuralNetwork(brainID)

    #     for i in range(c.Number_of_Links):
            
    #         if self.Links_with_Sensors[i] == 1:
    #             name = str(self.counter_for_motors)
    #             self.counter_for_motors += 1
    #             linkName = "Link" + str(i)
    #             Number_of_Sensors += 1
    #             pyrosim.Send_Sensor_Neuron(name = name , linkName = linkName)
                          
    #     for i in range(c.Number_of_Links-1):
    #         name =self.counter_for_motors+i
    #         Parent_Name = 'Link' + str(i+1)
    #         Child_Name = 'Link' + str(i+2)
    #         Joint_Name = Parent_Name + '_' + Child_Name
    #         pyrosim.Send_Motor_Neuron( name = name , jointName = Joint_Name)
    #         pass
    #     self.weights = np.random.rand(Number_of_Sensors,c.Number_of_Links-1)
    #     for currentRow in range(Number_of_Sensors):
    #         for currentColumn in range(c.Number_of_Links-1 ):
    #             pyrosim.Send_Synapse( sourceNeuronName = currentRow , 
    #                                  targetNeuronName = currentColumn + Number_of_Sensors, 
    #                                  weight = self.weights[currentRow][currentColumn] )
       
    #     pyrosim.End()  
        

    def Mutate(self):
        randomRow =  random.randint(0,self.Number_of_Sensors-1)
        randomColumn = random.randint(0,c.Number_of_Links-1)

        self.weights[randomRow,randomColumn] =  random.gauss()












         # def Create_Body(self):
    #     if self.myID == 0:
    #         pyrosim.Start_URDF("body.urdf")

    #         pyrosim.Send_Cube(name="Torso", pos=c.Link0 , size=[c.length,c.width,c.height])  
    #         pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", 
    #                            position = c.Link0_Link1, jointAxis = "1 0 0")        
    #         pyrosim.Send_Cube(name="BackLeg", pos=c.Link1 , size=[c.backleglength,c.backlegwidth,c.backlegheight])

    #         pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute",
    #                            position = c.Link0_Link2, jointAxis = "1 0 0")            
    #         pyrosim.Send_Cube(name="FrontLeg", pos=c.Link2 , size=[c.frontleglength,c.frontlegwidth,c.frontlegheight]) 

    #         pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", 
    #                            position = c.Link0_Link3, jointAxis = "0 1 0")            
    #         pyrosim.Send_Cube(name="LeftLeg", pos=c.Link3 , size=[c.leftleglength,c.leftlegwidth,c.leftlegheight])

    #         pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", 
    #                            position = c.Link0_Link4, jointAxis = "0 1 0")            
    #         pyrosim.Send_Cube(name="RightLeg", pos=c.Link4 , size=[c.rightleglength,c.rightlegwidth,c.rightlegheight]) 

    #         pyrosim.Send_Joint( name = "FrontLeg_FrontLowerLeg" , parent= "FrontLeg" , child = "FrontLowerLeg" , type = "revolute", 
    #                            position = c.Link2_Link5, jointAxis = "1 0 0")            
    #         pyrosim.Send_Cube(name="FrontLowerLeg", pos=c.Link5 , size=[c.frontlowerleglength,c.frontlowerlegwidth,c.frontlowerlegheight]) 

    #         pyrosim.Send_Joint( name = "BackLeg_BackLowerLeg" , parent= "BackLeg" , child = "BackLowerLeg" , type = "revolute", 
    #                            position = c.Link1_Link6, jointAxis = "1 0 0")
    #         pyrosim.Send_Cube(name="BackLowerLeg", pos=c.Link6 , size=[c.backlowerleglength,c.backlowerlegwidth,c.backlowerlegheight]) 

    #         pyrosim.Send_Joint( name = "RightLeg_RightLowerLeg" , parent= "RightLeg" , child = "RightLowerLeg" , type = "revolute", 
    #                            position = c.Link4_Link7, jointAxis = "0 1 0")
    #         pyrosim.Send_Cube(name="RightLowerLeg", pos=c.Link7 , size=[c.rightlowerleglength,c.rightlowerlegwidth,c.rightlowerlegheight]) 

    #         pyrosim.Send_Joint( name = "LeftLeg_LeftLowerLeg" , parent= "LeftLeg" , child = "LeftLowerLeg" , type = "revolute", 
    #                            position = c.Link3_Link8, jointAxis = "0 1 0")
    #         pyrosim.Send_Cube(name="LeftLowerLeg", pos=c.Link8 , size=[c.leftlowerleglength,c.leftlowerlegwidth,c.leftlowerlegheight]) 

    #         pyrosim.End()  


    
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
import pyrosim
import random
import numpy as np
            
Links_with_Sensors = {}
def Create_Body(self):
    if self.myID == 0:
        pyrosim.Start_URDF("body.urdf")
        for i in range(c.Number_of_Links):

            if random.randint(0,1) == 0:
                Links_with_Sensors[i] = 1
            else:
                 Links_with_Sensors[i] = 0

            Parent_Name = 'Link' + str(i+1)
            Child_Name = 'Link' + str(i+2)
            Joint_Name = Parent_Name + '_' + Child_Name
            type = "revolute"
            jointAxis = "0 1 0"
            # child_length = random.random()*5
            # child_width = random.random()*5
            # child_height = random.random()*5
            child_length = random.random()
            child_width = random.random()
            child_height = random.random()

            if i == 0:
                    Link_position = [0, 0, child_height]
                    Joint_position = [child_length/2,0,child_height]
            else:
                    Link_position = [child_length/2,0,0]
                    Joint_position = [child_length,0,0]
            
            parent_length = child_length
            parent_width = child_width 
            parent_height = child_height
            if Links_with_Sensors[i] == 1:
                pyrosim.Send_Cube(name=Parent_Name, pos= Link_position , size=[parent_length, parent_width, parent_height],
                              colorString='    <color rgba="0 1 0 1.0"/>', colorName='<material name="Gren">') 
                
            if Links_with_Sensors[i] == 0:
                pyrosim.Send_Cube(name=Parent_Name, pos= Link_position , size=[parent_length, parent_width, parent_height],
                              colorString='    <color rgba="0 0 1 1.0"/>', colorName='<material name="Blue">')  
               
            
            if i != c.Number_of_Links-1:
                pyrosim.Send_Joint( name = Joint_Name , parent= Parent_Name , child = Child_Name , type = type, 
                                    position = Joint_position, jointAxis = jointAxis) 
        pyrosim.End()  

def Create_Brain(self):
        brainID = 'brain' + str(self.myID) + '.nndf'
        pyrosim.Start_NeuralNetwork(brainID)
        Number_of_Sensors = 0
        counter_for_motors = 0

        for i in range(c.Number_of_Links):
            
            if Links_with_Sensors[i] == 1:
                name = str(counter_for_motors)
                counter_for_motors += 1
                linkName = "Link" + str(i)
                Number_of_Sensors += 1
                pyrosim.Send_Sensor_Neuron(name = name , linkName = linkName)
                          
        for i in range(c.Number_of_Links-1):
            name =counter_for_motors+i
            Parent_Name = 'Link' + str(i+1)
            Child_Name = 'Link' + str(i+2)
            Joint_Name = Parent_Name + '_' + Child_Name
            pyrosim.Send_Motor_Neuron( name = name , jointName = Joint_Name)
            
        self.weights = np.random.rand(Number_of_Sensors,c.Number_of_Links-1)
        for currentRow in range(Number_of_Sensors):
            for currentColumn in range(c.Number_of_Links-1 ):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , 
                                     targetNeuronName = currentColumn + Number_of_Sensors, 
                                     weight = self.weights[currentRow][currentColumn] )
       
        pyrosim.End()  

if __name__ == '__main__':
    import pyrosim.pyrosim as pyrosim
    import pybullet as p
    import pybullet_data
    import random
    import constants as c
    from types import SimpleNamespace
    from time import sleep
    from itertools import repeat

    self = SimpleNamespace(myID = 0)
    Create_Body(self)
    Create_Brain(self)

    physicsClient = p.connect(p.GUI)
    p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.setGravity(0,0,-9.8)
    p.loadURDF("plane.urdf")
    p.loadSDF("world.sdf")
    p.loadURDF('body.urdf')

    for t in repeat(None,5000):
        p.stepSimulation()
        sleep(1/500)
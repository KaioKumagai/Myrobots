import pyrosim.pyrosim as pyrosim
import constants as c

# length = 1
# width = 1
# height = 1

# Link0 = [1.0,0,1.5]
# Link1 = [-0.5,0,-0.5]
# Link2 = [0.5,0,-0.5]

# Link0_Link1 = [0.5,0,1]
# Link0_Link2 = [1.5,0,1]


def Generate_Body():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=c.Link0 , size=[c.length,c.width,c.height])  
    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = c.Link0_Link1)
    pyrosim.Send_Cube(name="BackLeg", pos=c.Link1 , size=[c.length,c.width,c.height]) 
    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = c.Link0_Link2)
    pyrosim.Send_Cube(name="FrontLeg", pos=c.Link2 , size=[c.length,c.width,c.height]) 

    pyrosim.End()   



def Generate_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")
    pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")   
    pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")   
    pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")    
    pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
    pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")
    pyrosim.End()  

Generate_Body()
Generate_Brain()



import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1

# x = 0
# y = 0
# z = 1.0

# def Create_World():
#     pyrosim.Start_SDF("world.sdf")

#     x = 3
#     y = 3
    
#     pyrosim.Send_Cube(name="Box", pos=[3,3,1] , size=[length,width,height]) 

#     pyrosim.End()


# x = 0
# y = 0
# z = 1.0

Link0 = [1.0,0,1.5]
Link1 = [-0.5,0,-0.5]
Link2 = [0.5,0,-0.5]
# Link2 = [0.5,0,0]
Link0_Link1 = [0.5,0,1]
Link0_Link2 = [1.5,0,1]
# Link1_Link2 = [1.5,0,0.5]

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=Link0 , size=[length,width,height])  
    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = Link0_Link1)
    pyrosim.Send_Cube(name="BackLeg", pos=Link1 , size=[length,width,height]) 
    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = Link0_Link2)
    pyrosim.Send_Cube(name="FrontLeg", pos=Link2 , size=[length,width,height]) 

    # pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[length,width,height]) 
    # pyrosim.Send_Cube(name="Leg", pos=[1,0,1.5] , size=[length,width,height]) 
    # pyrosim.Send_Joint( name = "Torso_Leg" , parent= "Torso" , child = "Leg" , type = "revolute", position = [1,0,1.5])
    pyrosim.End()   

# Create_World()

Create_Robot()



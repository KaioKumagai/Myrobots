import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim

class WORLD:

    def __init__(self):

        pyrosim.Start_SDF("world.sdf")

        length = 1
        width = 1
        height = 1
    
        pyrosim.Send_Cube(name="Box", pos=[3,3,1] , size=[length,width,height]) 

        pyrosim.End()

        
        self.planeId = p.loadURDF("plane.urdf")
        p.loadSDF("world.sdf")
        

        pass
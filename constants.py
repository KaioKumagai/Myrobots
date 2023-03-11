import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random

gravity = -9.8
amplitude_backLeg = np.pi/10
frequency_backLeg = 15
phaseOffset_backLeg = 0

amplitude_frontLeg = np.pi
frequency_frontLeg = 15
phaseOffset_frontLeg = 0
maxforce = 100

length = 1
width = 1
height = 1

frontleglength = 0.2
frontlegwidth = 1
frontlegheight = 0.2

backleglength = 0.2
backlegwidth = 1
backlegheight = 0.2

leftleglength = 1
leftlegwidth = 0.2
leftlegheight = 0.2

rightleglength = 1
rightlegwidth = 0.2
rightlegheight = 0.2

frontlowerleglength = 0.2
frontlowerlegwidth = 0.2
frontlowerlegheight = 1

backlowerleglength = 0.2
backlowerlegwidth = 0.2
backlowerlegheight = 1

rightlowerleglength = 0.2
rightlowerlegwidth = 0.2
rightlowerlegheight = 1

leftlowerleglength = 0.2
leftlowerlegwidth = 0.2
leftlowerlegheight = 1

Link0 = [0,0,1]
Link1 = [0,-0.5,0] #Backleg
Link2 = [0,0.5,0] #frontleg
Link3 = [-0.5,0,0] #leftleg
Link4 = [0.5,0,0] #rightleg
Link5 = [0,0,-0.5] #frontlowerleg
Link6 = [0,0,-0.5] #backlowerleg
Link7 = [0,0,-0.5] #rightlowerleg
Link8 = [0,0,-0.5] #leftlowerleg

Link0_Link1 = [0,-0.5,1] #torso to backleg
Link0_Link2 = [0,0.5,1] #torso to front leg
Link0_Link3 = [-0.5,0,1] #torso to left leg
Link0_Link4 = [0.5,0,1] #torso to right leg
Link2_Link5 = [0,1,0] #front leg to lower front leg
Link1_Link6 = [0,-1,0] #backleg to lower back leg
Link4_Link7 = [1,0,0] #rightleg to lower right leg
Link3_Link8 = [-1,0,0] #leftleg to lower left leg

numberOfGenerations = 1

populationSize = 1

timeofsimulation = 5000

motorJointRange = 0.5

# numSensorNeurons = 4
# numMotorNeurons = 8

Number_of_Links = 5
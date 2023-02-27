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

length = 1
width = 1
height = 1

Link0 = [1.0,0,1.5]
Link1 = [-0.5,0,-0.5]
Link2 = [0.5,0,-0.5]

Link0_Link1 = [0.5,0,1]
Link0_Link2 = [1.5,0,1]

numberOfGenerations = 100

populationSize = 10
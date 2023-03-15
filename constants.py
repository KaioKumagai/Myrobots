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

maxsize = 1
numberOfGenerations = 500

populationSize = 10

timeofsimulation = 2500

motorJointRange = 0.5

colorStrings = {True:'    <color rgba="0 0 1 1.0"/>', False:'    <color rgba="0 1 0 1.0"/>'}
colorNames = {True: '<material name="Blue">', False: '<material name="Green">'}

maxLinks = 10
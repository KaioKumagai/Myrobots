import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random

gravity = -9.8
amplitude_backLeg = np.pi/10
frequency_backLeg = 15
# phaseOffset_backLeg = np.pi/8
phaseOffset_backLeg = 0

amplitude_frontLeg = np.pi
frequency_frontLeg = 15
phaseOffset_frontLeg = 0
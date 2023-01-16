import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random

gravity = -9.8
amplitude_backLeg = np.pi/4
frequency_backLeg = 15
phaseOffset_backLeg = np.pi/8

amplitude_frontLeg = np.pi/8
frequency_frontLeg = 15
phaseOffset_frontLeg = 0
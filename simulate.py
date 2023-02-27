import sys
from simulation import SIMULATION
from robot import ROBOT
import pyrosim

if __name__ == '__main__':
    directOrGUI =  sys.argv[1]
    solutionID = sys.argv[2]
    simulation = SIMULATION(directOrGUI, solutionID)
    
    simulation.Run()
    simulation.Get_Fitness()


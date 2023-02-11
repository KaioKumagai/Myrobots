import solution
import pyrosim.pyrosim as pyrosim
import constants as c 

# copy

class HILL_CLIMBER:

    def __init__(self):
        self.parent = solution.SOLUTION()

        pass

    def Evolve(self):
        self.parent.Evaluate()
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()

        self.Mutate()

        self.child.Evaluate()

        self.Select()
    
    def Spawn(self):
        pass

    def Mutate(self):
        pass

    def Select(self):
        pass
        
            
        

    

  

  
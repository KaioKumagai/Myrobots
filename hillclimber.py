import solution
import pyrosim.pyrosim as pyrosim
import constants as c 
import copy

class HILL_CLIMBER:

    def __init__(self):
        self.parent = solution.SOLUTION()


    def Evolve(self):
        self.parent.Evaluate("GUI")
        # self.parent.Evaluate("DIRECT")
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()

        self.Mutate()

        self.child.Evaluate("DIRECT")
       
        self.Print()

        self.Select()
        
    
    def Spawn(self):

        self.child = copy.deepcopy(self.parent)
        

    def Mutate(self):

        self.child.Mutate()
        # print(f'Parents weights are {self.parent.weights}')
        # print(f'Parents weights are {self.child.weights}')
        # exit()
        

    def Select(self):
        # print(f'Parent fitness is {self.parent.fitness}')
        # print(f'Child fitness is {self.child.fitness}')
        if self.child.fitness < self.parent.fitness:
            self.parent = self.child
            print('this happened')
        # print(f'Winning generation is {self.parent.fitness}')
        # exit()
        # pass

    def Print(self):
        print(f'Parent fitness is {self.parent.fitness} and Child fitness is {self.child.fitness}')
        # pass

    def Show_Best(self):
        self.parent.Evaluate("GUI")
        pass
            
        

    

  

  
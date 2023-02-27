import solution
import pyrosim.pyrosim as pyrosim
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        for file in os.listdir():
            if file.startswith("brain"):
                os.system("del brain*.nndf")
            if file.startswith("fitness"):
                os.system("del fitness*.txt")
        self.parents = {}
        self.nextAvailableID = 0

        for i in range(c.populationSize):
            self.parents[i] = solution.SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1





    def Evolve(self):

        self.Evaluate(self.parents)

        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evaluate(self, solutions):
        self.solutions = solutions
        for solution in self.solutions:

            self.solutions[solution].Start_Simulation("DIRECT")

        for solution in self.solutions:

            self.solutions[solution].Wait_For_Simulation_To_End()

        
        pass


    def Evolve_For_One_Generation(self):
        self.Spawn()

        self.Mutate()

        self.Evaluate(self.children)

        self.Print()

        self.Select()



    def Spawn(self):

        self.children = {}

        for parent in self.parents:
            self.children[parent] = copy.deepcopy(self.parents[parent])
            self.children[parent].set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

        pass


    def Mutate(self):

        # self.child.Mutate()
        for child in self.children:
            self.children[child].Mutate()
        


    def Select(self):

        for parent in self.parents:
            if self.children[parent].fitness < self.parents[parent].fitness:
                self.parents[parent] = self.children[parent]

       

    def Print(self):
        for parent in self.parents:
            print("\n")
            print(f'Parent fitness is {self.parents[parent].fitness} and Child fitness is {self.children[parent].fitness}')
            print("\n")
       

    def Show_Best(self):
        current = 0
        for parent in self.parents:
            if self.parents[parent].fitness < current:
                current = parent
        self.parents[current].Start_Simulation("GUI")
        









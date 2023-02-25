import solution
import pyrosim.pyrosim as pyrosim
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        # self.parent = solution.SOLUTION()
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
            # print(self.parents)





    def Evolve(self):

        # for parent in self.parents:

        #     # self.parents[parent].Start_Simulation("GUI")
        #     self.parents[parent].Start_Simulation("DIRECT")

        # for parent in self.parents:

        #     self.parents[parent].Wait_For_Simulation_To_End()

        self.Evaluate(self.parents)
        # exit()

        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evaluate(self, solutions):
        self.solutions = solutions
        for solution in self.solutions:

            # self.parents[parent].Start_Simulation("GUI")
            self.solutions[solution].Start_Simulation("DIRECT")

        for solution in self.solutions:

            self.solutions[solution].Wait_For_Simulation_To_End()

        
        pass


    def Evolve_For_One_Generation(self):
        self.Spawn()

        self.Mutate()

        # self.child.Evaluate("DIRECT")
        self.Evaluate(self.children)
        # exit()

        self.Print()

        self.Select()



    def Spawn(self):

        self.children = {}

        for parent in self.parents:
            # print(parent)
            self.children[parent] = copy.deepcopy(self.parents[parent])
            # print(self.children)
            self.children[parent].set_ID(self.nextAvailableID)
            # print(f"after {self.children}")
            self.nextAvailableID += 1

        # print(self.children)
        # exit()


        # self.child = copy.deepcopy(self.parent)
        # self.child
        # self.child.Set_ID(self.nextAvailableID)
        # self.nextAvailableID += 1
        pass


    def Mutate(self):

        # self.child.Mutate()
        for child in self.children:
            # print(child)
            # exit()
            self.children[child].Mutate()
        
        # print(f'Parents weights are {self.parent.weights}')
        # print(f'Parents weights are {self.child.weights}')
        # exit()


    def Select(self):

        for parent in self.parents:
            if self.children[parent].fitness < self.parents[parent].fitness:
                self.parents[parent] = self.children[parent]
                # print('this happened')

       

    def Print(self):
        # print(f'Parent fitness is {self.parent.fitness} and Child fitness is {self.child.fitness}')
        for parent in self.parents:
            print("\n")
            print(f'Parent fitness is {self.parents[parent].fitness} and Child fitness is {self.children[parent].fitness}')
            print("\n")
       

    def Show_Best(self):
        current = 0
        for parent in self.parents:
            if self.parents[parent].fitness < current:
                current = parent
        self.parents[current].Evaluate("GUI")
        









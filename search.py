import os
import simulate
import parallelhillclimber
import matplotlib.pyplot as plt

phc = parallelhillclimber.PARALLEL_HILL_CLIMBER()
phc.Evolve()

phc.Get_Best_generations()
fitness_array = phc.Get_Best_generations()
plt.plot(fitness_array)

plt.xlabel('Number of Generations')
plt.ylabel('Fitness Value')
plt.legend()


phc.Show_Best()
plt.show()

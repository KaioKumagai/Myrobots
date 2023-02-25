import os
import generate
import simulate
# import hillclimber
import parallelhillclimber

# hc = hillclimber.HILL_CLIMBER()
phc = parallelhillclimber.PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()

# for i in range(1):
#     os.system("py generate.py")
#     os.system("py simulate.py")
    



import os
import generate
import simulate
import hillclimber

hc = hillclimber.HILL_CLIMBER()
hc.Evolve()
hc.Show_Best()

# for i in range(1):
#     os.system("py generate.py")
#     os.system("py simulate.py")
    



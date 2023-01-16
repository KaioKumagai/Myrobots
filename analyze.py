import numpy as np
import matplotlib.pyplot

backLegSensorValues = np.load('data/backLegSensorValues.npy')
frontLegSensorValues = np.load('data/frontLegSensorValues.npy')

# print(backLegSensorValues)
matplotlib.pyplot.plot(backLegSensorValues, label = 'Back Leg Sensor Values',linewidth = 3)
# matplotlib.pyplot.legend('Back Leg Sensor Values')
matplotlib.pyplot.plot(frontLegSensorValues, label = 'Front Leg Sensor Values')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
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

targetPostion_backLeg = np.load('data/targetPosition_backLeg.npy')
targetPostion_frontLeg = np.load('data/targetPosition_frontLeg.npy')
matplotlib.pyplot.plot(targetPostion_backLeg, label = 'Target Position for back leg',linewidth = 3)
matplotlib.pyplot.plot(targetPostion_frontLeg, label = 'Target Position for front leg',linewidth = 1)
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
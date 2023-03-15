import constants as c 
import numpy as np
import solution
import pickle

s = solution.SOLUTION(0)

# # ROBOT 1
# with open('links1.pkl', 'rb') as f:
#     links = pickle.load(f)
# with open('joints1.pkl', 'rb') as f:
#     joints = pickle.load(f)
# weights = np.load('weights1.npy')

# # ROBOT 2
# with open('links2.pkl', 'rb') as f:
#     links = pickle.load(f)
# with open('joints2.pkl', 'rb') as f:
#     joints = pickle.load(f)
# weights = np.load('weights2.npy')

# # ROBOT 3
# with open('links3.pkl', 'rb') as f:
#     links = pickle.load(f)
# with open('joints3.pkl', 'rb') as f:
#     joints = pickle.load(f)
# weights = np.load('weights3.npy')

# ROBOT 4
with open('links4.pkl', 'rb') as f:
    links = pickle.load(f)
with open('joints4.pkl', 'rb') as f:
    joints = pickle.load(f)
weights = np.load('weights4.npy')

# # ROBOT 5
# with open('links5.pkl', 'rb') as f:
#     links = pickle.load(f)
# with open('joints5.pkl', 'rb') as f:
#     joints = pickle.load(f)
# weights = np.load('weights5.npy')

## ROBOT 6
# with open('links6.pkl', 'rb') as f:
#     links = pickle.load(f)
# with open('joints6.pkl', 'rb') as f:
#     joints = pickle.load(f)
# weights = np.load('weights6.npy')

## ROBOT 7
# with open('links7.pkl', 'rb') as f:
#     links = pickle.load(f)
# with open('joints7.pkl', 'rb') as f:
#     joints = pickle.load(f)
# weights = np.load('weights7.npy')

## ROBOT 8
# with open('links8.pkl', 'rb') as f:
#     links = pickle.load(f)
# with open('joints8.pkl', 'rb') as f:
#     joints = pickle.load(f)
# weights = np.load('weights8.npy')

# # ROBOT 9
# with open('links9.pkl', 'rb') as f:
#     links = pickle.load(f)
# with open('joints9.pkl', 'rb') as f:
#     joints = pickle.load(f)
# weights = np.load('weights9.npy')

## ROBOT 10
# with open('links10.pkl', 'rb') as f:
#     links = pickle.load(f)
# with open('joints10.pkl', 'rb') as f:
#     joints = pickle.load(f)
# weights = np.load('weights10.npy')

s.links = links
s.joints = joints
s.weights = weights

s.Start_Simulation("GUI")

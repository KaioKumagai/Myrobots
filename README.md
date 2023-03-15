# Myrobots

*hg*

## **gjy**

## GIF / Teaser:

https://youtu.be/gMeGmIDQW6w

## Video:

https://youtu.be/AWHy4YXkl5I

## Methods:

How to run the code for evolution:
Download all files and open constants.py. There all required values should be changed such as number of population members, and for how many generations evolution should run. Then, search.py should be run



How to run the saved robots:
Uncomment the desired robot in testinground.py and run that program to see the robot performing.



## Diagrams:
Fitness graphs for all 10 saved robots may be found on the folder “Diagrams”. Furthermore, a diagram showing the process through which the robots were developed will also be included there.


How does the code work:
Running search.py creates a instance of the class parallel hill climber, which creates an object of the class solution. Create.py is used to create the position of all links and joints. Once the robot is generated a copy of it is created in parallel hillclimber that has one of the weights of its neural network changed, if that change leads to a better locomotion (further distance) the child robot is then selected. Then at the end, the robot with best design, and best weights is then selected and shown. Details on each file can be seen below:

## Results:
The result of the best robots obtained by running the program 10 times with a starting population of 10 robots that evolve through 500 generations can be seen in the folder “Diagrams”. The robots evolved by changing the weights in their neural networks. As time passed each robot with its own unique shape evolved to walk and at the end the one who walked the most and thus had the best shape and weights was chosen. Looking at the fitness graphs it is possible to see that there is a lowering trend, which shows that overall as generations passed fitness got lower. However it is important to note that there was a lot of variation between each change in weight, so the graph is not a clear line but a bunch of zig zags.

The 10 best robots also followed the trend of generally having a lower amount of links. Although up to 10 limbs not all of them had up to that big amount of links, to the contrary the majority had lower. This could possibly be due to the fact that the bigger the number of links the bigger the possibility that weights would be changed in “useless” parts of the body that would not contribute to moving. Thus, mutations in weights in smaller bodies was more prone to affect locomotion.

An example of bias that might have happened in the selection process is in the fitness function. The fitness function used only analyzes the x axis position of the robot, and locomotion only on that axis is observed. That means for example that a robot that topples over the y-axis and then moves in that direction would be eliminated. This could be solved by changing the fitness function into accounting for overall movement instead of movement in only one direction.

Yet another bias observed is that the complex bodies that did end up surviving through all 50000 simulations were unusually long. When they would topple over, most of the distance covered by them was resultant of their big length rather than because of their better locomotion.

## References:

https://www.reddit.com/r/ludobots/

Prof. Kriegman
T.A. Donna Hooshmand


import pyrosim.pyrosim as pyrosim
import constants as c
import numpy as np
import random

class Joint:
    def __init__(self, parent, child, pos, direction, updown, prev_joint_pos = None, type = 'revolute', axis = None, rel_or_abs = 'relative'):
        self.parent = str(parent)
        self.child = str(child)
        self.pos = pos
        self.direction = direction
        self.updown = updown
        self.type = type
        self.rel_or_abs = rel_or_abs
        self.neuron = True
        self.name = f'{parent}_{child}'
        
        if self.rel_or_abs == 'relative':
            self.pos_abs = [self.pos[i]+prev_joint_pos[i] for i in range(3)]
        else:
            self.pos_abs = self.pos

        if axis is None:
            self.jointAxis = random.choice(['1 0 0', '0 1 0', '0 0 1'])
        else:
            self.jointAxis = axis
    def Send_Joint(self):
        pyrosim.Send_Joint( name = self.name, parent = self.parent, child = self.child, type = self.type, position = self.pos, jointAxis = self.jointAxis)

    def Send_Motor_Neuron(self, count):
        pyrosim.Send_Motor_Neuron(name = count , jointName = self.name)
        return count+1


class Link:
    def __init__(self, name, pos, direction = None, updown = None, prev_joint_pos = None, size = None, rel_or_abs = 'relative', neuron = None):
        self.name = str(name)
        self.pos = pos
        self.direction = direction
        self.updown = updown
        self.rel_or_abs = rel_or_abs
        self.prev_joint_pos = prev_joint_pos
        if neuron is None:
            self.neuron = random.choice((True, False))
        else:
            self.neuron = neuron
        if size is None:
            self.size = [random.uniform(0,c.maxsize), random.uniform(0,c.maxsize), random.uniform(0,c.maxsize)]
        else:
            self.size = size
        if self.rel_or_abs == 'relative':
            self.pos_abs = [self.pos[i]+self.prev_joint_pos[i] for i in range(3)]
        else:
            self.pos_abs = self.pos

        limit0 = [self.pos_abs[0] - self.size[0]/2, self.pos_abs[0] + self.size[0]/2]
        limit1 = [self.pos_abs[1] - self.size[1]/2, self.pos_abs[1] + self.size[1]/2]
        limit2 = [self.pos_abs[2] - self.size[2]/2, self.pos_abs[2] + self.size[2]/2]

        self.available = set([(i, 1) for i in range(3)] + [(i,-1) for i in range(3)])
        
        self.limits = {'x': limit0, 'y': limit1, 'z': limit2}
        
        if self.direction is not None and self.updown is not None:
            self.available.remove((self.direction, self.updown))

    def Send_Sensor_Neuron(self, count: int) -> int:
        if self.neuron == True:
            pyrosim.Send_Sensor_Neuron(name = count , linkName = self.name)
            return count+1
        else:
            return count

    def Send_Cube(self) -> None:
        pyrosim.Send_Cube( name = self.name, pos = self.pos, size = self.size, colorString=c.colorStrings[self.neuron], colorName=c.colorNames[self.neuron])

def line_collision(linea, lineb, axis):
    if linea[axis][0] == lineb[axis][0]:
        return True
    if (lineb[axis][0] < linea[axis][1] and linea[axis][0] < lineb[axis][0]):
        return True 
    if (lineb[axis][0] < linea[axis][0] and linea[axis][0] < lineb[axis][1]):
        return True
    else:
        return False

def cube_collision(self, link):
    limits_self = self.limits
    limits_other = link.limits

    if (line_collision(limits_self, limits_other, 'x') and 
        line_collision(limits_self, limits_other, 'y') and 
        line_collision(limits_self, limits_other, 'z')):
        return True
    
    if line_collision(limits_self, limits_other, 'x'):
        if line_collision(limits_self, limits_other, 'y'):
            if line_collision(limits_self, limits_other, 'z'):
                return True

    return False 

def cube_collisions(self, links):
    collide = False
    for link in links:
        collide = cube_collision(self, link) or collide
        if collide:
            return collide
    return collide

def placel(joint):
    name = joint.child
    prev_joint_pos = joint.pos_abs
    direction, updown = joint.direction, joint.updown

    size = [random.uniform(0,c.maxsize), random.uniform(0,c.maxsize), random.uniform(0,c.maxsize)]
    location = [0,0,0]
    location[direction] = updown * size[direction]/2

    for axis in range(3):
        if axis != direction:
            location[axis] = random.choice((-1,1)) * np.random.rand() * size[axis]/2

    link = Link(
        name = name,
        pos = location,
        prev_joint_pos = prev_joint_pos,
        direction = direction,
        updown = updown,
        size = size
    )

    return link

def placej(links, child = None):
    
    if child is None:
        child = len(links)
    parent = random.randint(0,child-1)
    parent_link = links[parent]

    location = [0,0,0]
    direction, updown = random.choice(list(parent_link.available)) 
    location[direction] = updown * parent_link.size[direction]/2

    for axis in range(3):
        if axis != direction:
            location[axis] = random.choice((-1,1)) * np.random.rand() * parent_link.size[axis]/2

    if parent == 0:
        rel_or_abs = 'absolute'
        location = [location[i] + parent_link.pos_abs[i] for i in range(3)]
        prev_joint_pos = None
    else:
        rel_or_abs = 'relative'
        location = [location[i] + parent_link.pos[i] for i in range(3)]
        prev_joint_pos = parent_link.prev_joint_pos
    
    joint = Joint(
        parent = parent,
        child = child,
        pos = location,
        rel_or_abs = rel_or_abs,
        direction = direction,
        updown = updown,
        prev_joint_pos = prev_joint_pos
    )

    return joint

def Create_Body(my_id, nLinks, links, joints):
    if links is None and joints is None:
        size = [random.uniform(0,c.maxsize), random.uniform(0,c.maxsize), random.uniform(0,c.maxsize)]
        link0 = Link(
            name = 0,
            pos = [0,0,size[2]/2],
            prev_joint_pos = None,
            rel_or_abs = 'absolute',
            size = size
        )
        links = [link0]
        joints = []
        for i in range(1, nLinks):
            joint = placej(links)
            link = placel(joint)
            collide = cube_collisions(link, links)
            while collide:
                joint = placej(links)
                link = placel(joint)
                collide = cube_collisions(link, links)
            joints.append(joint)
            links.append(link)

        zmin = 0
        for link in links:
            zmin = min(zmin, link.limits['z'][0])
        pyrosim.Start_URDF(f'body{my_id}.urdf')
        for link in links:
            if link.rel_or_abs == 'absolute':
                link.pos[2] += -zmin
            link.Send_Cube()
        for joint in joints:
            if joint.rel_or_abs == 'absolute':
                joint.pos[2] += -zmin
            joint.Send_Joint()
        pyrosim.End()
        return links, joints
    else:
        pyrosim.Start_URDF(f'body{my_id}.urdf')
        for link in links:
            link.Send_Cube()
        for joint in joints:
            joint.Send_Joint()
        pyrosim.End()
        return links, joints

def Create_Brain(my_id, links, joints, weights):
    pyrosim.Start_NeuralNetwork(f'brain{my_id}.nndf')
    num = 0
    Number_Sensors = 0
    Number_Motors = len(joints)
    for link in links:
        if link.neuron:
            Number_Sensors += 1

    if Number_Sensors == 0:
        links[random.randint(0, len(links)-1)].neuron = True
        Number_Sensors+=1

    for link in links:
        if link.neuron:
            num = link.Send_Sensor_Neuron(num)
    for joint in joints:
        num = joint.Send_Motor_Neuron(num)

    if weights is None:
        weights = np.random.randn(Number_Sensors, Number_Motors)

    for sensor_num in range(Number_Sensors):
        for motor_num in range(Number_Sensors, Number_Sensors+Number_Motors):
            pyrosim.Send_Synapse( sourceNeuronName = sensor_num , targetNeuronName = motor_num , weight = weights[sensor_num][motor_num-Number_Sensors] )
    
    pyrosim.End()

    return weights
"""This is our particle file which contains all our approximation methods and the physics used to evolve our simulation in question"""
import numpy as np
import math
np.random.seed(seed=1943545)
'Our particle class'
class Particle():
    'Defines our values'
    def __init__(self,position=np.array([0, 0, 0], dtype=float),velocity=np.array([0, 0, 0], dtype=float),acceleration=np.array([0, 0, 0], dtype=float),name='Particle',mass=1):
        self.position =  np.array(position, dtype=float)
        self.velocity =  np.array(velocity, dtype=float)
        self.acceleration = np.array(acceleration, dtype=float)
        self.mass = mass
        self.name = name
    'Returns a string which includes our data in __init__'
    def __str__(self):
        return "Particle: {0}, Mass: {1:.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}".format(
            self.name, self.mass,self.position, self.velocity, self.acceleration
    )    
    
    'Update our position and velocity depending on the method selected'
    def update(self,deltaT,method,acceleration,force):
        'Update method, takes in 3 arguemnts, self, time interval and method type e.g. 1 being Eulers'
        if method == 1:
            'Eulers Method'
            self.acceleration=acceleration
            self.position = self.position + self.velocity*(deltaT)
            self.velocity = self.velocity + self.acceleration*(deltaT)
        elif method ==2:
            'Euler-Cromer Method'
            self.acceleration=acceleration
            self.velocity = self.velocity + self.acceleration*(deltaT)
            self.position = self.position + self.velocity*(deltaT) 
        else:
            self.momentum=self.momentum + force*deltaT
            self.velocity=(self.momentum/self.mass)
            self.position=self.position + self.velocity*deltaT

    
    def Momentum(self):
        self.momentum= self.mass*self.velocity
        return self.momentum

    def kineticEnergy(self):
        return 0.5*self.mass*(np.linalg.norm(self.velocity))**2
    

class ChargedParticle(Particle):
    def __init__(self, position=np.array([0, 0, 0], dtype=float), velocity=np.array([0, 0, 0], dtype=float), acceleration=np.array([0, 0, 0],dtype=float), name='Proton', mass=1,charge=1):
        super().__init__(position, velocity, acceleration, name, mass)
        self.charge=charge
    
    def __repr__(self):
        return 'Charged Particle: {0}, Mass: {1:12.3e}, Charge: {2:12.3e}, Position: {3}, Velocity: {4}, Acceleration: {5}'.format(self.name,self.mass,self.charge,self.position, self.velocity,self.acceleration)

class ProtonBunch():
    def __init__(self):
        pass
    def Generate_Bunch(self,proton_num):
        Bunch=[0,0]
        mean = [0, 0, 0]
        mean_2=[5,5,0]
        position_matrix = [[0.1, 0, 0], [0, 0.001, 0], [0, 0, 0.001]]
        velocity_matrix=[[5, 0, 0], [0, 5, 0], [0, 0, 0]]
        # using np.multinomial() method
        proton_positions = np.random.multivariate_normal(mean, position_matrix, proton_num)
        proton_velocities=np.random.multivariate_normal(mean_2, velocity_matrix, proton_num)
        Bunch[0]=proton_positions
        Bunch[1]=proton_velocities
        return Bunch

    def Averages(self,positions,velocities):
        Average_Positions=[np.mean(positions[:,0]),np.mean(positions[:,1]),np.mean(positions[:,2])]
        Average_Velocities=[np.mean(velocities[:,0]),np.mean(velocities[:,1]),np.mean(velocities[:,2])]
        return(Average_Positions,Average_Velocities)


PB=ProtonBunch()
Bunch=PB.Generate_Bunch(2)
print(Bunch)

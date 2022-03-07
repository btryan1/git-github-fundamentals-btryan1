"""This is our particle file which contains all our approximation methods and the physics used to evolve our simulation in question"""

import numpy as np
import math
from GeneralEMField2 import EMField
np.random.seed(seed=1943545)


class ChargedParticle():
    def __init__(self,position=np.array([0, 0, 0], dtype=float),velocity=np.array([0, 0, 0], dtype=float),acceleration=np.array([0, 0, 0], dtype=float),name='Charged Particle',mass=1,charge=1):
        self.position =  np.array(position, dtype=float)
        self.velocity =  np.array(velocity, dtype=float)
        self.acceleration = np.array(acceleration, dtype=float)
        self.mass = mass
        self.name = name
        self.charge=charge
    
    def __repr__(self):
        return 'Charged Particle: {0}, Mass: {1:12.3e}, Charge: {2:12.3e}, Position: {3}, Velocity: {4}, Acceleration: {5}'.format(self.name,self.mass,self.charge,self.position, self.velocity,self.acceleration)
    'Update our position and velocity depending on the method selected'

    def update(self,deltaT,method,acceleration):
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

    
    def Momentum(self):
        self.momentum= self.mass*self.velocity
        return self.momentum

    def kineticEnergy(self):
        return 0.5*self.mass*(np.linalg.norm(self.velocity))**2

class Proton(ChargedParticle):
    def __init__(self, position=np.array([0, 0, 0], dtype=float), velocity=np.array([0, 0, 0], dtype=float), acceleration=np.array([0, 0, 0],dtype=float), name='Proton', mass=1.6726219E-27,charge=1.602176634E-19):
        super().__init__(position, velocity, acceleration, name, mass,charge)
    def __repr__(self):
        return 'Charged Particle: {0}, Mass: {1:12.3e}, Charge: {2:12.3e}, Position: {3}, Velocity: {4}, Acceleration: {5}'.format(self.name,self.mass,self.charge,self.position, self.velocity,self.acceleration)


class ProtonBunch(EMField,Proton):
    def __init__(self,ElectricField , MagneticField):
        self.electric=ElectricField
        self.magnetic=MagneticField

    def Generate_Bunch(self,proton_num):
        Bunch=[]                      
        mean = [0, 0, 0]
        mean_2=[900,1100,0]
        position_matrix = [[0.01, 0, 0], [0, 0.01, 0], [0, 0, 0.01]]
        velocity_matrix=[[1000, 0, 0], [0, 1000, 0], [0, 0, 0]]
        # using np.multinomial() method
        proton_positions = np.random.multivariate_normal(mean, position_matrix, proton_num)
        proton_velocities=np.random.multivariate_normal(mean_2, velocity_matrix, proton_num)
        for i in range(proton_num):
            proton=Proton()
            proton.position=proton_positions[i]
            proton.velocity=proton_velocities[i]
            Bunch.append(proton)
        return Bunch
    
    def Bunch_Update(self,bunch,deltaT,method):
        BField= EMField(self.electric,self.magnetic)
        for i in range(len(bunch)):
            proton=bunch[i]
            acceleration=BField.getAcceleration(proton)
            proton.update(deltaT,method,acceleration)
            bunch[i]=proton
        return bunch
         
    def Orbit_Period(self,bunch):
        BField= EMField(self.electric,self.magnetic)
        Orbit_Period=[]
        for i in range(len(bunch)):
            Orbit_Period.append(BField.TimePeriod(bunch[i]))
        return (max(Orbit_Period))
        
    
    def Averages(self,positions,velocities):
        Average_Position=[np.mean(positions[:,0]),np.mean(positions[:,1]),np.mean(positions[:,2])]
        Average_Velocities=[np.mean(velocities[:,0]),np.mean(velocities[:,1]),np.mean(velocities[:,2])]
        return(Average_Position,Average_Velocities)

    def EnergySpread(self,velocities):
        T=[]
        for i in range(len(velocities)):
            T.append((1/2)*self.mass*np.linalg.norm(velocities))

    def Store_Positions(self,bunch):
        X=[]
        Y=[]
        Z=[]
        for i in range(len(bunch)):
            proton=bunch[i]
            X.append(proton.position[0])
            Y.append(proton.position[1])
            Z.append(proton.position[2])
        return (np.vstack((X,Y,Z)))


"""This is our particle file which contains all our approximation methods and the physics used to evolve our simulation in question"""

import numpy as np
import math

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

class AntiProton(ChargedParticle):
    def __init__(self, position=np.array([0, 0, 0], dtype=float), velocity=np.array([0, 0, 0], dtype=float), acceleration=np.array([0, 0, 0],dtype=float), name='Anit-Proton', mass=1.6726219E-27,charge=-1.602176634E-19):
        super().__init__(position, velocity, acceleration, name, mass,charge)
    def __repr__(self):
        return 'Charged Particle: {0}, Mass: {1:12.3e}, Charge: {2:12.3e}, Position: {3}, Velocity: {4}, Acceleration: {5}'.format(self.name,self.mass,self.charge,self.position, self.velocity,self.acceleration)

class DeuteriumNucleus(ChargedParticle):
    def __init__(self, position=np.array([0, 0, 0], dtype=float), velocity=np.array([0, 0, 0], dtype=float), acceleration=np.array([0, 0, 0],dtype=float), name='Deuterium Nucleus', mass=3.343580719E-27,charge=1.602176634E-19):
        super().__init__(position, velocity, acceleration, name, mass,charge)
    def __repr__(self):
        return 'Charged Particle: {0}, Mass: {1:12.3e}, Charge: {2:12.3e}, Position: {3}, Velocity: {4}, Acceleration: {5}'.format(self.name,self.mass,self.charge,self.position, self.velocity,self.acceleration)
    
class AntiDeuteriumNucleus(ChargedParticle):
    def __init__(self, position=np.array([0, 0, 0], dtype=float), velocity=np.array([0, 0, 0], dtype=float), acceleration=np.array([0, 0, 0],dtype=float), name='Anti Deuterium Nucleus', mass=3.343580719E-27,charge=-1.602176634E-19):
        super().__init__(position, velocity, acceleration, name, mass,charge)
    def __repr__(self):
        return 'Charged Particle: {0}, Mass: {1:12.3e}, Charge: {2:12.3e}, Position: {3}, Velocity: {4}, Acceleration: {5}'.format(self.name,self.mass,self.charge,self.position, self.velocity,self.acceleration)



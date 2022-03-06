from abc import ABC, abstractmethod
from cmath import pi
import numpy as np
import math
from Particle import ChargedParticle
import matplotlib.pyplot as plt

class GeneralEMField(ABC):

    @abstractmethod
    def __init__(self, ElectricField = np.array([0,0,0], dtype=float), MagneticField = np.array([0,0,0], dtype=float),particle = ChargedParticle(
    position=np.array([0, 0, 0]),
    velocity=np.array([0, 0, 0]),
    acceleration=np.array([0, 0, 0]),
    name="Proton",
    mass=1.6726219E-27,
    charge=1.602176634E-19
)):
        self.electric = np.array(ElectricField,dtype=float)
        self.magnetic = np.array(MagneticField, dtype=float)
        super(GeneralEMField, self).__init__()


    def __repr__(self):
        return 'EMField: E = {0}, B = {1}'.format(self.electric,self.magnetic)


    def getAcceleration(self,particle):
        lorentz = np.array(self.electric, dtype=float)
        lorentz+=np.cross(particle.velocity, self.magnetic)
        lorentz *= (particle.charge/particle.mass)
        return lorentz
    
class EMField(GeneralEMField):
        
    def __init__(self, ElectricField = np.array([0,0,0], dtype=float),MagneticField = np.array([0,0,0], dtype=float) ):
        super().__init__(ElectricField,MagneticField)
    
    def TimePeriod(self,particle):
        return (2*pi*particle.mass)/(particle.charge*np.linalg.norm(self.magnetic))
    
    def getForce(self,momentum,particle):
        lorentz = np.array(self.electric, dtype=float)
        lorentz+=np.cross(particle.charge*momentum/particle.mass, self.magnetic)
        return lorentz
    

time_percent=3.049968E-4    

from abc import ABC, abstractmethod
from cmath import pi
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import signal
class GeneralEMField(ABC):

    @abstractmethod
    def __init__(self, ElectricField = np.array([0,0,0], dtype=float), MagneticField = np.array([0,0,0], dtype=float)):
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
        
    def __init__(self,electric = np.array([0,0,0], dtype=float),magnetic = np.array([0,0,0], dtype=float)):
        super().__init__(electric,magnetic)
  
    def TimePeriod(self,particle):
        return (2*pi*particle.mass)/(particle.charge*np.linalg.norm(self.magnetic))

    def Cyclotron_Frequency(self,particle):
        return (particle.charge*np.linalg.norm(self.magnetic))/(particle.mass)

    def Square_Wave_Gen(self,f_cyclo):
        t = np.linspace(0, 0.05, 2000, endpoint=False)
        return signal.square(f_cyclo * t)


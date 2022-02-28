from abc import ABC, abstractmethod
from cmath import pi
import numpy as np
import math
import copy
from Particle import ChargedParticle
import matplotlib.pyplot as plt

particle = ChargedParticle(
    position=np.array([0, 0, 0]),
    velocity=np.array([5, 0, 0]),
    acceleration=np.array([0, 0, 0]),
    momentum=np.array([8.3631095e-27, 0, 0]),  
    name="Proton",
    mass=1.6726219E-27,
    charge=1.602176634E-19
)

class GeneralEMField(ABC):

    @abstractmethod
    def __init__(self, ElectricField = np.array([0,0,0], dtype=float), MagneticField = np.array([0,0,0], dtype=float)):
        self.electric = np.array(ElectricField,dtype=float)
        self.magnetic = np.array(MagneticField, dtype=float)
        super(GeneralEMField, self).__init__()


    def __repr__(self):
        return 'EMField: E = {0}, B = {1}'.format(self.electric,self.magnetic)


    def getAcceleration(self):
        lorentz = np.array(self.electric, dtype=float)
        lorentz+=np.cross(particle.velocity, self.magnetic)
        lorentz *= (particle.charge/particle.mass)
        return lorentz
    
class EMField(GeneralEMField):
        
    def __init__(self, ElectricField = np.array([0,0,0], dtype=float),MagneticField = np.array([0,0,0], dtype=float) ):
        super().__init__(ElectricField,MagneticField)
    
    def TimePeriod(self):
        return (2*pi*particle.mass)/(particle.charge*np.linalg.norm(self.magnetic))
    
    def getForce(self,momentum):
        lorentz = np.array(self.electric, dtype=float)
        lorentz+=np.cross(particle.charge*momentum/particle.mass, self.magnetic)
        return lorentz
    

    
def test(choice1):
    BField= EMField(ElectricField = np.array([0,0,0], dtype=float), MagneticField = np.array([0,0,-1E-5], dtype=float))
    time = 0  # initial time stamp
    deltaT =0.9E-6  # time steps of 1ms

    times = []
    X=[]
    Y=[]
    no_deltaT=0
    vmax=299792455
    # run simulation until time period has been achieved 

    if choice1==0:
        while time<=BField.TimePeriod():
            times.append(time)
            Force=BField.getForce(particle.momentum)
            # store the xy-position
            X.append(particle.position[0])
            Y.append(particle.position[1])
            # update the time
            time += deltaT
            no_deltaT += 1
            # update the positions and velocities
            particle.update(deltaT,3,particle.acceleration,Force)
    else:
        while time<=6.55E-3:
            times.append(time)

            # store the xy-position
            X.append(particle.position[0])
            Y.append(particle.position[1])

            # update the time
            time += deltaT
            no_deltaT += 1
            acceleration=BField.getAcceleration()
            # update the positions and velocities
            particle.update(deltaT,2,acceleration,0)

    fft=np.fft.fft2((X,Y))

    print(max(abs(fft)))
    plt.plot(X,Y, 'r-', label='trajectory')
    plt.xlabel('time (s)')
    plt.ylabel('y-position (m)')
    plt.title('Proton of non-zero inital velocity in a constand B-Field')
    plt.legend()

    plt.show()
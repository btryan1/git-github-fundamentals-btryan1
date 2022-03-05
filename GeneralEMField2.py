from abc import ABC, abstractmethod
from cmath import pi
import numpy as np
import math
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
    deltat =0.001E-5  # time steps of 1ms
    deltat_2=0.0002E-5

    times = []
    X=[]
    Y=[]
    T=[]
    T_2=[]
    deltaT=[]
    deltaT_2=[]
    no_deltaT=0
    vmax=299792455
    # run simulation until time period has been achieved 
    T.append(particle.kineticEnergy())  
    T_2.append(particle.kineticEnergy()) 
    if choice1==0:
        while time<=BField.TimePeriod():
            times.append(time)
            Force=BField.getForce(particle.momentum)
            # store the xy-position
            X.append(particle.position[0])
            Y.append(particle.position[1])
            # update the time
            time += deltat
            no_deltaT += 1
            # update the positions and velocities
            particle.update(deltat,3,particle.acceleration,Force)
            T.append(particle.kineticEnergy())
            deltaT.append(T[-1]-T[-2])
        return X,Y,times,T,deltaT
    
    else:
        while time<=BField.TimePeriod():
            times.append(time)

            # store the xy-position
            X.append(particle.position[0])
            Y.append(particle.position[1])

            # update the time
            time += deltat_2
            no_deltaT += 1
            acceleration=BField.getAcceleration()
            # update the positions and velocities
            particle.update(deltat_2,2,acceleration,0)
            T_2.append(particle.kineticEnergy())
            deltaT_2.append(T_2[-1]-T_2[-2])
        return X,Y,times,T_2,deltaT_2
def plot1():

    X,Y,times,T,deltaT=test(0)
    X,Y,times_2,T_2,deltaT_2=test(1)

    fft=np.fft.fft(Y)
    plt.plot(times,deltaT, 'r-', label='DeltaT choice 1')
    plt.plot(times_2,deltaT_2, 'g', label='DeltaT choice 2')
    plt.xlabel('time (s)')
    plt.ylabel('Delta T(j)')
    plt.title('Proton of non-zero inital velocity in a constand B-Field')
    plt.legend()

    plt.show()      

def plot2():
    X,Y,times_2,T_2,deltaT_2=test(1)
    plt.plot(X,Y, 'g', label='DeltaT choice 2')
    plt.xlabel('X(m)')
    plt.ylabel('Y(m)')
    plt.title('Proton of non-zero inital velocity in a constand B-Field')
    plt.legend()

    plt.show()      

plot2()

from Particle import Proton,AntiProton,DeuteriumNucleus
from GeneralEMField2 import EMField
import numpy as np

ParticleType=Proton

class ChargedParticleBunch(EMField,ParticleType):
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


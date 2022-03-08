
from Particle import Proton,AntiProton,DeuteriumNucleus,AntiDeuteriumNucleus
from GeneralEMField2 import EMField
import numpy as np

ParticleType=Proton

class ChargedParticleBunch(EMField,ParticleType):
    def __init__(self,ElectricField , MagneticField):
        self.electric=ElectricField
        self.magnetic=MagneticField

    def Generate_Bunch(self,particle_num):
        Bunch=[]                      
        mean = [0, 0, 0]
        mean_2=[900,1100,0]
        position_matrix = [[0.01, 0, 0], [0, 0.01, 0], [0, 0, 0.01]]
        velocity_matrix=[[1000, 0, 0], [0, 1000, 0], [0, 0, 0]]
        # using np.multinomial() method
        particle_positions = np.random.multivariate_normal(mean, position_matrix, particle_num)
        particle_velocities=np.random.multivariate_normal(mean_2, velocity_matrix, particle_num)
        for i in range(particle_num):
            particle=ParticleType()
            particle.position=particle_positions[i]
            particle.velocity=particle_velocities[i]
            Bunch.append(particle)
        return Bunch
    
    def Bunch_Update(self,bunch,deltaT,method):
        BField= EMField(self.electric,self.magnetic)
        for i in range(len(bunch)):
            particle=bunch[i]
            acceleration=BField.getAcceleration(particle)
            particle.update(deltaT,method,acceleration)
            bunch[i]=particle
        return bunch
         
    def Orbit_Period(self,bunch):
        BField= EMField(self.electric,self.magnetic)
        Orbit_Period=[]
        for i in range(len(bunch)):
            Orbit_Period.append(BField.TimePeriod(bunch[i]))
        return (max(Orbit_Period))
        
    
    def Averages(self,bunch):
        Type=ParticleType()
        positions=[]
        velocities=[]
        for i in range(len(bunch)):
            Particle=bunch[i]
            positions.append(Particle.position)
            velocities.append(Particle.velocity)
        positions=np.vstack(positions)
        velocities=np.stack(velocities)
        average_position=np.array([np.mean(positions[:,0]),np.mean(positions[:,1]),np.mean(positions[:,2])],dtype=float)
        average_velocity=np.array([np.mean(velocities[:,0]),np.mean(velocities[:,1]),np.mean(velocities[:,2])],dtype=float)
        average_kinetic_energy=0.5*Type.mass*(np.linalg.norm(average_velocity))**2
        return average_position,average_velocity,average_kinetic_energy

    def EnergySpread(self,bunch):
        T=[]
        for i in range(len(bunch)):
            Particle=bunch[i]
            T.append(0.5*Particle.mass*(np.linalg.norm(Particle.velocity))**2)
        return T

    def Store_Positions(self,bunch):
        positions=[]
        for i in range(len(bunch)):
            particle=bunch[i]
            positions.append(particle.position)
        return (np.vstack(positions))



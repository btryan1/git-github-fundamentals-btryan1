from Particle import Proton
from GeneralEMField2 import EMField
import pandas as pd
from GenerateParticleBunch import ChargedParticleBunch
import numpy as np

time = 0  # initial time stamp
time2=0
deltat =2.5E-05  # time steps of 1ms
deltat_2=0.0002E-5
times = []
times_2=[]
Positions=[]
particle=Proton()
BField=EMField(electric = np.array([0,0,0], dtype=float), magnetic = np.array([0,0,-1E-5], dtype=float))
Cyclo_Frequency=BField.Cyclotron_Frequency(particle)
square_sig=BField.Square_Wave_Gen(Cyclo_Frequency)
PB=ChargedParticleBunch()
CM=ChargedParticleBunch(electric = np.array([0,0,0], dtype=float), magnetic = np.array([0,0,-1E-5], dtype=float))
radius_of_orbit=2.9868732070658437
L=0.1493436603532922
Bunch=PB.Generate_Bunch(100)
Time_period=CM.Orbit_Period(Bunch)
Average_Positons=[]
Average_Velocities=[]
Average_Kinetic_Energies=[]
i=0
it=0
while time<=7*Time_period:
    if i==0:
        Averages=CM.Averages(Bunch)
        Average_Positons.append(Averages[0])
        Average_Velocities.append(Averages[1])
        Average_Kinetic_Energies.append(Averages[2])
        Bunch=CM.Bunch_Update(Bunch,deltat,2)
        time += deltat
        i+=1
    else:
        Y_avg=Average_Positons[-1]
        y=np.abs(Y_avg[1])
        print(y)
        if y<=L:
            SQ_Val=square_sig[it]
            print(time-time2,SQ_Val)
            EMC=ChargedParticleBunch(electric = np.array([0,SQ_Val*-5E-4,0], dtype=float), magnetic = np.array([0,0,-1E-5], dtype=float))
            Averages=EMC.Averages(Bunch)
            Average_Positons.append(Averages[0])
            Average_Velocities.append(Averages[1])
            Average_Kinetic_Energies.append(Averages[2])
            Bunch=EMC.Bunch_Update(Bunch,deltat,2)
            time += deltat
        else:
            Averages=CM.Averages(Bunch)
            Average_Positons.append(Averages[0])
            Average_Velocities.append(Averages[1])
            Average_Kinetic_Energies.append(Averages[2])
            Bunch=CM.Bunch_Update(Bunch,deltat,2)
            time+=deltat
            it+=1
            time2+=deltat




pd.DataFrame(Average_Positons).to_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonPositions.csv')
print('100ProtonPositions.csv has been saved')

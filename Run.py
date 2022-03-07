import pandas as pd
from GenerateParticleBunch import ChargedParticleBunch
import numpy as np


time = 0  # initial time stamp
deltat =0.01E-5  # time steps of 1ms
deltat_2=0.0002E-5
times = []
Positions=[]
PB=ChargedParticleBunch(ElectricField = np.array([0,0,0], dtype=float), MagneticField = np.array([0,0,-1E-5], dtype=float))
Bunch=PB.Generate_Bunch(1)
Time_period=PB.Orbit_Period(Bunch)
Positions.append(PB.Store_Positions(Bunch))
while time<=Time_period:
    Bunch=PB.Bunch_Update(Bunch,deltat,2)
    Positions.append(PB.Store_Positions(Bunch))
    time += deltat
Positions=np.squeeze(Positions)
pd.DataFrame(Positions).to_csv(r'C:\Users\benti\Documents\PHYS 389\1ProtonPositions.csv')
print('1ProtonPositions.csv has been saved')

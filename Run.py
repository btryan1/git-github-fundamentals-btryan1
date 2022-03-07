from matplotlib.animation import FuncAnimation
import pandas as pd
from Particle import ChargedParticle
from Particle import ProtonBunch
import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.pyplot as plt
from GeneralEMField2 import EMField
BField= EMField(ElectricField = np.array([0,0,0], dtype=float), MagneticField = np.array([0,0,-1E-5], dtype=float))
PB=ProtonBunch()

def test(proton_num,proton_choice):
    time = 0  # initial time stamp
    deltat =0.01E-5  # time steps of 1ms
    deltat_2=0.0002E-5
    times = []
    X=[]
    Y=[]
    Z=[]
    position_history=[]
    Proton_Bunch=PB.Generate_Bunch(proton_num)
    Proton_Bunch_Positions=Proton_Bunch[0]

    Proton_Bunch_Velocites=Proton_Bunch[1]

    Proton_Bunch_Accelerations=np.zeros((proton_num,3))
   
    while time<=BField.TimePeriod():
        if proton_choice==1:
            for i in range(proton_num):
                    proton = ChargedParticle(
                        position=Proton_Bunch_Positions[i],
                        velocity=Proton_Bunch_Velocites[i],
                        acceleration=Proton_Bunch_Accelerations[i],
                        name="Proton",
                        mass=1.6726219E-27,
                        charge=1.602176634E-19)
                    X.append(proton.position[0])
                    Y.append(proton.position[1])
                    Z.append(proton.position[2])
                    acceleration=BField.getAcceleration(proton)
                    proton.update(deltat,2,acceleration,0)
                    Proton_Bunch_Positions[i]=proton.position
                    Proton_Bunch_Velocites[i]=proton.velocity
            time += deltat
        elif proton_choice==2:
                for i in range(proton_num):
                    antiproton = ChargedParticle(
                        position=Proton_Bunch_Positions[i],
                        velocity=Proton_Bunch_Velocites[i],
                        acceleration=Proton_Bunch_Accelerations[i],
                        name="Proton",
                        mass=1.6726219E-27,
                        charge=-1.602176634E-19)
                    X.append(antiproton.position[0])
                    Y.append(antiproton.position[1])
                    Z.append(antiproton.position[2])
                    acceleration=BField.getAcceleration(antiproton)
                    antiproton.update(deltat,2,acceleration,0)
                    Proton_Bunch_Positions[i]=antiproton.position
                    Proton_Bunch_Velocites[i]=antiproton.velocity
                time += deltat
        else:
            print('Incorrect proton type')
            break
    return X,Y,Z
choice=2
X,Y,Z=test(2,choice)

df=np.vstack((X,Y,Z))
print(np.shape(df))
if choice==1 :    
    pd.DataFrame(df).to_csv(r'C:\Users\benti\Documents\PHYS 389\2Proton.csv')
    print('2Proton.csv has been saved')
elif choice==2:
    pd.DataFrame(df).to_csv(r'C:\Users\benti\Documents\PHYS 389\2AntiProton.csv')
    print('2AntiProton.csv has been saved')

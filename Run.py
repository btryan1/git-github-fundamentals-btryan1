from matplotlib.animation import FuncAnimation
from Particle import ChargedParticle
from Particle import ProtonBunch
import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.pyplot as plt
from GeneralEMField2 import EMField
BField= EMField(ElectricField = np.array([0,0,0], dtype=float), MagneticField = np.array([0,0,-1E-5], dtype=float))
PB=ProtonBunch()

def test(proton_num):
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
            for i in range(proton_num):
                if i ==0:
                    proton = ChargedParticle(
                        position=Proton_Bunch_Positions[i],
                        velocity=Proton_Bunch_Velocites[i],
                        acceleration=Proton_Bunch_Accelerations[i],
                        charge=-1)
                    X.append(proton.position[0])
                    Y.append(proton.position[1])
                    Z.append(proton.position[2])
                    acceleration=BField.getAcceleration(proton.velocity)
                    proton.update(deltat,2,acceleration,0)
                    Proton_Bunch_Positions[i]=proton.position
                    Proton_Bunch_Velocites[i]=proton.velocity
                else:
                    proton = ChargedParticle(
                        position=Proton_Bunch_Positions[i],
                        velocity=Proton_Bunch_Velocites[i],
                        acceleration=Proton_Bunch_Accelerations[i])
                    X.append(proton.position[0])
                    Y.append(proton.position[1])
                    Z.append(proton.position[2])
                    acceleration=BField.getAcceleration(proton.velocity)
                    proton.update(deltat,2,acceleration,0)
                    Proton_Bunch_Positions[i]=proton.position
                    Proton_Bunch_Velocites[i]=proton.velocity
            time += deltat
    return X,Y,Z
def Extract(X,Y,Z):
    X_0=[]
    X_1=[]
    Y_0=[]
    Y_1=[]
    Z_0=[]
    Z_1=[]
    for i in range(0,len(X)-1,4*160):
        X_0.append(X[i])
        X_1.append(X[i+1])
        Y_0.append(Y[i])   
        Y_1.append(Y[i+1])      
        Z_0.append(Z[i])
        Z_1.append(Z[i+1]) 
    return (X_0,X_1,Y_0,Y_1,Z_0,Z_1)

time_percent=3.049968E-4    
X,Y,Z=test(2)

X_0,X_1,Y_0,Y_1,Z_0,Z_1=Extract(X,Y,Z)
X_line=[]
Y_line=[]
Z_line=[]
X_1line=[]
Y_1line=[]
Z_1line=[]


def update(i):
    ax.cla()

    x = X_0[i]
    y = Y_0[i]
    z = 0
    X_line.append(x)
    Y_line.append(y)
    Z_line.append(z)
    x_1 = X_0[i]
    y_1 = Y_0[i]
    z_1 = 0
    X_1line.append(x_1)
    Y_1line.append(y_1)
    Z_1line.append(z_1)

    ax.scatter(x, y, z, s = 15, marker = 'o')
    ax.scatter(x_1, y_1, z_1, s = 10, marker = 'o')
    ax.plot(X_line, Y_line, Z_line)
    ax.plot(X_1line, Y_1line, Z_1line)



    ax.set_xlim(-0.02, 0.02)
    ax.set_ylim(-0.02, 0.02)
    ax.set_zlim(-0, 0.)

fig = plt.figure(dpi=200)
ax = fig.add_subplot(projection='3d')

ani = FuncAnimation(fig = fig, func = update, frames = 600, interval = 1, repeat = False)
plt.show()

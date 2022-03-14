import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
from matplotlib.animation import FuncAnimation, PillowWriter

df = pd.read_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonPositions.csv')
n = 1000
number_of_frames = 1000
data = pd.DataFrame(df).to_numpy()
Positions=data[:,1:]
X_1=Positions[:,0]
Y_1=Positions[:,1]
Z_1=Positions[:,2]


def update_hist(num, data):
    print(num)
    plt.cla()
    plt.hist(data[num])

    fig = plt.figure()
    hist = plt.hist(data[7])

    animation = animation.FuncAnimation(fig, update_hist, number_of_frames, fargs=(data, ) )
        
def Extract(X_1,Y_1,Z_1):
    X=[]
    Y=[]
    Z=[]
    for i in range(0,1826,2):
        X.append(X_1[i])
        Y.append(Y_1[i])
        Z.append(Z_1[i])
    return X,Y,Z


time_percent=3.049968E-4    
X,Y,Z=Extract(X_1,Y_1,Z_1)
X_line=[]
Y_line=[]
Z_line=[]


frames=len(X)
def update(i):
    ax.cla()

    x = X[i]
    y = Y[i]
    z = Z[i]
    X_line.append(x)
    Y_line.append(y)
    Z_line.append(z)


    ax.scatter(x, y, z, s = 10, marker = 'o')
    ax.plot(X_line, Y_line, Z_line)



    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_zlim(-0.1, 0.1)

fig = plt.figure(dpi=150)
ax = fig.add_subplot(projection='3d')

anim = FuncAnimation(fig = fig, func = update, frames = frames, interval = 1, repeat = False)
f = r'C:\Users\benti\Documents\PHYS 389\100Proton.gif'
writergif = animation.PillowWriter(fps=30) 
anim.save(f, writer=writergif)
plt.show()



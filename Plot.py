import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
from matplotlib.animation import FuncAnimation, PillowWriter

df = pd.read_csv(r'C:\Users\benti\Documents\PHYS 389\2AntiProton.csv')
n = 1000
number_of_frames = 1000
data = pd.DataFrame(df).to_numpy()
data=data[:,1:]


def update_hist(num, data):
    print(num)
    plt.cla()
    plt.hist(data[num])

    fig = plt.figure()
    hist = plt.hist(data[7])

    animation = animation.FuncAnimation(fig, update_hist, number_of_frames, fargs=(data, ) )
        
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

X_0,X_1,Y_0,Y_1,Z_0,Z_1=Extract(data[0],data[1],data[2])
print(len(X_0))
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

    ax.scatter(x, y, z, s = 10, marker = '<')
    ax.scatter(x_1, y_1, z_1, s = 10, marker = '>')
    ax.plot(X_line, Y_line, Z_line)
    ax.plot(X_1line, Y_1line, Z_1line)



    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_zlim(-0.1, 0.1)

fig = plt.figure(dpi=150)
ax = fig.add_subplot(projection='3d')

anim = FuncAnimation(fig = fig, func = update, frames = 205, interval = 1, repeat = False)
f = r'C:\Users\benti\Documents\PHYS 389\2AntiProton.gif'
writergif = animation.PillowWriter(fps=30) 
anim.save(f, writer=writergif)
plt.show()

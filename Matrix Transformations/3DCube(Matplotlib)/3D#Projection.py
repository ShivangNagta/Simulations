import numpy as np
from matplotlib import pyplot as plt
import math
import random


plt.rcParams['figure.figsize'] = [6, 6]
plt.rcParams['font.size'] = 20


points = []
angle = 0
for k in range(5):
    for i in range(5):
        if i == 0 or i == 4:
            for j in range(5):
                if j == 0 or j == 4: 
                    points.append([4*k-8,4*i-8,4*j-8])
                    
        

pointsarray = np.array(points)
pointsarray = pointsarray.reshape((5,2,2,3))



while True:
    plt.clf()
    
    rotation_z = np.matrix([[math.cos(angle),-math.sin(angle),0],
                            [math.sin(angle), math.cos(angle),0],
                            [0,0,1]])
    rotation_x = 2*np.matrix([[1,0,0],
                            [0,math.cos(angle),-math.sin(angle)],
                            [0,math.sin(angle),math.cos(angle)]])
    rotation_y = np.matrix([
        [math.cos(angle), 0, math.sin(angle)],
        [0, 1, 0],
        [-math.sin(angle), 0, math.cos(angle)]
    ])
    
    
    projection = np.matrix([[1,0,0],
                            [0,1,0]])
    for k in range(5):
        for i in range(2):
            for j in range(2):
                pointvector = np.matrix([pointsarray[k][i][j][0],pointsarray[k][i][j][1],pointsarray[k][i][j][2]])
                rotatedy = np.dot(rotation_y, pointvector.reshape((3,1)))
                rotatedx = np.dot(rotation_x, rotatedy)
                #rotatedz = np.dot(rotation_z, rotatedx)
                projected = np.dot(projection, rotatedx)
                # pointsarray[i][j][0] = rotated[0][0] 
                # pointsarray[i][j][1] = rotated[1][0]
                
                x = projected[0][0] + 20
                y = projected[1][0] + 20
                
                glitch = "#*"
                t=random.randint(0,1)
                plt.text(x,y, glitch[t])
            

                  
    angle+=0.01
        
    
    
    plt.axis('off')
    plt.axis([0,40,0,40])
    plt.draw()
    plt.pause(0.01)
    
    


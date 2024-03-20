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
        for j in range(5):
                 points.append([4*k-8,4*i-8,4*j-8])
        

pointsarray = np.array(points)
pointsarray = pointsarray.reshape((5,5,5,3))
 


while True:
    plt.clf()
    
    rotation_z = np.matrix([[math.cos(angle),-math.sin(angle),0],
                            [math.sin(angle), math.cos(angle),0],
                            [0,0,1]])
    rotation_x = np.matrix([[1,0,0],
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
        for i in range(5):
            for j in range(5):
                pointvector = np.matrix([pointsarray[k][i][j][0],pointsarray[k][i][j][1],pointsarray[k][i][j][2]])
                rotatedx = np.dot(rotation_z, pointvector.reshape((3,1)))
                rotatedy = np.dot(rotation_y, rotatedx)
                projected = np.dot(projection, rotatedy)
                # pointsarray[i][j][0] = rotated[0][0] 
                # pointsarray[i][j][1] = rotated[1][0]
                
                x = projected[0][0] + 20
                y = projected[1][0] + 20
                
                # plt.plot(x,y,'bo',linestyle="--", linewidth=8, markersize=15, color='black')   
                glitch = "@#$%*"
                #t=random.randint(0,4)
                plt.text(x,y, "$") 
                    

                  
    angle+=0.05
        
    
    
    plt.axis('off')
    plt.axis([0,40,0,40])
    plt.draw()
    plt.pause(0.01)
    
    

plt.show()
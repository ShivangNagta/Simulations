import numpy as np
from matplotlib import pyplot as plt
from math import *


plt.rcParams['figure.figsize'] = [6, 6]
plt.rcParams['font.size'] = 20


points = [[1,1,1],[1,1,-1],[1,-1,1],[1,-1,-1],[-1,1,1],[-1,1,-1],[-1,-1,1],[-1,-1,-1]]
angle = 0
        

pointsarray = np.array(points)
 


while True:
    plt.clf()
    
    rotation_z = np.matrix([[cos(angle),-sin(angle),0],
                            [sin(angle), cos(angle),0],
                            [0         ,0          ,1]])
    
    rotation_x = np.matrix([[1           ,0        ,0],
                            [0,cos(angle),-sin(angle)],
                            [0,sin(angle), cos(angle)]])
    
    rotation_y = np.matrix([[cos(angle) , 0, sin(angle)],
                            [0          , 1          ,0],
                            [-sin(angle), 0, cos(angle)]])

    projectionMatrix = np.matrix([[1,0,0],              
                                  [0,1,0]])
    
    
    for i in range(8):
                pointvector = np.matrix([pointsarray[i][0],pointsarray[i][1],pointsarray[i][2]])
                rotatedy = np.dot(rotation_y, pointvector.reshape((3,1)))
                # rotatedz = np.dot(rotation_z, rotatedy)
                projected = np.dot(projectionMatrix, rotatedy)
                # pointsarray[i][j][0] = rotated[0][0] 
                # pointsarray[i][j][1] = rotated[1][0]
                
                x = 8*projected[0][0] + 20
                y = 8*projected[1][0] + 20
                
                plt.text(x,y, '#')              
    
                  
    angle+=0.01
        
    
    
    plt.axis('off')
    plt.axis([0,40,0,40])
    plt.draw()
    plt.pause(0.01)
    
    


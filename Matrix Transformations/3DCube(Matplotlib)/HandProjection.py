import numpy as np
from matplotlib import pyplot as plt
import math
import random

def SkullVertex(filename):
    vertex= []
    with open(filename) as f:
        for line in f:
            if line.startswith('v '):
                vertex.append([float(i) for i in line.split()[1:]])
    return vertex


plt.rcParams['figure.figsize'] = [6, 6]
plt.rcParams['font.size'] = 12

points = SkullVertex("hand.obj")


angle = 0

# points = points[:1000]
newpoints = []

for i in range(int(len(points)/70)-3):
    newpoints.append(points[70*i])

# pointsarray = np.array(newpoints)
# pointsarray = pointsarray.reshape((5,5,5,3))
print(np.shape(newpoints))

 

rot = np.matrix([[1,0,0],
                            [0,0,1],
                            [0,-1,0]])

newpt = []

for k in newpoints:
                pointvector = np.matrix([k[0],k[1],k[2]])
                rotmat = np.dot(rot, pointvector.reshape((3,1)))
                newpt.append([rotmat[0][0],rotmat[1][0],rotmat[2][0]])
    
     
newpt = np.array(newpt)




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
    for k in newpt:
                newptt = np.matrix([k[0][0],k[1][0],k[2][0]])
                rotatedy = np.dot(rotation_y, newptt.reshape((3,1)))
                # rotatedy = np.dot(rotation_y, rotatedx)
                #rotatedz = np.dot(rotation_z, rotatedy)
                # projected = np.dot(projection, pointvector.reshape((3,1)))
                projected = np.dot(projection, rotatedy)
                # pointsarray[i][j][0] = rotated[0][0] 
                # pointsarray[i][j][1] = rotated[1][0]
                
                x = projected[0][0] + 8
                y = projected[1][0] + 1
                
                # plt.plot(x,y,'bo',linestyle="--", linewidth=8, markersize=15, color='black')   
                glitch = "@#$%*"
                #t=random.randint(0,4)
                plt.text(x,y, "#") 
                    

                  
    angle+=0.2
        
    
    
    plt.axis('off')
    plt.tight_layout()
    plt.axis([0,20,0,20])
    plt.draw()
    plt.pause(0.01)
    
    

plt.show()
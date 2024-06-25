import numpy as np
import keyboard
from matplotlib import pyplot as plt
from matplotlib import colors
#from matplotlib import pylab




plt.rcParams['figure.figsize'] = [8, 5]
renderMap = [[1,1,1,1,1,1,1],
             [1,0,0,1,0,0,1],
             [1,0,0,0,0,0,1],
             [1,1,0,1,0,0,1],
             [1,0,0,1,0,0,1],
             [1,1,1,1,1,1,1]]

#renderMapTr = np.transpose(renderMap)


posx , posy = 1,1
rot = np.pi/4

while True:
    
    plt.text(30,30, '#', horizontalalignment='center', verticalalignment='center') 
    plt.text(35,35, '#', horizontalalignment='center', verticalalignment='center') 
    
    plt.axis('off')
    plt.tight_layout()
    plt.axis([0,60,0,60])

    plt.draw()
    plt.pause(0.01)
    plt.clf()
    

    

plt.close()
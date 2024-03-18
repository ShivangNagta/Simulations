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
    colormap = colors.ListedColormap(["white","green"])
    plot1 = plt.subplot2grid((1, 2), (0, 0)) 
    plot2 = plt.subplot2grid((1, 2), (0, 1))
    plot2.imshow(renderMap, cmap=colormap, origin='upper')
    plot1.hlines(-0.6,0,60, colors= 'gray', lw=185, alpha=0.7)
    plot1.hlines(0.6,0,60, colors= 'lightblue', lw=185, alpha=0.7)
    
    for i in range(60):
        rot_i = rot + np.deg2rad(i-30)
        x,y = posx, posy
        cos = 0.01*np.cos(rot_i)
        sin = 0.01*np.sin(rot_i)
        n = 0
        while True:
            # current_pos = (x,y)
            x,y = x+cos, y+sin
            n += 1
            if renderMap[int(x)][int(y)] == 1:
                # final_pos = (x,y)
                # fishEye = math.dist(list(final_pos),list(current_pos))*abs(np.cos(rot_i))
                # print(fishEye,np.cos(abs(rot_i)))
                # print(".........................")
                # print(np.clip((1/(n*0.02)),0,1))
                h = np.clip((1/(n*0.01)),0,1)
                break
        plot1.vlines(i,-h,h, linewidth=8, colors=np.asarray([0,1,0])*(0.4+0.6*h**2))
    

    
    
    
    
    x, y = (posx, posy)
    plot2.arrow(y-0.5,x-0.5, 0.3*np.sin(rot), 0.3*np.cos(rot),
        width = 0.03,
        ec ='blue')
    plot1.axis('off')
    plt.tight_layout()
    plot1.axis([0,60,-1,1])
    plot2.axis([-0.5,6.5,-0.5,5.5])
    plot2.plot(np.array([y])-0.5,np.array([x])-0.5,'o')
    plt.draw()
    plt.pause(0.01)
    plt.clf()
    
    
    
    key = keyboard.read_key()
    if key == 'up':
        x, y = (x + 0.3*np.cos(rot), y + 0.3*np.sin(rot))
    elif key == 'down':
        x, y = (x - 0.3*np.cos(rot), y - 0.3*np.sin(rot))
    elif key == 'left':
        rot = rot - np.pi/8
    elif key == 'right':
        rot = rot + np.pi/8
    elif key == 'esc':
        break
    
    
    #plot2.plot(np.array([x]),np.array([y]),'o')
    if renderMap[int(x)][int(y)] == 0:
        posx, posy = (x, y)
        #print(posx,posy)
        # plot2.plot(np.array([posy]),np.array([posx]),'o')

plt.close()
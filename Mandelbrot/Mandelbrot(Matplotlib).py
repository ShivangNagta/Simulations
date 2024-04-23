import matplotlib.pyplot as plt
import numpy as np

def Mandelbrot(complexNum, maxIterations):
    z=0
    for i in range(maxIterations):
        if abs(z) > 2:
            return i
        z = z*z + complexNum     
    return maxIterations

def MandelbrotSet(xMin, xMax, yMin, yMax, width, height, maxIterations):
    x =  np.linspace(xMin, xMax, width)
    y =  np.linspace(yMin, yMax, height)
    
    mSet = np.zeros((width, height))
    for i in range(height):
        for j in range(width):
            complexNum = complex(x[i], y[j])
            mSet[j,i] = Mandelbrot(complexNum, maxIterations)
    return mSet

xMin, xMax, yMin, yMax = -0.76, -0.6, 0.4, 0.45
height, width = 1000, 1000
maxIterations = 100

plt.imshow(MandelbrotSet(xMin, xMax, yMin, yMax, width, height, maxIterations), extent= [xMin,xMax, yMin,yMax], cmap ="hot")

plt.show()

    
import numpy as np
import pygame
from math import *

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)


WIDTH, HEIGHT = 800, 600
pygame.display.set_caption("3D Cube projection")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

scale = 100
circle_pos =[WIDTH/2,HEIGHT/2]
angle = 0


points = []
points.append(np.matrix([-1, -1, 1]))
points.append(np.matrix([1, -1, 1]))
points.append(np.matrix([1, 1, 1]))
points.append(np.matrix([-1, 1, 1]))
points.append(np.matrix([-1, -1, -1]))
points.append(np.matrix([1, -1, -1]))
points.append(np.matrix([1, 1, -1]))
points.append(np.matrix([-1, 1, -1]))
points.append(np.matrix([-0, 2 ,0]))


projection_matrix = np.matrix([
    [1, 0, 0],
    [0, 1, 0]
])
projected_points = [
    [n,n] for n in range(len(points))
]

def connect_points(i,j,points):
    pygame.draw.line(screen, RED, (points[i][0], points[i][1]), (points[j][0], points[j][1]))


clock = pygame.time.Clock()

while True:
    
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
    
    rotation_z = np.matrix([
        [cos(angle), -sin(angle), 0],
        [sin(angle), cos(angle), 0],
        [0, 0, 1]
    ])
    
    rotation_y = np.matrix([
        [cos(angle), 0, sin(angle)],
        [0, 1, 0],
        [-sin(angle), 0, cos(angle)]
    ])
    
    rotation_x = np.matrix([
        [1, 0, 0],
        [0, cos(angle), -sin(angle)],
        [0, sin(angle), cos(angle)]
    
    ])
    
    angle+=0.01 
    
    screen.fill(WHITE)
    
    i=0
    for point in points:
        rotated_2d = np.dot(rotation_y, point.reshape((3,1)))
        # rotated_2d = np.dot(rotation_x, rotated_2d)
        projected2d = np.dot(projection_matrix, rotated_2d)
        x = int(projected2d[0][0]* scale)+circle_pos[0]
        y = int(projected2d[1][0]* scale)+circle_pos[1] 
        
        projected_points[i] = [x,y]
        pygame.draw.circle(screen, BLACK, (x,y), 5)
        i+=1
        
    # connect_points(0,1,projected_points)
    # connect_points(1,2,projected_points)
    # connect_points(2,3,projected_points)
    # connect_points(3,0,projected_points)
    
    # connect_points(4,5,projected_points)
    # connect_points(5,6,projected_points)
    # connect_points(6,7,projected_points)
    # connect_points(7,4,projected_points)
    
    # connect_points(0,4,projected_points)
    # connect_points(1,5,projected_points)
    # connect_points(2,6,projected_points)
    # connect_points(3,7,projected_points)
    
    for p in range(4):
        connect_points(p, (p+1)%4, projected_points)
        connect_points(p+4, (p+1)%4+4, projected_points)
        connect_points(p, p+4, projected_points)
    connect_points(8, 2, projected_points)
    connect_points(8, 3, projected_points)
    connect_points(8, 6, projected_points)
    connect_points(8, 7, projected_points)
    # connect_points(0, 6, projected_points)
    # connect_points(1, 7, projected_points)
    # connect_points(2, 4, projected_points)
    # connect_points(3, 5, projected_points)
    
    pygame.display.update()
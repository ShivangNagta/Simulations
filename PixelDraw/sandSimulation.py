
import pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

dt = 0
def drawGrid():
    blockSize = 20 
    for x in range(0, screen.get_width(), blockSize):
        for y in range(0, screen.get_height(), blockSize):
            pygame.draw.rect(screen, (255,255,255), (x,y,20,20), 1)
            
renderSet=[]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    drawGrid()
    
    
    
    if pygame.mouse.get_pressed()[0]:
        x,y = pygame.mouse.get_pos()
        renderPositionX= (x//20)*20
        renderPositionY= (y//20)*20
        renderSet.append([renderPositionX,renderPositionY])
    
    for i in range(len(renderSet)):
        pygame.draw.rect(screen, (255,255,255), (renderSet[i][0],renderSet[i][1],20,20),0)
        
    
    
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
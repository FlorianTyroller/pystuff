import os
import pygame
import time
import math
import numpy as np

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_PLUS,
    K_MINUS,
    K_ESCAPE,
    K_SPACE,
    KEYDOWN,
    QUIT,
)

pygame.font.init() 
myfont = pygame.font.SysFont("Times New Roman",20)

# Initialize pygame
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800,800

CENTER = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



size = 5
l = 2*size + 1
#sphere
#grid =[[[1 if math.sqrt((i-size)**2+(j-size)**2+(k-size)**2)<=size*0.9 else 0 for i in range(l)] for j in range(l)] for k in range(l)]

#plane
grid =[[[1 if k == size and j == size else 0 for i in range(l)] for j in range(l)] for k in range(l)]


def printS(s):
    for i in range(l):
        print(*grid[i][s])

    print()

def rotateMatrix(a, v):
    x,y,z = v
    sc =[] 
    for ar in a:
        l = ar * math.pi / 180
        sc.append((math.sin(l),math.cos(l)))
    

    sina = sc[0][0]
    cosa = sc[0][1]
    #xrot
    x = x 
    y = y * cosa - z * sina
    z = y * sina + z * cosa

    sina = sc[1][0]
    cosa = sc[1][1]
    #yrot
    x = x * cosa + z * sina
    y = y 
    z = (-x) * sina + z * cosa

    sina = sc[2][0]
    cosa = sc[2][1]
    #zrot
    x = x * cosa - y * sina
    y = x * sina + y * cosa
    z = z 

    return (x,y,z)



def main():
    clicked = False
    origin = [0,0]
    off = 100
    scale = 300
    run = True
    xRot = 0
    yRot = 0
    zRot = 0

    
    
    rotate = False

    while run:
        for event in pygame.event.get():

            if event.type == KEYDOWN:
                e = event.key 
                if e == K_ESCAPE:
                    run = False
                if e == K_LEFT:
                    xRot-=5 
                if e == K_RIGHT:
                    xRot+=5
                if e == K_DOWN:
                    yRot-=5 
                if e == K_UP:
                    yRot+=5
                if e == K_SPACE:
                    rotate = True
                xRot %= 360
                yRot %= 360
            elif event.type == pygame.KEYUP:
                rotate = False
            elif event.type == pygame.QUIT:
                run = False
            '''
            elif event.type == pygame.MOUSEBUTTONUP:
                pos =  pygame.mouse.get_pos()
                if clicked: 
                    balls.add(Ball((origin), [pos[0] - origin[0],pos[1] - origin[1]]))
                    clicked = False
                else:
                    origin = pos
                    clicked = True
            '''
            if rotate: xRot += 3

            screen.fill((255, 255, 255))
            t1 = myfont.render("xRot: " + str(xRot) , False, (0, 0, 0))
            t2 = myfont.render("yRot: " + str(yRot) , False, (0, 0, 0))
            t3 = myfont.render("zRot: " + str(zRot) , False, (0, 0, 0))
            t4 = myfont.render("+" , False, (0, 0, 0))
            screen.blit(t1,(0,0))
            screen.blit(t2,(0,20))
            screen.blit(t3,(0,40))
            screen.blit(t4,CENTER)
            for i in range(l):
                for j in range(l):
                    for k in range(l):
                        st = grid[i][j][k]
                        if st == 1:
                            x = (i-size)
                            y = (j-size)
                            z = (k-size)

                            x,y,z = rotateMatrix((xRot,yRot,zRot), (x,y,z))
                            
                            z = 15 - z
                            
                            x /= z
                            y /= z

                            #print(m,x,y,z)

                            x *= scale
                            y *= scale
                            
                            
                            x = int(CENTER[0]-x)
                            y = int(CENTER[1]-y)


                            
                            textsurface1 = myfont.render("o", False, (0, 0, 0))
                            screen.blit(textsurface1,(x,y))
                
        

 

        pygame.display.flip()

    pygame.quit()
        


if __name__ == '__main__':
    print("start rendering")
    main()
    print("complete")
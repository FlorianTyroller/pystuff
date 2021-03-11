import os
import pygame
import time
import math
import random

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_PLUS,
    K_MINUS,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.font.init() 


# Initialize pygame
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800,800
myfont = pygame.font.SysFont("Times New Roman",(SCREEN_WIDTH)//40)


xOff=SCREEN_WIDTH//2
yOff=SCREEN_HEIGHT//2

zoom = 0.01

CENTER = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#functions = [lambda a : math.sin(a),lambda a : math.cos(a),lambda a : math.tan(a)]

#functions = [lambda a : a,lambda a : 2*a,lambda a : 3*a]

#functions = [lambda a : 1/a,lambda a : a*a]

#functions = [lambda a :a*a,lambda a : a*a*a*a]

#functions = [lambda a : math.pow(a,a)]

#functions = [lambda a : math.sin(a),lambda a : math.cos(a),lambda a : math.tan(a)]

functions = [lambda a : math.sin(a),lambda a : math.sin(a*4)*2]

def f(x):
    #return math.sin(x)
    #return 
    try:
        z = random.choice(functions)
        y = z(x)
    except:
        y = 0
    return y
def update():
    screen.fill((255, 255, 255))
    textsurface1 = myfont.render("zoom: " + str(round(zoom,1)), False, (0, 0, 0))
    screen.blit(textsurface1,(0,0))
    points = []


    #draw axis
    pygame.draw.line(screen, (0,0,0), (0,yOff), (SCREEN_WIDTH,yOff), 1)
    pygame.draw.line(screen, (0,0,0), (xOff,SCREEN_HEIGHT), (xOff,0), 1)
    #draw numbers
    # x
    for i in range(11):
        x = int((1+i)/12 * SCREEN_WIDTH)
        y = yOff
        textsurface2 = myfont.render(str(round(((x-xOff)*zoom),1)), False, (0, 0, 0))
        pygame.draw.line(screen, (140,140,140), (x,0), (x,SCREEN_HEIGHT), 1)
        screen.blit(textsurface2,(x,y))
    # y
    for i in range(11):
        y = int((1+i)/12 * SCREEN_HEIGHT)
        x = xOff
        textsurface2 = myfont.render(str(round(((yOff-y)*zoom),1)), False, (0, 0, 0))
        pygame.draw.line(screen, (140,140,140), (0,y), (SCREEN_WIDTH,y), 1)
        screen.blit(textsurface2,(x,y))
    
    #calc points
    for i in range(SCREEN_WIDTH):
        points.append((i,f((i-xOff)*zoom)))

    #draw points
    for i in range(len(points)):
        if i < SCREEN_WIDTH-1:
            pOrigin = (points[i][0],yOff-points[i][1]*(1/zoom))
            pDestination = (points[i+1][0],yOff-points[i+1][1]*(1/zoom))
            pygame.draw.line(screen, (0,0,0), pOrigin, pDestination, 1)

    



    pygame.display.flip()

def main():
    
    global zoom
    global xOff
    global yOff
    run = True
    update()
    while run:
        for event in pygame.event.get():
            
            if event.type == KEYDOWN:

                e = event.key 
                if e == K_ESCAPE:
                    run = False
                elif e == K_RIGHT:
                    xOff+=zoom
                elif e == K_LEFT:
                    xOff-=zoom
                elif e == K_UP:
                    yOff+=zoom
                elif e == K_DOWN:
                    yOff-=zoom

            elif event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                xOff,yOff =  pygame.mouse.get_pos()

                
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 5:
               zoom *= 1.05

            elif event.type == pygame.MOUSEBUTTONUP and event.button == 4:
                zoom *= 0.95
        update()
                

        

    pygame.quit()


    # Fill the screen with white
        


if __name__ == '__main__':
    print("start rendering")
    main()
    print("complete")
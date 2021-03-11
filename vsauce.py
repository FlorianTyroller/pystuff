import os
import pygame
import time
import math

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
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
myfont = pygame.font.SysFont("Times New Roman",20)

# Initialize pygame
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 400,1000

CENTER = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)

radius = int((min(SCREEN_WIDTH, SCREEN_HEIGHT) // 2) * 0.9)
nodes = 40
iterations = 2
multi = 4

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    global nodes
    global iterations
    global multi
    update()

    run = True

    while run:
        for event in pygame.event.get():

            if event.type == KEYDOWN:
                e = event.key 
                if e == K_ESCAPE:
                    run = False
                elif e == K_UP:
                    nodes += 10
                elif e == K_DOWN:
                    nodes -= 10
                elif e == K_LEFT:
                    iterations -= 1 
                elif e == K_RIGHT:
                    iterations += 1
                elif e == 47:
                    multi -= 1 
                elif e == 93:
                    multi += 1

                update()
            elif event.type == pygame.QUIT:

                run = False
    pygame.quit()

def update():
    # Fill the screen with white
        screen.fill((255, 255, 255))
        textsurface1 = myfont.render("nodes: " + str(nodes), False, (0, 0, 0))
        textsurface2 = myfont.render("iter.: " + str(iterations), False, (0, 0, 0))
        textsurface3 = myfont.render("multi: " + str(multi), False, (0, 0, 0))
        screen.blit(textsurface1,(0,0))
        screen.blit(textsurface2,(0,15))
        screen.blit(textsurface3,(0,30))
        #draw
        for z in range(nodes):
            i = z+1
            coords = get_coordinate(i)
            textsurface = myfont.render(str(i), False, (0, 0, 0))
            screen.blit(textsurface,coords)
            linecolor = (0,0,0)
            for k in range(iterations):
                if (i + (k * nodes)) * multi < nodes * iterations:
                    pygame.draw.line(screen, linecolor, coords, get_coordinate((i + (k * nodes)) * multi), 1)

        pygame.display.flip()

def get_coordinate(n):

    i = n % nodes
    a = (i/nodes * 360 - 90) * (math.pi/180)
    x = math.cos(a) * radius + CENTER[0]
    y = math.sin(a) * radius + CENTER[1]  

    return (x,y)

if __name__ == '__main__':
    print("start rendering")
    main()
    print("complete")
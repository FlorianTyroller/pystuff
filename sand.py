import os
import pygame
import time
import math

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

SCREEN_WIDTH, SCREEN_HEIGHT = 400,400



xOff=10
yOff=10

zoom = 5

CENTER = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)

screen = pygame.display.set_mode((800, 800))
blocks = pygame.sprite.Group()

class Block(pygame.sprite.Sprite):
    def __init__(self,coords,type):
        super(Block, self).__init__()
        self.x,self.y = coords
        self.type = type
        self.surf = pygame.Surface((zoom, zoom))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect(center=(self.x, self.y))

    def update(self):
        self.surf = pygame.Surface((zoom, zoom))
        self.rect = self.surf.get_rect(center=(self.x, self.y))
        None

        
def posToIds(coords):
    return (coords[0]//zoom,coords[1]//zoom)

def update():
    screen.fill((255, 255, 255))
    textsurface1 = myfont.render("sand test", False, (0, 0, 0))
    screen.blit(textsurface1,(0,0))

    #draw grid
    '''
    for i in range(SCREEN_HEIGHT//zoom):
        pygame.draw.line(screen, (0,0,0), (0,i*zoom), (SCREEN_WIDTH,i*zoom), 1)
    
    for i in range(SCREEN_WIDTH//zoom):
        pygame.draw.line(screen, (0,0,0), (i*zoom,SCREEN_HEIGHT), (i*zoom,0), 1)
    '''
    #draw blocks
    blocks.update()
    for b in blocks:
        pygame.draw.rect(screen,(0,0,0),(b.x*zoom+xOff,b.y*zoom+yOff,zoom,zoom))
            

    #balls.draw()    
    # Check if any enemies have collided with the player
    



    pygame.display.flip()

def main():
    global blocks
    for i in range(SCREEN_HEIGHT):
        for j in range(SCREEN_WIDTH):
            if i == 0 or i == SCREEN_HEIGHT-1 or j == 0 or j == SCREEN_WIDTH-1:
                blocks.add(Block((j,i),1))
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
                pos =  pygame.mouse.get_pos()
                gx = (pos[0]-xOff)//zoom
                gy = (pos[1]-yOff)//zoom
                if gx in range(SCREEN_WIDTH) and gy in range(SCREEN_HEIGHT):
                    blocks.add(Block((gx,gy),1))
                

            elif event.type == pygame.MOUSEBUTTONUP and event.button == 4:
                zoom+=1

            elif event.type == pygame.MOUSEBUTTONUP and event.button == 5:
                if zoom > 1:
                    zoom -= 1 
        update()
                

        

    pygame.quit()


    # Fill the screen with white
        


if __name__ == '__main__':
    print("start rendering")
    main()
    print("complete")
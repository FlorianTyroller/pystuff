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

SCREEN_WIDTH, SCREEN_HEIGHT = 800,800

CENTER = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Ball(pygame.sprite.Sprite):
    def __init__(self,coords,vector):
        super(Ball, self).__init__()
        self.x,self.y = coords
        self.dir = vector
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect(center=(self.x, self.y))
        self.radius = 50

    def update(self):
        self.dir[1] *= 0.9999
        self.dir[1] += 0.01
        self.dir[0] *= 0.9999
        self.x += self.dir[0]/100
        self.y += self.dir[1]/100 
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

        # Keep Ball on the screen
        if self.rect.left < 0:
            self.rect.left = 0
            self.dir[0] = -self.dir[0]
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.dir[0] = -self.dir[0]
        if self.rect.top <= 0:
            self.rect.top = 0
            self.dir[1] = -self.dir[1]
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.dir[1] = -self.dir[1]

    
        




ball = Ball((0,0),(0,0))

def main():
    balls = pygame.sprite.Group()
    clicked = False
    origin = [0,0]

    run = True

    while run:
        for event in pygame.event.get():

            if event.type == KEYDOWN:
                e = event.key 
                if e == K_ESCAPE:
                    run = False
            elif event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONUP:
                pos =  pygame.mouse.get_pos()
                if clicked: 
                    balls.add(Ball((origin), [pos[0] - origin[0],pos[1] - origin[1]]))
                    clicked = False
                else:
                    origin = pos
                    clicked = True

        screen.fill((255, 255, 255))
        textsurface1 = myfont.render("physic test", False, (0, 0, 0))
        screen.blit(textsurface1,(0,0))
        collided = []
        for b in balls:
            screen.blit(b.surf, b.rect)
            
        #balls.draw()    
        balls.update()
        # Check if any enemies have collided with the player
        

 

        pygame.display.flip()

    pygame.quit()


    # Fill the screen with white
        


if __name__ == '__main__':
    print("start rendering")
    main()
    print("complete")
# breakout game

#import modules
import pygame
import random


width = 600
height = 600

# make aplatform object, a black rectangle
class Platform(pygame.sprite.Sprite):
    def __init__(self, coords):
        super(Platform, self).__init__()
        self.width = 50
        self.height = 10
        self.x, self.y = coords
        self.surf = pygame.Surface((self.width, self.height))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect(center=(self.x, self.y))
    
    def update(self):
        # check if self.x is within the screen
        if self.x < 0:
            self.x = 0
        if self.x > width - self.width:
            self.x = width - self.width
        self.rect.x = self.x
        self.rect.y = self.y

        # check for collisions with borders
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > height:
            self.rect.bottom = height

# red ball object  
class Ball(pygame.sprite.Sprite):
    def __init__(self, coords, vector):
        super(Ball, self).__init__()
        self.x, self.y = coords
        self.dir = vector
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=(self.x, self.y))
        self.radius = 50
    
    def update(self, platform):
        # move ball
        self.x += self.dir[0]
        self.y += self.dir[1]
        # bounce off borders
        if self.x < 0:
            self.x = 0
            self.dir[0] = -self.dir[0]
        if self.x > width - self.radius:
            self.x = width - self.radius
            self.dir[0] = -self.dir[0]
        if self.y < 0:
            self.y = 0
            self.dir[1] = -self.dir[1]
        if self.y > height - self.radius:
            self.y = height - self.radius
            self.dir[1] = -self.dir[1]
        # check for collisions with platform
        if self.rect.colliderect(platform.rect):
            self.dir[1] = -self.dir[1]
        self.rect.x = self.x
        self.rect.y = self.y
        

        


# main loop thath paint a screen with height and width
def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    running = True
    platform = Platform((width//2, height//2))
    ball = Ball((width//2, height//2), [10, 10])
    while running:
        for event in pygame.event.get():
            # make the platform move to the left and right with the arrow keys, holding down the left key will make it move faster
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    platform.x -= 50
                if event.key == pygame.K_RIGHT:
                    platform.x += 50
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        platform.update()
        ball.update(platform)
        screen.blit(platform.surf, platform.rect)
        screen.blit(ball.surf, ball.rect)
        pygame.display.flip()
        clock.tick(60)

# init main
if __name__ == '__main__':
    main()

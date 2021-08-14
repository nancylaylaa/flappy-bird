import pygame,sys,random
pygame.init()

SCREEN = pygame.display.set_mode((288,512))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock() #used for fps setting
FPS = 120 

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    SCREEN.fill((255,255,255))

    pygame.draw.circle(SCREEN,(0,0,255),(144,256),75)

    pygame.display.update()

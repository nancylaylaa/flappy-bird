import pygame,sys,random
pygame.init()

# 1 draw screen and init
SCREEN = pygame.display.set_mode((288,512)) # screen size
pygame.display.set_caption("Flappy Bird") # set window title
clock = pygame.time.Clock() # used for fps setting
FPS = 120 
# end1

# 2 loop
# main loop of game infinite loop
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # fill the background with white
    SCREEN.fill((255,255,255))

    # draw a solid blue circle in the center
    pygame.draw.circle(SCREEN,(0,0,255),(144,256),75)
    
    # update pygame
    pygame.display.update()

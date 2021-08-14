import pygame,sys,random
pygame.init()

# 1 draw screen and init
SCREEN = pygame.display.set_mode((288,512)) # screen size
pygame.display.set_caption("Flappy Bird") # set window title
clock = pygame.time.Clock() # used for fps setting
FPS = 120 
# end1

# 2 memuat gambar
# image load untuk memuat gambar
# convert atau convert_alpha (sama aja) untuk membuat surface compatible dengan format pygame agar tidak berat saat update surface
bg_surface = pygame.image.load('assets/background-day.png').convert()
bird_downflap = pygame.image.load('assets/bluebird-downflap.png').convert_alpha()
bird_midflap = pygame.image.load('assets/bluebird-midflap.png').convert_alpha()
bird_upflap = pygame.image.load('assets/bluebird-upflap.png').convert_alpha()
# get_rect untuk menentukan posisi aset dengan argumen center
bird_rect = bird_surface.get_rect(center = (50,256))

# 3 loop
# main loop of game infinite loop
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # SCREEN untuk menentukan apa yang akan ditampilkan pada surface sesuai urutan code
    # SCREEN.blit akan menampilkan aset gambar dengan argumen aset, posisi
    SCREEN.blit(bg_surface,(0,0))
    SCREEN.blit(bird_downflap,bird_rect)
    
    # update pygame
    pygame.display.update()

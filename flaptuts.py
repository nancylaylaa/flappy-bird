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

# 3 menambahkan fungsi matematika
start = False
bird_movement = 0
gravity = 0.1 # pixel FPS

# 4 loop
# main loop of game infinite loop
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            # mendeteksi tombol spasi yang dijalankan
            if event.key == pygame.K_SPACE and not start:
                start=True
            # tombol spasi untuk melompat
            if event.key == pygame.K_SPACE and start:
                bird_movement = -5 
     # burung bergerak ke bawah karena gravitasi           
     if start:
        bird_movement += gravity
        bird_rect.centery += bird_movement
        
    
    # SCREEN untuk menentukan apa yang akan ditampilkan pada surface sesuai urutan code
    # SCREEN.blit akan menampilkan aset gambar dengan argumen aset, posisi
    SCREEN.blit(bg_surface,(0,0))
    SCREEN.blit(bird_downflap,bird_rect)
    
    # update pygame
    pygame.display.update()




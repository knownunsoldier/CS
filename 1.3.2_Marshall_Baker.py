# imp libraries
import pygame
import random
pygame.init()


#win vars + setup
WIDTH = 600
HEIGHT = 300
spritewh = 30

#create win
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("super cool game v0.1")

#et al vars
fps = 60
pac_velo = 5
ghost_velo = 3
updown = "up"
bullets_fired = []
white = (255, 255, 255)
green = (0, 255, 0)


#set imgs
BGimg = pygame.image.load("pacScreen.gif") #make bg obj
BGimg = pygame.transform.scale(BGimg, (WIDTH, HEIGHT))

pacimg = pygame.image.load("pac.gif") #make pacman obj
pacimg = pygame.transform.scale(pacimg, (spritewh, spritewh))

gstimg = pygame.image.load("ghost.gif") #make ghost obj
gstimg = pygame.transform.scale(gstimg, (spritewh, spritewh))

#make recs
ghost = pygame.Rect(WIDTH-spritewh, 100, spritewh, spritewh)
pac = pygame.Rect(100, 100, spritewh, spritewh) #4params xloc, yloc, w, h

#funcs in mainloop
def player_movement():
    if keys_pressed[pygame.K_UP] and pac.y>0:
        pac.y -= pac_velo
    if keys_pressed[pygame.K_DOWN] and pac.y<HEIGHT-spritewh:
        pac.y += pac_velo
    if keys_pressed[pygame.K_LEFT] and pac.x-spritewh>0:
        pac.x -= pac_velo 
    if keys_pressed[pygame.K_RIGHT] and pac.x<WIDTH//2:
        pac.x += pac_velo
def ghost_movement():
    global updown#movement 
    if updown == "down":

        ghost.y += ghost_velo
    if updown == "up":

        ghost.y -= ghost_velo
    #bounce
    if ghost.y>HEIGHT-spritewh:
        updown = "up"
    if ghost.y<10:
        updown = "down"
    #jukes
    juke = random.randint(0,50)
    if juke == 42:
        print("juke!")
        if updown == "down":
            updown = "up"
        if updown == "up":
            updown = "down"

#func update screen--important
def update_screen():
    WIN.blit(BGimg, (0,0))
    WIN.blit(pacimg, (pac.x,pac.y))
    WIN.blit(gstimg, (ghost.x, ghost.y))
    for bullet in bullets_fired:
        pygame.draw.rect(WIN, green, bullet) #on what, what color, what to draw
    pygame.display.update()

#mainloop
keys_pressed = []
def go():
    global keys_pressed, bullets_fired
    clock = pygame.time.Clock() #inst clock obj
    running = True
    while running:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #click type right x
                running = False
                pygame.quit() #close win
            if event.type == pygame.KEYDOWN: #any?
                if event.key == pygame.K_SPACE:
                    bullet = pygame.Rect(pac.x+spritewh//2, pac.y+(spritewh/2), 13, 7)
                    bullets_fired.append(bullet)
                    print(bullets_fired)
        keys_pressed = pygame.key.get_pressed()
        print(keys_pressed)
        update_screen()
        player_movement()
        ghost_movement()
go()
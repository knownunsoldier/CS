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
ghost_health = 5
bullet_velo = 7
max_bullet = 4
bullets_fired = []




updown = "up"
white = (255, 255, 255)
green = (0, 255, 0)


#set imgs
BGimg = pygame.image.load("encounter.gif") #make bg obj
BGimg = pygame.transform.scale(BGimg, (WIDTH, HEIGHT))

pacimg = pygame.image.load("heart.gif") #make pacman obj
pacimg = pygame.transform.scale(pacimg, (spritewh, spritewh))

gstimg = pygame.image.load("sans.gif") #make ghost obj
gstimg = pygame.transform.scale(gstimg, (spritewh*2, spritewh*3))

#make recs
ghost = pygame.Rect(WIDTH-spritewh*2, 100, spritewh*2, spritewh*3)
pac = pygame.Rect(100, 100, spritewh, spritewh) #4params xloc, yloc, w, h

#hand font
pygame.font.init()
ghost_health_fond=pygame.font.SysFont("comicsans", 40)

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
    if ghost.y>HEIGHT-spritewh*3:
        updown = "up"
    if ghost.y<10:
        updown = "down"
    #jukes
    juke = random.randint(0,50)
    if juke == 42:
        #print("juke!")
        if updown == "down":
            updown = "up"
        if updown == "up":
            updown = "down"
def bullet_actions():
    global bullets_fired
    global ghost_health
    for bullet in bullets_fired:
        bullet.x +=bullet_velo
        if bullet.x>WIDTH:
            bullets_fired.remove(bullet)
        if bullet.colliderect(ghost):
            bullets_fired.remove(bullet)
            ghost_health-=1
            print(ghost_health)
def win_screen(text, size):
    winner_font=pygame.font.SysFont('comicsans', size)
    winner_font_text = winner_font.render(text, 1, white)
    WIN.blit(winner_font_text, (20, 20))
    pygame.display.update()
    pygame.time.delay(3000)#3sec
    WIN.blit(BGimg, (0,0))
def update_screen():
    WIN.blit(BGimg, (0,0))
    WIN.blit(pacimg, (pac.x,pac.y))
    WIN.blit(gstimg, (ghost.x, ghost.y))

    for bullet in bullets_fired:
        pygame.draw.rect(WIN, green, bullet) #on what, what color, what to draw
    ghost_health_text=ghost_health_fond.render("Ghost Health: "+str(ghost_health), 1, white)
    WIN.blit(ghost_health_text, (WIDTH-ghost_health_text.get_width(), 0))

    pygame.display.update()

#mainloop
keys_pressed = []
start_game=False
def go():
    global keys_pressed, bullets_fired, ghost_health
    clock = pygame.time.Clock() #inst clock obj
    print("Arrow keys to move, spacebar to fire. Hit enter to start game.")

    ghost_health=5
    running = True
    start_game=False
    keys_pressed=[]
    while running:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #click type right x
                running = False
                pygame.quit() #close win
            if event.type == pygame.KEYDOWN: #any?
                if event.key == pygame.K_SPACE and len(bullets_fired)<max_bullet:
                    bullet = pygame.Rect(pac.x+spritewh//2, pac.y+(spritewh/2), 13, 7)
                    bullets_fired.append(bullet)
                    #print(bullets_fired)
                if event.key==pygame.K_RETURN and start_game==False:
                    start_game=True
        keys_pressed = pygame.key.get_pressed()
        #print(keys_pressed)
        update_screen()

        if ghost_health<=0:
            win_screen("you won!!!", 120)
            win_screen("hit enter to play again", 80)
            break#exit wloop
        if start_game==True:
            player_movement()
            ghost_movement()
            bullet_actions()
    go()
go()
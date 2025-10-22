##---------- Imports and Setup
import pygame
pygame.init()

##-----------WINDOW/SCREEN
width = 800
height = 400

win = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()




##-----------VARIABLES
FPS = 60
SPRITEWH = 70

gray = (49, 54, 56)
orange = (240, 157, 81)

ghost_x = 300
ghost_y = 100
ghost_accel = 0.4
ghost_speed = 0
ghost_on_ground = False

spriteFaceRight = True
GHOSTimg = pygame.image.load('ghost.gif')
GHOSTimgL = pygame.transform.scale(GHOSTimg, (SPRITEWH, SPRITEWH))
##-----------IMAGES



##-----------PLATFORMS
platforms = [
    pygame.Rect(100, 300, 400, 50),
    pygame.Rect(100, 250, 50, 50),
    pygame.Rect(450, 250, 300, 50)
    ]
##-----------FUNCTIONS
def update_screen():
    #fill background
    win.fill(gray)
    #draw platforms
    for p in platforms:
        pygame.draw.rect(win, orange, p)
    #draw sprite - DIFFERENT THAN WEBX - VSCODE DIDN'T LIKE IT
    if spriteFaceRight:
        win.blit(GHOSTimgL, (ghost_x, ghost_y))
    else:
        win.blit(pygame.transform.flip(GHOSTimgL, True, False), (ghost_x, ghost_y))
    pygame.display.update()

def check_collision():
    global ghost_speed, ghost_on_ground
    global y_collision, ghost_y, new_ghost_y
    global ghost_x, new_ghost_x

    #vertical fall
    ghost_speed += ghost_accel
    new_ghost_y += ghost_speed

    #draw rectangle of new possible locations to check if location is availible.
    new_ghost_rect = pygame.Rect(ghost_x, new_ghost_y, SPRITEWH, SPRITEWH)
    y_collision = False
    ghost_on_ground = False

    #check to see if we hit platform
    for p in platforms:
        if p.colliderect(new_ghost_rect): #check if touching
            print("hit feet")
            y_collision = True
            ghost_on_ground = True
            ghost_speed = 0
            break #stop checking
    if y_collision == False:
        ghost_y = new_ghost_y


    #horizontal move
    x_collision = False
    for p in platforms:
        if p.colliderect(new_ghost_rect):
            print("hit face")
            x_collision = True
            break
    if x_collision == False:
        ghost_x = new_ghost_x
    new_ghost_rect = pygame.Rect(new_ghost_x, ghost_y, SPRITEWH, SPRITEWH)








    #fall off screen reset
def check_keypress(keys_pressed):
    global new_ghost_x, ghost_speed
    if keys_pressed[pygame.K_a]:
        new_ghost_x -= 3
    if keys_pressed[pygame.K_s]:
        new_ghost_x +=3



##-----------UPDATE SCREEN


##-----------MAINLOOP
def go():
    global spriteFaceRight, new_ghost_x, new_ghost_y
    running = True
    while running:
        clock.tick(FPS) #reuglate loop speed
        keys_pressed = pygame.key.get_pressed()
        #print(keys_pressed)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("you quit")
                    running = False
                    pygame.quit()
                if event.key == pygame.K_a:
                    spriteFaceRight = False
                if event.key == pygame.K_s:
                    spriteFaceRight = False
        new_ghost_x = ghost_x
        new_ghost_y = ghost_y
        check_collision() 
        check_keypress(keys_pressed)
        update_screen()
go()
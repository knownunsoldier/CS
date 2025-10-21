

'''
 - CONSTANTS + VARIABLES
 - Setup WIN/Screen
 - setup main game loop
    - while running = True:
 - update screen function
 - Create platforms
 - get sprite image onto window

DAY2
 - image falling
 - collision detection w/ platforms
    - "Can I move there?"  
         Store last X,Y values so we can return if collide/overlap
    - Vertical then Horizontal
 - arrow keys
   - a = LEFT
   - d = RIGHT
   - w = JUMP
 - Reset to top of screen when jump off platform
'''
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
    #draw sprite
    if spriteFaceRight:
        win.blit(GHOSTimgL, (ghost_x, ghost_y))
    pygame.display.update()

##-----------UPDATE SCREEN


##-----------MAINLOOP
def go():
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
        update_screen()

go()
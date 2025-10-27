'''
DAY 1 
- import libraries 
- create our window / GUI
- setup main game loop
- while running = True.
- update sreen function 
- get 3 images onto window
- create rectangles to control each image
- move pac w/ arrows 
DAY 2
- move pac w/ arrows
- keep Pac on left side
- create ghost path movement
- create bullets 
DAY 3
- move bullets
- determine bullet collisions
- display score on screen
- determine win condition
- add Break and Restart
- display Winner message
- start game when ENTER KEY clicked 
'''
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
#
#set imgs
BGimg = pygame.image.load("pacScreen.gif") #make img obj
BGimg = pygame.transform.scale(BGimg, (WIDTH, HEIGHT))

pacimg = pygame.image.load("pac.gif") #make img objp
pacimg = pygame.transform.scale(pacimg, (spritewh, spritewh))

gstimg = pygame.image.load("ghost.gif") #make img objp
gstimg = pygame.transform.scale(gstimg, (spritewh, spritewh))







def go():
    running = True
    while running:
        print("hey")
go()
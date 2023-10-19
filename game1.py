import pygame
import random
import sys

#Initialize pygame
pygame.init()

#dimensions
screen_width = 800
screen_height = 600
tile_size = 64
rectangle_height = 150

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Unda da Sea!')

#define a function to draw background

def draw_background(screen):
    #load our tiles
    water = pygame.image.load("assets/sprites/water.png").convert()
    sand = pygame.image.load("assets/sprites/sand_top.png").convert()
    seagrass = pygame.image.load("assets/sprites/seagrass.png").convert()
    #use png transparency
    sand.set_colorkey((0,0,0))
    seagrass.set_colorkey((0,0,0))

    #fill the screen
    for x in range(0, screen_width, tile_size):
        for y in range(0, screen_height, tile_size):
           screen.blit(water, (x, y))

    #draw sand
    for x in range(0, screen_width, tile_size):
#        screen.blit(sand, (x, screen_height - tile_size))
        for y in range(screen_height - rectangle_height, screen_height, tile_size - 10):
            screen.blit(sand, (x,y))

    #add seagrass randomly at the bottom of the beach
    for _ in range(20):
        x = random.randint(0, screen_width)
        y = random.randint(screen_height - rectangle_height - tile_size, screen_height - tile_size/2)
        screen.blit(seagrass, (x, y))

#Main Loop
running = True
background = screen.copy()
draw_background(background)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #draw background
    screen.blit(background, (0,0))

    # update the display
    pygame.display.flip()

#quit pygame
pygame.quit()
import random

import pygame
import sys

from background import draw_background
from game_parameters import *

#Initialize pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Collecting Pygame Events')

#Main Loop
running = True
background = screen.copy()
draw_background(background)


while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
                running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print('you pressed up')
            if event.key == pygame.K_DOWN:
                print('you pressed down')
            if event.key == pygame.K_RIGHT:
                print('you pressed right')
            if event.key == pygame.K_LEFT:
                print('you pressed left')

    # draw background
    screen.blit(background, (0, 0))

    #update the displya
    pygame.display.flip()

    #limit the frame rate
    #clock.tick(60)

#quit pygame
pygame.quit()
sys.exit()
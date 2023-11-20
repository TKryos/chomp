import pygame
import sys

#Initialize pygame
pygame.init()

#screen dimensions
screen_width = 1280
screen_height = 660

#define colors
BLUE = (0, 0, 255)
BROWN = (224, 161, 52)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Blue Background with Brown Rectangle')

#Main Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #fill screen with blue
    screen.fill(BLUE)

    #draw the brown rectangle
    rectangle_height = 150
    pygame.draw.rect(screen, BROWN, (0, screen_height - rectangle_height, screen_width, rectangle_height))
    #pygame.draw.polygon(screen, BROWN, [(200, screen_height - rectangle_height), (300, 150), (500, 150), (600, screen_height - rectangle_height)])
    #update the display
    pygame.display.flip()

#quit pygame
pygame.quit()
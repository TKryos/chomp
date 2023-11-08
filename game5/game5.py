import pygame
import random
import sys

from game_parameters import *
from fish import Fish, fishes
from background import draw_background, FONT_SIZE
from player import Player

#initialize pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Unda da Sea!')

#clock object
clock = pygame.time.Clock()

# Main Loop
running = True
background = screen.copy()
draw_background(background)

#draw fish on the screen
for _ in range(5):
    fishes.add(Fish(random.randint(SCREEN_WIDTH, 2 * SCREEN_WIDTH - TILE_SIZE),
                    random.randint(FONT_SIZE, SCREEN_HEIGHT - RECTANGLE_HEIGHT - 2*TILE_SIZE)))

player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)


while running:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False
        #control fish with keyboard
        player.stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                print('you pressed up')
                player.move_up()
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                print('you pressed left')
                player.move_left()
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                print('you pressed down')
                player.move_down()
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                print('you pressed right')
                player.move_right()


    # draw background
    screen.blit(background, (0, 0))

    #update our fish location
    fishes.update()

    #update player location
    player.update()

    #check if any fish is off the screen
    for fish in fishes:
        if fish.rect.x < -fish.rect.width: #can also use the tile size
            fishes.remove(fish) #remove the fish from the sprite group
            fishes.add(Fish(random.randint(SCREEN_WIDTH + TILE_SIZE / 2, SCREEN_WIDTH + TILE_SIZE),
                            random.randint(FONT_SIZE + TILE_SIZE/2, SCREEN_HEIGHT - RECTANGLE_HEIGHT - 2 * TILE_SIZE)))


    #draw green fish
    fishes.draw(screen)

    #draw player fish
    player.draw(screen)

    #update the display
    pygame.display.flip()

    #limit the frame rate
    clock.tick(60)

#quit pygame
pygame.quit()
sys.exit()

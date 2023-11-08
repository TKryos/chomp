import pygame
import random
import sys

from game_parameters import *
from fish import Fish, fishes
from background import *
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
                    random.randint(CUSTOM_FONT_SIZE, SCREEN_HEIGHT - RECTANGLE_HEIGHT - 2*TILE_SIZE)))

#create a player fish
player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

#initialize score for fish game
score = 0
score_font = pygame.font.Font("../assets/fonts/Black_Crayon.ttf", SCORE_FONT_SIZE)

#load the sound effects
chomp = pygame.mixer.Sound("../assets/sounds/chomp.wav")

while running:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False
        #control fish with keyboard
        #player.stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                #print('you pressed up')
                player.move_up()
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                #print('you pressed left')
                player.move_left()
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                #print('you pressed down')
                player.move_down()
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                #print('you pressed right')
                player.move_right()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                #print('you pressed up')
                player.stop_y()
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                #print('you pressed left')
                player.stop_x()
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                #print('you pressed down')
                player.stop_y()
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                #print('you pressed right')
                player.stop_x()


    # draw background
    screen.blit(background, (0, 0))

    #update our fish location
    fishes.update()

    #update player location
    player.update()

    #check for player collision

    result = pygame.sprite.spritecollide(player, fishes, True)
    #print(result)
    if result:
        #play chomp
        pygame.mixer.Sound.play(chomp)
        score += len(result)
        print(score)
        #draw more green fish on the screen
        for _ in range(len(result)):
            fishes.add(Fish(random.randint(SCREEN_WIDTH + TILE_SIZE / 2, SCREEN_WIDTH + TILE_SIZE),
                            random.randint(CUSTOM_FONT_SIZE + TILE_SIZE / 2,
                                           SCREEN_HEIGHT - RECTANGLE_HEIGHT - 1.5*TILE_SIZE)))

    #check if any fish is off the screen
    for fish in fishes:
        if fish.rect.x < -fish.rect.width: #can also use the tile size
            fishes.remove(fish) #remove the fish from the sprite group
            fishes.add(Fish(random.randint(SCREEN_WIDTH + TILE_SIZE / 2, SCREEN_WIDTH + TILE_SIZE),
                            random.randint(CUSTOM_FONT_SIZE + TILE_SIZE/2,
                                           SCREEN_HEIGHT - RECTANGLE_HEIGHT - 1.5*TILE_SIZE)))


    #draw green fish
    fishes.draw(screen)

    #draw player fish
    player.draw(screen)

    #draw the score on the screen
    text = score_font.render(f"SCORE : {score}", True, (255, 0, 0))
    screen.blit(text, (SCREEN_WIDTH - TILE_SIZE * 5/2, CUSTOM_FONT_SIZE - 32))
    #update the display
    pygame.display.flip()

    #limit the frame rate
    clock.tick(60)

#quit pygame
pygame.quit()
sys.exit()

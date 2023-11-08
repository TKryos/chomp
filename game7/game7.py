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
add_fish(5)

# draw enemies on the screen
add_enemies(3)

#create a player fish
player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

#initialize score for fish game
score = 0
score_font = pygame.font.Font("../assets/fonts/Black_Crayon.ttf", SCORE_FONT_SIZE)

#life = 3
#life_font = pygame.font.Font("../assets/fonts/Black_Crayon.ttf", LIFE_FONT_SIZE)
#load the sound effects
chomp = pygame.mixer.Sound("../assets/sounds/chomp.wav")
hurt = pygame.mixer.Sound("../assets/sounds/hurt.wav")
bubbles = pygame.mixer.Sound("../assets/sounds/bubbles.wav")

#add alternate fish image
life_icon = pygame.image.load("../assets/sprites/orange_fish_alt.png").convert()
life_icon.set_colorkey((0, 0, 0))

#set the number of lives
lives = NUM_LIVES

#Main Loop
while lives > 0 and running:
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
    enemies.update()
    #update player location
    player.update()

    #check for player collision with fish
    result = pygame.sprite.spritecollide(player, fishes, True)

    #print(result)
    if result:
        #play chomp
        pygame.mixer.Sound.play(chomp)
        score += len(result)
        print(score)
        #draw more green fish on the screen
        add_fish(len(result))
        #for _ in range(len(result)):
        #    fishes.add(Fish(random.randint(SCREEN_WIDTH + TILE_SIZE / 2, SCREEN_WIDTH + TILE_SIZE),
        #                    random.randint(CUSTOM_FONT_SIZE + TILE_SIZE / 2,
        #                                   SCREEN_HEIGHT - RECTANGLE_HEIGHT - 1.5*TILE_SIZE)))

    #check for player collision with enemy
    result = pygame.sprite.spritecollide(player, enemies, True)

    if result:
        #play hurt sound
        pygame.mixer.Sound.play(hurt)

        #lose lives if hurt
        lives -= len(result)

        #draw more enemy fish on the screen
        add_enemies(len(result))

    #check if any fish is off the screen
    for fish in fishes:
        if fish.rect.x < -fish.rect.width: #can also use the tile size
            fishes.remove(fish) #remove the fish from the sprite group
            add_fish(1)
            #fishes.add(Fish(random.randint(SCREEN_WIDTH + TILE_SIZE / 2, SCREEN_WIDTH + TILE_SIZE),
            #                random.randint(CUSTOM_FONT_SIZE + TILE_SIZE/2,
            #                               SCREEN_HEIGHT - RECTANGLE_HEIGHT - 1.5*TILE_SIZE)))

    # check if any enemy is off the screen
    for enemy in enemies:
        if enemy.rect.x < -enemy.rect.width:  # can also use the tile size
            enemies.remove(enemy)  # remove the fish from the sprite group
            add_enemies(1)

    #draw green fish
    fishes.draw(screen)
    player.draw(screen)
    enemies.draw(screen)

    #draw the score on the screen
    text = score_font.render(f"SCORE : {score}", True, (255, 0, 0))
    screen.blit(text, (SCREEN_WIDTH - TILE_SIZE * 5/2, CUSTOM_FONT_SIZE - 32))

    #draw lives in the lower left corner
    for i in range(lives):
        screen.blit(life_icon, (i * TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE))

    #update the display
    pygame.display.flip()

    #limit the frame rate
    clock.tick(60)
#once all lives are gone
#create new background when game over
screen.blit(background, (0, 0))

#show game over message
message = score_font.render("GAME OVER!!!", True, (255, 0, 0))
screen.blit(message, (SCREEN_WIDTH/2 - message.get_width()/2, SCREEN_HEIGHT/2 - message.get_height()))
score_text = score_font.render(f"Score: {score}",True,  (255, 0, 0))
screen.blit(score_text, (SCREEN_WIDTH/2 - score_text.get_width()/2, SCREEN_HEIGHT/2))

#update display
pygame.display.flip()

#play game over sound effect
pygame.mixer.Sound(bubbles)

#wait for user to exit the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

#quit pygame
#pygame.quit()
#sys.exit()

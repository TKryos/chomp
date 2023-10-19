import pygame
import random
import sys

#Initialize pygame
pygame.init()

#dimensions
screen_width = 800
screen_height = 600
tile_size = 64
rectangle_height = 100

#create screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Unda da Sea!')

#load our game font
custom_font = pygame.font.Font("assets/fonts/Brainfish_Rush.ttf", 120)

def draw_background(surf):
    #load our tiles
    waves = pygame.image.load("assets/sprites/waves.png").convert()
    water = pygame.image.load("assets/sprites/water.png").convert()
    sand_top = pygame.image.load("assets/sprites/sand_top.png").convert()
    seagrass = pygame.image.load("assets/sprites/seagrass.png").convert()
    sand = pygame.image.load("assets/sprites/sand.png").convert()
    #use png transparency
    sand_top.set_colorkey((0,0,0))
    seagrass.set_colorkey((0,0,0))
    waves.set_colorkey((0,0,0))

    #fill the screen
    for x in range(0, screen_width, tile_size):
        surf.blit(waves, (x, 0))

    for x in range(0, screen_width, tile_size):
        for y in range(tile_size, screen_height, tile_size):
           surf.blit(water, (x, y))

    #draw sand
    for x in range(0, screen_width, tile_size):
        surf.blit(sand_top, (x, screen_height - rectangle_height))

    for x in range(0, screen_width, tile_size):
        for y in range(screen_height - rectangle_height + tile_size, screen_height, tile_size):
            surf.blit(sand, (x, y))

    #add seagrass randomly at the bottom of the beach
    for _ in range(20):
        x = random.randint(0, screen_width)
        y = random.randint(screen_height - rectangle_height - tile_size, screen_height - tile_size/2)
        surf.blit(seagrass, (x, y))

    #draw the text
    text = custom_font.render('Chomp', True, (255, 0, 0))
    surf.blit(text, (screen_width/2 - text.get_width()/2, 0))


#time for the fish
def draw_fishes(surf):
    #load some fish tiles from sprites
    green_fish = pygame.image.load("assets/sprites/green_fish.png").convert()
    orange_fish = pygame.image.load("assets/sprites/orange_fish.png").convert()
    puffer_fish = pygame.image.load("assets/sprites/puffer_fish.png").convert()
    green_fish.set_colorkey((0, 0, 0)) #set png transparency
    orange_fish.set_colorkey((0, 0, 0))
    puffer_fish.set_colorkey((0, 0, 0))

    for _ in range(random.randint(1, 5)):
        x = random.randint(0, screen_width - tile_size)
        y = random.randint(custom_font.get_height(), screen_height - rectangle_height - 2*tile_size)
        flip = random.randint(0, 1)
        if flip == 0:
            surf.blit(green_fish, (x, y))
        else:
            green_fish = pygame.transform.flip(green_fish, True, False)
            surf.blit(green_fish, (x, y))

    for _ in range(random.randint(1, 5)):
        x = random.randint(0, screen_width - tile_size)
        y = random.randint(custom_font.get_height(), screen_height - rectangle_height - 2*tile_size)
        flip = random.randint(0, 1)
        if flip == 0:
            surf.blit(orange_fish, (x, y))
        else:
            orange_fish = pygame.transform.flip(orange_fish, True, False)
            surf.blit(orange_fish, (x, y))

    for _ in range(random.randint(1, 5)):
        x = random.randint(0, screen_width - tile_size)
        y = random.randint(custom_font.get_height(), screen_height - rectangle_height - 2*tile_size)
        flip = random.randint(0, 1)
        if flip == 0:
            surf.blit(puffer_fish, (x, y))
        else:
            puffer_fish = pygame.transform.flip(puffer_fish, True, False)
            surf.blit(puffer_fish, (x, y))


# Main Loop
running = True
background = screen.copy()
draw_background(background)
draw_fishes(background)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
    # draw background
    screen.blit(background, (0, 0))

    #draw fish

    # update the display
    pygame.display.flip()

# quit pygame
pygame.quit()





















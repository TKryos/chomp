import pygame
from game_parameters import *
from fish import Fish, fishes
import random
from enemy import Enemy, enemies

def draw_background(surf):
    #load our tiles
    waves = pygame.image.load("../assets/sprites/waves.png").convert()
    water = pygame.image.load("../assets/sprites/water.png").convert()
    sand_top = pygame.image.load("../assets/sprites/sand_top.png").convert()
    seagrass = pygame.image.load("../assets/sprites/seagrass.png").convert()
    sand = pygame.image.load("../assets/sprites/sand.png").convert()
    #use png transparency
    sand_top.set_colorkey((0,0,0))
    seagrass.set_colorkey((0,0,0))
    waves.set_colorkey((0,0,0))

    #fill the screen
    #surf.fill(255, 255, 255)
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        surf.blit(waves, (x, 0))

    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        for y in range(TILE_SIZE, SCREEN_HEIGHT, TILE_SIZE):
           surf.blit(water, (x, y))

    #draw sand
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        surf.blit(sand_top, (x, SCREEN_HEIGHT - RECTANGLE_HEIGHT))

    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        for y in range(SCREEN_HEIGHT - RECTANGLE_HEIGHT + TILE_SIZE, SCREEN_HEIGHT, TILE_SIZE):
            surf.blit(sand, (x, y))

    #add seagrass randomly at the bottom of the beach
    for _ in range(20):
        x = random.randint(0, SCREEN_WIDTH)
        y = random.randint(SCREEN_HEIGHT - RECTANGLE_HEIGHT - TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE/2)
        surf.blit(seagrass, (x, y))

    #draw the text
    custom_font = pygame.font.Font("../assets/fonts/Brainfish_Rush.ttf", CUSTOM_FONT_SIZE)
    text = custom_font.render('Chomp', True, (255, 0, 0))
    surf.blit(text, (SCREEN_WIDTH/2 - text.get_width()/2, 0))

def add_fish(num_fish):
    for _ in range(num_fish):
        fishes.add(Fish(random.randint(SCREEN_WIDTH, 2 * SCREEN_WIDTH - TILE_SIZE),
                        random.randint(CUSTOM_FONT_SIZE, SCREEN_HEIGHT - RECTANGLE_HEIGHT - 2 * TILE_SIZE)))

def add_enemies(num_enemies):
    for _ in range(num_enemies):
        enemies.add(Enemy(random.randint(SCREEN_WIDTH, 2 * SCREEN_WIDTH - TILE_SIZE),
                        random.randint(CUSTOM_FONT_SIZE, SCREEN_HEIGHT - RECTANGLE_HEIGHT - 2 * TILE_SIZE)))

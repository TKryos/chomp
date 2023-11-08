import pygame
import random
import sys

from fish import Fish, fishes #importing a class and a Sprite Group


#Initialize pygame
pygame.init()

#dimensions
screen_width = 800
screen_height = 600
tile_size = 64
rectangle_height = 100

#initialize the text variables
custom_font = pygame.font.Font("../assets/fonts/Brainfish_Rush.ttf", 128)
text = custom_font.render('Chomp', True, (255, 0, 0))

#create screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Unda da Sea!')

#clock object
clock = pygame.time.Clock()

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

# Main Loop
running = True
background = screen.copy()
draw_background(background)

#draw fish on the screen
for _ in range(5):
    fishes.add(Fish(random.randint(screen_width, 2 * screen_width - tile_size),
                    random.randint(custom_font.get_height(), screen_height - rectangle_height - 2*tile_size)))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
    # draw background
    screen.blit(background, (0, 0))

    #update our fish location
    fishes.update()

    #check if any fish is off the screen
    for fish in fishes:
        if fish.rect.x < -fish.rect.width: #can also use the tile size
            fishes.remove(fish) #remove the fish from the sprite group
            fishes.add(Fish(random.randint(screen_width + tile_size / 2, screen_width + tile_size),
                            random.randint(custom_font.get_height(), screen_height - rectangle_height - 2 * tile_size)))


    #draw the fish
    fishes.draw(screen)

    #update the display
    pygame.display.flip()

    #limit the frame rate
    clock.tick(60)

#quit pygame
pygame.quit()
sys.exit()
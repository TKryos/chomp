import pygame
from game_parameters import *
#create pygame sprite class for a player

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.forward_image = pygame.image.load("../assets/sprites/orange_fish.png")
        self.reverse_image = pygame.transform.flip(self.forward_image, True, False)
        self.image = self.forward_image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.speed = PLAYER_SPEED
#       self.x_speed = 0
#       self.y_speed = 0

#   def move_up(self):
#       self.y_speed = -1 * PLAYER_SPEED
#
#   def move_down(self):
#       self.y_speed = PLAYER_SPEED
#
#   def move_left(self):
#       self.x_speed = -1 * PLAYER_SPEED
#       self.image = self.reverse_image
#   def move_right(self):
#       self.x_speed = PLAYER_SPEED
#       self.image = self.forward_image
#   def stop_x(self):
#       self.x_speed = 0
#       #self.y_speed = 0
#       #print(self.x, self.y)
#       #print(self.rect.x, self.rect.y)
#
#   def stop_y(self):
#       #self.x_speed = 0
#       self.y_speed = 0
#       #print(self.x, self.y)
#       #print(self.rect.x, self.rect.y)
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed
    def draw(self, surf):
        surf.blit(self.image, self.rect)
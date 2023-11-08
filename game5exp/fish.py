#create a pygame sprite class for a fish

import pygame
import random
from game_parameters import *

class Fish(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.forward_image = pygame.image.load("../assets/sprites/green_fish.png").convert()
        self.reverse_image = pygame.transform.flip(self.forward_image, True, False)
        self.image = self.forward_image
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = random.uniform(MIN_SPEED, MAX_SPEED)
        self.rect.center = (x, y)

    def update_backward(self):
        self.x += -self.speed
        self.rect.x = self.x

    def update_forward(self):
        self.x += self.speed
        self.rect.x = self.x
    def draw_forward(self, surf):
        surf.blit(self.forward_image, self.rect)

    def draw_backward(self, surf):
        surf.blit(self.reverse_image, self.rect)


fishes = pygame.sprite.Group()


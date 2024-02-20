import pygame
from random import randint as rnd


class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def receive_strenght(self):
        pass

    def breake(self):
        pass

    def coordinate_x(self):
        pass

    def coordinate_y(self):
        pass

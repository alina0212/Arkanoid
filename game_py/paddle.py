import pygame
from pygame.locals import *


class Paddle():
    """
    responsible for displaying and controlling the paddle
    """

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('../image/paddle2.png')
        self.image = pygame.transform.scale(self.image, (200, 50))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.coordinates = [0, 0]  # initial coordinates of the platform
        self.speed = 10  # speed of the platform movement

    """
    method that draws a paddle
    """
    def draw(self):
        self.screen.blit(self.image, self.rect)

    """
    method that is responsible for the movement of the platform and for keeping it within its boundaries
    """
    def move(self):
        # getting the status of keystrokes
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= self.speed
        if keys[K_RIGHT]:
            self.rect.x += self.speed

        # restricting the movement of the platform to the screen borders
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screen_rect.right:
            self.rect.right = self.screen_rect.right


import pygame
from pygame.locals import *


class Paddle():
    """
    відповідає за відображення і керуванням paddle
    """

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('../image/paddle2.png')
        self.image = pygame.transform.scale(self.image, (200, 50))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.coordinates = [0, 0]  # Початкові координати платформи
        self.speed = 10  # Швидкість руху платформи

    """
    метод який малює paddle
    """
    def draw(self):
        self.screen.blit(self.image, self.rect)

    """
    метод що відповідає за рух платформи і щоб вона не виходила за свої межі
    """
    def move(self):
        # Отримання стану натискання клавіш
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= self.speed
        if keys[K_RIGHT]:
            self.rect.x += self.speed

        # Обмеження руху платформи до меж екрану
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screen_rect.right:
            self.rect.right = self.screen_rect.right


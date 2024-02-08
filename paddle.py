import pygame

class Paddle():


    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('image/paddle2.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.coordinates = [0, 0]  # Початкові координати платформи

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def move(self):
        pass

    def coordinates(self):

        return self.coordinates
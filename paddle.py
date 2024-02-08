import pygame

class Paddle():

   c
        self.screen = screen
        self.image = pygame.image.load('image/paddle2.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx

    def draw(self):
        self.screen.blit(self.image, self.rect)

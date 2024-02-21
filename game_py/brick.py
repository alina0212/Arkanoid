import pygame
from random import randint as rnd


class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, screen, color):
        super().__init__()
        self.color = color
        self.screen = screen
       # self.rect = self.image.get_rect()
        #self.rect.x = x
       # self.rect.y = y
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.block_height = 40
        self.block_width = 100
        self.margin_y = 20
        self.margin_x = 20
        self.num_rows = 4
        self.num_cols = 7

    def generate_block_list(self):
        block_list = []
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                x = self.margin_x + i * (self.block_width + self.margin_x)
                y = self.margin_y + j * (self.block_height + self.margin_y)
                block = Brick(x, y, self.screen, self.color)
                block_list.append(block)
        return block_list
    
    def receive_strenght(self):
        pass

    def breake(self):
        pass

    def coordinate_x(self):
        pass

    def coordinate_y(self):
        pass

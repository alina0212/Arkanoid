import pygame


class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, color, width=100, height=40):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class BrickContainer:
    def __init__(self, screen):
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.margin_x = 15
        self.margin_y = 20
        self.num_rows = 4
        self.num_cols = 6

    def generate_block_list(self, color):
        block_list = []
        block_width = 120
        block_height = 40
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                x = self.margin_x + i * (block_width + self.margin_x)
                y = self.margin_y + j * (block_height + self.margin_y)
                block = Block(x, y, color)
                block_list.append(block)
        return block_list

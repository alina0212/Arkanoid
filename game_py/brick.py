import pygame
from constants import num_cols, num_rows, margin_y, margin_x, width, height, block_width, block_height


class Block(pygame.sprite.Sprite):
    """
    a subclass of the pygame.sprite.Sprite class and is responsible for representing blocks in the game
    """

    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class BrickContainer:
    """
    responsible for creating and controlling the block container in the game
    """

    def __init__(self, screen):
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()

    def generate_block_list(self, color):
        """
        list of blocks is created
        :param color:
        :return:
        """
        block_list = []
        for i in range(num_cols):
            for j in range(num_rows):
                # calculates the position of each block based on the indentation and size of the blocks
                x = margin_x + i * (block_width + margin_x)
                y = margin_y + j * (block_height + margin_y)
                block = Block(x, y, color)
                block_list.append(block)
                # creates a new block and adds it to the list of blocks
        return block_list

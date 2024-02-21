# import sys
import pygame
from random import randint as rnd

from brick import Brick
# from game_py.brick import Brick
from paddle import Paddle
from ball import Ball


# def run():
#     pygame.init()
#     screen = pygame.display.set_mode((800, 600))
#     pygame.display.set_caption("Arkanoid")
#     background_image = pygame.image.load('../image/backgroung2.png')
#
#     paddle = Paddle(screen)
#     ball = Ball(screen, paddle)
#
#     clock = pygame.time.Clock()
#
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 if (event.key == pygame.K_LSHIFT or
#                         event.key == pygame.K_RSHIFT):
#                     ball.start_move()
#
#         paddle.move()
#         ball.move()
#         ball.collision()
#         screen.blit(background_image, (0, 0))
#         paddle.draw()
#         ball.draw_ball()
#         pygame.display.flip()
#         clock.tick(60)
#
# run()

class GameWindow:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def run(self):
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Arkanoid")
        background_image = pygame.image.load('../image/backgroung2.png')

########################################################3
        paddle = Paddle(screen)
        ball = Ball(screen, paddle, self.difficulty)
        # # Створення списку блоків
        # block_list = [pygame.Rect(20 + 110 * i, 20 + 50 * j, 100, 40) for i in range(7) for j in range(4)]
        #
        # # Створення групи спрайтів для блоків
        # block_sprites = pygame.sprite.Group()
        # for block_rect in block_list:
        #     x, y, width, height = block_rect
        #     block = Brick(x, y, width, height, (182, 54, 36))  # Рожевий колір
        #     block_sprites.add(block)
        #
        # block_sprites.draw(screen)


        # Створюємо екземпляр класу Brick
        brick = Brick(0, 0, screen, (245, 109, 82))

        # Генеруємо список блоків
        block_list = brick.generate_block_list()


        # Створення групи спрайтів для блоків
        block_sprites = pygame.sprite.Group()
        block_sprites.add(*block_list)



        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_LSHIFT or
                            event.key == pygame.K_RSHIFT):
                        ball.start_move()

            paddle.move()

            ball.move()
            ball.collision()
            screen.blit(background_image, (0, 0))
            block_sprites.draw(screen)
            paddle.draw()
            ball.draw_ball()
            pygame.display.flip()
            clock.tick(60)


class Button:
    def __init__(self, screen, x, y, width, height, text, color, action=None):
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.action = action

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect, border_radius=30)
        font = pygame.font.SysFont(None, 32)
        text = font.render(self.text, True, (32, 33, 33))
        text_rect = text.get_rect(center=self.rect.center)
        self.screen.blit(text, text_rect)

    def is_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        clicked = self.rect.collidepoint(mouse_pos)
        if clicked:
            self.color = (156, 246, 231)
        return clicked


class Game:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Game")

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if difficult1_button.is_clicked():
                        game_window = GameWindow(difficulty=1)

                    elif difficult2_button.is_clicked():
                        game_window = GameWindow(difficulty=2)

                    elif difficult3_button.is_clicked():
                        game_window = GameWindow(difficulty=3)

                    if start_button.is_clicked():
                        game_window.run()
                    # перехід у вікно гри
                    # if start_button.is_clicked():
                    #     game_window.run()
                    # перехід у вікно результатів
                    elif results_button.is_clicked():
                        ...  # results_window.run()
                    # перехід у вікно старт з вікна кінець
                    # elif end_button.is_clicked():
                    #     start_window.run()

            self.screen.fill((26, 45, 115))
            background_image_start = pygame.image.load('../image/ARKANOID.png')
            resized_image = pygame.transform.scale(background_image_start , (700, 200))
            game.screen.blit(resized_image , (55, 0))
            start_button.draw()
            results_button.draw()
            difficult1_button.draw()
            difficult2_button.draw()
            difficult3_button.draw()
            pygame.display.flip()

        # При виході з циклу гри виходимо з програми
        pygame.quit()


class StartWindow:
    def run(self):
        start_button.rect.topleft = (300, 200)
        results_button.rect.topleft = (300, 300)
        #game.screen.fill((26, 45, 115))
        start_button.draw()
        results_button.draw()
        difficult1_button.draw()
        difficult2_button.draw()
        difficult3_button.draw()
        pygame.display.flip()


pygame.init()
game = Game()
start_button = Button(game.screen, 300, 200, 200, 50, "Start", (240, 133, 245))
results_button = Button(game.screen, 295, 300, 210, 50, "History of results", (240, 133, 245))

difficult1_button = Button(game.screen, 160, 400, 140, 50, "Easy", (46, 224, 155))
difficult2_button = Button(game.screen, 330, 400, 140, 50, "Medium", (46, 224, 155))
difficult3_button = Button(game.screen, 500, 400, 140, 50, "Hard", (46, 224, 155))

start_window = StartWindow()

# results_window = ResultsWindow()
# end_window = EndWindow()

game.run()

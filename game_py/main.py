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

        paddle = Paddle(screen)
        ball = Ball(screen, paddle, self.difficulty)
        # Створення списку блоків
        block_list = [pygame.Rect(20 + 110 * i, 20 + 50 * j, 100, 40) for i in range(7) for j in range(4)]

        # Створення групи спрайтів для блоків
        block_sprites = pygame.sprite.Group()
        for block_rect in block_list:
            x, y, width, height = block_rect
            block = Brick(x, y, width, height, (182, 54, 36))  # Рожевий колір
            block_sprites.add(block)

        block_sprites.draw(screen)
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
            self.color = (245, 255, 230)
        return clicked


class Game:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Game")

    def run(self):
        running = True
        game_window = None
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

                    # перехід у вікно гри
                    if start_button.is_clicked():
                        if game_window is not None:
                            game_window.run()

                    # перехід у вікно історії результатів
                    elif history_results_button.is_clicked():
                        history_results_window.run()

            self.screen.fill((26, 45, 115))
            background_image_start = pygame.image.load('../image/ARKANOID.png')
            resized_image = pygame.transform.scale(background_image_start, (700, 200))
            game.screen.blit(resized_image, (55, 0))
            start_button.draw()
            history_results_button.draw()
            difficult1_button.draw()
            difficult2_button.draw()
            difficult3_button.draw()
            pygame.display.flip()

        # При виході з циклу гри виходимо з програми
        pygame.quit()


class HistoryResultsWindow:
    def __init__(self):
        self.results = []

    def run(self):
        screen_history = pygame.display.set_mode((800, 600))

        pygame.display.set_caption("History of results")
        result_label_font = pygame.font.SysFont(None, 24)
        screen_history.fill((162, 255, 240))

        clock = pygame.time.Clock()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if back_menu_button.is_clicked():
                        running = False

            screen_history.fill((162, 255, 240))
            self.display_results(screen_history, result_label_font)
            back_menu_button.draw()
            pygame.display.flip()
            clock.tick(60)

    def add_result(self, time_spent, blocks_broken):
        self.results.append((time_spent, blocks_broken))
        return self.results

    def display_results(self, screen_history, result_label_font):
        label_surface = result_label_font.render("Results:", True, (255, 255, 255))
        screen_history.blit(label_surface, (10, 10))

        for i, result in enumerate(self.results):
            result_text = f"Result #{i + 1}: Time Spent: {result[0]}, Blocks Broken: {result[1]}"
            result_surface = result_label_font.render(result_text, True, (255, 255, 255))
            screen_history.blit(result_surface, (10, 40 + i * 20))


# class StartWindow:
#     def run(self):
#         start_button.rect.topleft = (300, 200)
#         history_results_button.rect.topleft = (300, 300)
#         #game.screen.fill((26, 45, 115))
#         start_button.draw()
#         history_results_button.draw()
#         difficult1_button.draw()
#         difficult2_button.draw()
#         difficult3_button.draw()
#         pygame.display.flip()


pygame.init()
game = Game()
start_button = Button(game.screen, 300, 200, 200, 50, "Start", (240, 133, 245))
history_results_button = Button(game.screen, 295, 300, 210, 50, "History of results", (240, 133, 245))

difficult1_button = Button(game.screen, 160, 400, 140, 50, "Easy", (46, 224, 155))
difficult2_button = Button(game.screen, 330, 400, 140, 50, "Medium", (46, 224, 155))
difficult3_button = Button(game.screen, 500, 400, 140, 50, "Hard", (46, 224, 155))

back_menu_button = Button(game.screen, 5, 5, 140, 50, "Menu", (240, 133, 245))

history_results_window = HistoryResultsWindow()

# start_window = StartWindow()
# end_window = EndWindow()

game.run()

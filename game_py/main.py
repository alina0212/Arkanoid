import sys
import pygame

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
    def run(self):
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Arkanoid")
        background_image = pygame.image.load('../image/backgroung2.png')

        paddle = Paddle(screen)
        ball = Ball(screen, paddle)

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
        pygame.draw.rect(self.screen, self.color, self.rect, border_radius=10)
        font = pygame.font.SysFont(None, 36)
        text = font.render(self.text, True, (0, 0, 0))
        text_rect = text.get_rect(center=self.rect.center)
        self.screen.blit(text, text_rect)

    def is_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_pos)



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
                    # перехід у вікно гри
                    if start_button.is_clicked():
                        game_window.run()
                    # перехід у вікно результатів
                    elif results_button.is_clicked():
                        ... # results_window.run()
                    # перехід у вікно старт з вікна кінець
                    # elif end_button.is_clicked():
                    #     start_window.run()

            self.screen.fill((255, 255, 255))
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
        game.screen.fill((255, 255, 255))
        start_button.draw()
        results_button.draw()
        pygame.display.flip()

pygame.init()
game = Game()
start_button = Button(game.screen, 300, 200, 200, 50, "Start", (0, 255, 0))
results_button = Button(game.screen, 300, 300, 200, 50, "Results", (0, 255, 0))


difficult1_button = Button(game.screen,160, 400, 140, 50, "Easy", (0, 255, 0))
difficult2_button = Button(game.screen,330, 400, 140, 50, "Medium", (0, 255, 0))
difficult3_button = Button(game.screen,500, 400, 140, 50, "Hard", (0, 255, 0))


start_window = StartWindow()
game_window = GameWindow()
# results_window = ResultsWindow()
# end_window = EndWindow()

game.run()






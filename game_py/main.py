import sys
import pygame
from paddle import Paddle
from ball import Ball


def run():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Arkanoid")
    background_image = pygame.image.load('../image/backgroung2.png')

    paddle = Paddle(screen)
    ball = Ball(screen, paddle)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
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

run()

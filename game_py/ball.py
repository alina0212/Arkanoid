import pygame
from random import randrange as rnd


class Ball:
    def __init__(self, screen, paddle):
        self.screen = screen
        self.paddle = paddle
        self.speed = None
        self.ball_radius = 10
        self.speed_1 = 6
        self.speed_2 = 10
        self.speed_3 = 14
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.dx = 0
        self.dy = 0
        self.speed = self.receive_speed()
        self.color_name = "white"
        self.ball_rect = self.initial_position()

    def start_move(self):
        if self.dx == 0 and self.dy == 0:
            self.dx = 1
            self.dy = -1
            self.speed = self.receive_speed()

    def size(self, radius):
        if radius > 0:
            self.ball_radius = radius
            return True
        else:
            return False

    def color(self):
        try:
            color = pygame.Color(self.color_name)
        except ValueError:
            color = pygame.Color('white')  # Повернемо білий колір за замовчуванням, якщо переданий недійсний колір
        return color

    def draw_ball(self):
        pygame.draw.circle(self.screen, self.color(), self.ball_rect.center, self.ball_radius)

    def put_speed(self, new_speed):
        if new_speed in (self.speed_1):
            self.speed = new_speed
            return True
        else:
            return False

    def receive_speed(self):
        return self.speed_1

    def collision(self):
        # колізія з правою, лівою межею
        if self.ball_rect.centerx < self.ball_radius or self.ball_rect.centerx > self.width - self.ball_radius:
            self.dx = -self.dx

        # колізія з верхнею межею
        if self.ball_rect.centery < self.ball_radius:
            self.dy = -self.dy

        # колізія з веслом
        if self.ball_rect.colliderect(self.paddle.rect) and self.dy > 0:
            self.dy = -self.dy

    def check_collision_brick(self):
        pass

    def move(self):
        self.ball_rect.x += self.speed * self.dx
        self.ball_rect.y += self.speed * self.dy

    def initial_position(self):
        ball_r = int(self.ball_radius * 2 ** 0.5)
        ball_rect = pygame.Rect(self.paddle.rect.centerx - self.ball_radius, self.paddle.rect.top - ball_r, ball_r, ball_r)
        return ball_rect

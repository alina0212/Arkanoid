import pygame
import pygame.sprite
import random


class Ball:
    """
    клас, що відповідає за відображення та дії м'яча
    """
    def __init__(self, screen, paddle, brick_sprites, difficulty):
        self.screen = screen
        self.paddle = paddle
        self.brick_sprites = brick_sprites  # Група блоків
        self.difficulty = difficulty
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
        self.color = "black"
        self.ball_rect = self.initial_position()
        self.rect = pygame.Rect(self.ball_rect) # Створення прямокутника, що обмежує м'яч
        self.blocks_hit = 0  # Додано для відстеження кількості блоків, які гравець вдарив

    def draw_ball(self):
        """
        малюємо м'яч
        :return: True
        """
        pygame.draw.circle(self.screen, self.color, self.ball_rect.center, self.ball_radius)
        return True

    def initial_position(self):
        """
        встановлюємо початкову позицію м'яча
        створюємо прямокутник для розташування м'яча
        :return: розташування м'яча
        """
        ball_r = int(self.ball_radius * 2 ** 0.5)  # визначаємо м'яч, як квадрат

        # встановлюємо (посередині плаформи, відстань між платф. і м'ячем - діаметр м'яча, ширина, висота)
        ball_rect = pygame.Rect(self.paddle.rect.centerx - self.ball_radius, self.paddle.rect.top - ball_r, ball_r,
                                ball_r)

        return ball_rect

    def start_move(self):
        """
        початковий рух м'яча
        :return: x, y, швидкість
        """
        if self.dx == 0 and self.dy == 0:
            # Генеруємо випадковий напрямок руху
            self.dx = random.choice([-1, 0, 1])
            self.dy = random.choice([-1, 1])
            self.speed = self.receive_speed()
            return self.dx, self.dy, self.speed

    def move(self):
        """
        рух м'яча
        :return: координати x, y
        """
        # оновлюються координати м'яча
        self.ball_rect.x += self.speed * self.dx
        self.ball_rect.y += self.speed * self.dy

        # координати верхнього лівого кута прямокутника, що обмежує м'яч
        # використовуємо для колізії з блоками
        self.rect.x = self.ball_rect.x
        self.rect.y = self.ball_rect.y
        return self.ball_rect.x, self.ball_rect.y

    def receive_speed(self):
        """
        обираємо швидкість м'яча
        :return: швидкість
        """
        if self.difficulty == 1:
            return self.speed_1
        elif self.difficulty == 2:
            return self.speed_2
        elif self.difficulty == 3:
            return self.speed_3

    def collision(self):
        """
        обробляємо колізії
        """
        # колізія з правою, лівою межею
        if self.ball_rect.centerx < self.ball_radius or self.ball_rect.centerx > self.width - self.ball_radius:
            self.dx = -self.dx

        # колізія з верхнею межею
        if self.ball_rect.centery < self.ball_radius:
            self.dy = -self.dy
            if self.dx == 0:
                self.dx = random.choice([-1, 1]) if self.dx > 0 else random.choice([-1, 1])

        # колізія з веслом
        if self.ball_rect.colliderect(self.paddle.rect) and self.dy > 0:
            self.dy = -self.dy

    def check_collision_brick(self):
        """
        перевіряємо колізію з блоками
        """
        hits = pygame.sprite.spritecollide(self, self.brick_sprites, True)
        for hit in hits:
            self.blocks_hit += 1  # Додано для відстеження кількості блоків, які гравець вдарив
            if self.dx > 0:  # якщо м'яч рухався вправо, змінюємо напрямок наліво
                self.dx = -self.dx
            elif self.dx < 0:  # якщо м'яч рухався вліво, змінюємо напрямок направо
                self.dx = -self.dx

            if self.dy > 0:  # якщо м'яч рухався вниз, змінюємо напрямок вгору
                self.dy = -self.dy
            elif self.dy < 0:  # якщо м'яч рухався вгору, змінюємо напрямок вниз
                self.dy = -self.dy

            # видаляємо блок із групи
            self.brick_sprites.remove(hit)

    def all_bricks_broken(self):
        """
        перевіряємо, чи всі блоки розбиті
        :return: True
        """
        return len(self.brick_sprites) == 0

    def check_collision_bottom(self):
        """
        перевіряємо, чи доторкнувся м'яч нижньої межі
        :return: доторкнувся / не доторкнувся
        """
        if self.ball_rect.bottom >= self.height:
            return True
        return False



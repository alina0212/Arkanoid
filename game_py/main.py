import pygame
import time
import os
import csv

from brick import BrickContainer
from paddle import Paddle
from ball import Ball


class GameWindow:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def run(self):
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Arkanoid")
        image_path = os.path.join("../image", "backgroung2.png")
        background_image = pygame.image.load(image_path)
        # background_image = pygame.image.load('../image/backgroung2.png')

        brick_container = BrickContainer(screen)
        block_list = brick_container.generate_block_list((153, 99, 241))
        block_sprites = pygame.sprite.Group(block_list)
        paddle = Paddle(screen)
        ball = Ball(screen, paddle, block_sprites, self.difficulty)

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
            ball.check_collision_brick()

            # м'яч доторкнувся нижньої межі екрану або розбиті всі блоки, гра завершена
            if ball.check_collision_bottom() or ball.all_bricks_broken():
                # Передаємо кількість вдарених блоків у вікно результатів гри
                result_window.run(ball.blocks_hit, self.difficulty)
                return

            screen.blit(background_image, (0, 0))
            block_sprites.draw(screen)
            paddle.draw()
            ball.draw_ball()
            pygame.display.flip()
            clock.tick(60)


class ResultWindow:
    def __init__(self):
        self.csv_filename = 'game_history.csv'
        self.background_image = None
        self.time_spent = None  # time_spent
        self.blocks_hit = None  # blocks_broken
        self.font = pygame.font.SysFont(None, 50)
        self.screen_result = pygame.display.set_mode((800, 600))
        self.width = self.screen_result.get_width()
        self.height = self.screen_result.get_height()
        self.game_over_text = self.font.render("Game Over", True, (0, 0, 0))
        self.time_text = None
        self.blocks_text = None
        self.you_win_background_image_path = os.path.join("../image", "you_win_background.jpg")

    def save_to_csv(self, blocks_hit, difficulty_level):  # Add difficulty_level as a parameter
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        time_spent = round(time.time() - game.start_time, 2)
        # Відкриваємо файл CSV у режимі додавання з новим рядком
        with open(self.csv_filename, mode='a', newline='') as file:
            # Створюємо об'єкт для запису в файл CSV
            writer = csv.writer(file)
            # Записуємо новий рядок в файл, який містить інформацію про результати гри
            writer.writerow([timestamp, difficulty_level, time_spent, blocks_hit])

    def run(self, blocks_hit, difficulty):
        # os.truncate('game_history.csv', 0) #очищення файлу
        pygame.display.set_caption("Result")
        self.screen_result.fill((162, 255, 240))

        # Перевіряємо, чи всі блоки розбиті
        if blocks_hit == 0:
            # Якщо так, встановлюємо фон на певне зображення
            you_win_background_image_path = os.path.join("../image", "you_win_background.jpg")
            self.background_image = pygame.image.load(you_win_background_image_path)
            self.screen_result.blit(self.background_image, (0, 0))
        else:
            # Якщо ні, залишаємо фон як заданий
            you_lost_background_image_path = os.path.join("../image", "you_lost_background.jpg")
            self.background_image = pygame.image.load(you_lost_background_image_path)
            self.screen_result.blit(self.background_image, (0, 0))

        # Розміщуємо фонове зображення на екрані
        self.time_spent = round(time.time() - game.start_time, 2)  # Обчислюємо час гри
        self.time_text = self.font.render("Time Spent: " + str(round(self.time_spent, 2)), True, (0, 0, 0))
        self.blocks_text = self.font.render("Blocks Broken: " + str(blocks_hit), True, (0, 0, 0))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if back_menu_button.is_clicked():
                        running = False

            self.screen_result.blit(self.game_over_text, (self.width // 2 - self.game_over_text.get_width() // 2, 200))
            self.screen_result.blit(self.time_text, (self.width // 2 - self.time_text.get_width() // 2, 300))
            self.screen_result.blit(self.blocks_text, (self.width // 2 - self.blocks_text.get_width() // 2, 400))

            back_menu_button.draw()
            pygame.display.flip()
        self.save_to_csv(blocks_hit, difficulty)


class HistoryResultsWindow:
    def __init__(self, csv_filename='game_history.csv'):
        self.results = []
        self.csv_filename = csv_filename
        # csv_path = os.path.join("../game_py", "game_history.csv")
        self.load_results_from_csv()

    def load_results_from_csv(self):
        try:
            with open(self.csv_filename, mode='r', newline='') as file:  # r  бо режим read
                reader = csv.reader(file)
                header = next(reader, None)  # Отримуємо заголовок
                if header is not None:  # Перевіряємо чи є рядок
                    for row in reader:
                        self.results.append(
                            row)  # файл CSV читається рядок за рядком, кожен рядок стає окремим елементом у списку self.results.
        except FileNotFoundError as e:
            print(f"Помилка: Файл CSV не знайдено. Деталі: {e}")

    def run(self):
        pygame.display.set_caption("History of results")
        screen_history = pygame.display.set_mode((800, 600))
        screen_history.fill((162, 255, 240))
        result_label_font = pygame.font.SysFont(None, 32)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if back_menu_button.is_clicked():
                        running = False

            self.display_results(screen_history, result_label_font)
            back_menu_button.draw()
            pygame.display.flip()

    # відображаємо результати
    def display_results(self, screen_history, result_label_font):
        label_surface = result_label_font.render("Results:", True, (70, 69, 69))
        screen_history.blit(label_surface, (20, 70))

        for i, result in enumerate(self.results):
            result_text = f"Result #{i + 1}: Time Spent: {result[2]}, Blocks Broken: {result[3]}, Difficulty: {result[1]}"  # Формуємо текст результату
            result_surface = result_label_font.render(result_text, True,
                                                      (70, 69, 69))  # Створюємо поверхню з текстом результату
            screen_history.blit(result_surface, (30, 100 + i * 40))  # Відображаємо текст результату на вікні


class Button:
    def __init__(self, screen, x, y, width, height, text, color):
        self.default_color = color
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.last_click_time = 0
        self.click_duration = 0.2

    # малюємо кнопку
    def draw(self):
        self.update()
        pygame.draw.rect(self.screen, self.color, self.rect, border_radius=30)
        font = pygame.font.SysFont(None, 32)
        text = font.render(self.text, True, (32, 33, 33))
        text_rect = text.get_rect(center=self.rect.center)
        self.screen.blit(text, text_rect)

    # оновлює колір кнопки
    def update(self):
        if time.time() - self.last_click_time < self.click_duration:
            self.color = (245, 255, 230)
        else:
            self.color = self.default_color

    # перевіряємо, чи мишка натиснула і якщо так, то оновлюємо час кліку
    def is_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        clicked = self.rect.collidepoint(mouse_pos)
        if clicked:
            self.last_click_time = time.time()
        return clicked


class Game:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Game")
        self.start_time = 0  # Додайте змінну для часу початку гри
        background_image2_start = pygame.image.load(os.path.join("../image", "start_windon_background.jpg"))
        background_image_start = pygame.image.load(os.path.join("../image", "ARKANOID.png"))
        self.resized_image = pygame.transform.scale(background_image_start, (700, 200))
        self.resized_image2 = pygame.transform.scale(background_image2_start, (800, 600))

    def run(self):
        clock = pygame.time.Clock()
        running = True
        game_window = None
        while running:
            game.screen.blit(self.resized_image2, (0, 0))
            game.screen.blit(self.resized_image, (55, 0))

            start_button.draw()
            history_results_button.draw()
            difficult1_button.draw()
            difficult2_button.draw()
            difficult3_button.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # обираємо складність
                    if difficult1_button.is_clicked():
                        game_window = GameWindow(difficulty=1)

                    elif difficult2_button.is_clicked():
                        game_window = GameWindow(difficulty=2)

                    elif difficult3_button.is_clicked():
                        game_window = GameWindow(difficulty=3)

                    # перехід у вікно гри
                    if start_button.is_clicked():
                        self.start_time = time.time()  # Запам'ятовуємо час початку гри
                        if game_window is not None:
                            game_window.run()

                    # перехід у вікно історії результатів
                    if history_results_button.is_clicked():
                        history_results_window.run()

            pygame.display.flip()
            clock.tick(60)


pygame.init()
game = Game()
start_button = Button(game.screen, 300, 200, 200, 50, "Start", (240, 133, 245))
history_results_button = Button(game.screen, 295, 300, 210, 50, "History of results", (240, 133, 245))

difficult1_button = Button(game.screen, 160, 400, 140, 50, "Easy", (46, 224, 155))
difficult2_button = Button(game.screen, 330, 400, 140, 50, "Medium", (46, 224, 155))
difficult3_button = Button(game.screen, 500, 400, 140, 50, "Hard", (46, 224, 155))

back_menu_button = Button(game.screen, 10, 10, 140, 50, "Menu", (240, 133, 245))

history_results_window = HistoryResultsWindow()

result_window = ResultWindow()

game.run()

pygame.quit()

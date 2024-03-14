import pygame
import time
import os
import csv

from brick import BrickContainer
from paddle import Paddle
from ball import Ball


class GameWindow:
    """
    responsible for displaying the window where the game takes place
    """

    def __init__(self, difficulty):
        self.difficulty = difficulty

    def run(self):
        """
        method to launch the game
        """
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Arkanoid")
        image_path = os.path.join("../image", "backgroung2.png")
        background_image = pygame.image.load(image_path)

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

            # the ball touches the bottom of the screen or all blocks are broken, the game is over
            if ball.check_collision_bottom() or ball.all_bricks_broken():
                # return the number of blocks hit to the game results window
                result_window.run(ball.blocks_hit, self.difficulty, ball)
                return

            screen.blit(background_image, (0, 0))
            block_sprites.draw(screen)
            paddle.draw()
            ball.draw_ball()
            pygame.display.flip()
            clock.tick(60)


class ResultWindow:
    """
    responsible for displaying the game result window
    """

    def __init__(self):

        self.csv_filename = 'game_history.csv'
        self.background_image = None
        self.time_spent = None
        self.blocks_hit = None
        self.font = pygame.font.SysFont(None, 50)
        self.screen_result = pygame.display.set_mode((800, 600))
        self.width = self.screen_result.get_width()
        self.height = self.screen_result.get_height()
        self.game_over_text = self.font.render("Game Over", True, (0, 0, 0))
        self.time_text = None
        self.blocks_text = None

    """
    method - saving data (date, time, difficulty, number of blocks broken) to a csv file 
    """

    def save_to_csv(self, blocks_hit, difficulty_level, time_spent):
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        # open a CSV file in add mode with a new line
        with open(self.csv_filename, mode='a', newline='') as file:
            # create an object to write to a CSV file
            writer = csv.writer(file)
            # write a new line to the file containing information about the game results
            writer.writerow([timestamp, difficulty_level, time_spent, blocks_hit])

    """
    method for launching the result window after the end of the game
    """

    def run(self, blocks_hit, difficulty, ball):
        pygame.display.set_caption("Result")
        self.screen_result.fill((162, 255, 240))

        # check if all blocks are broken
        if ball.all_bricks_broken():
            # if so, set the background to the winning image
            you_win_background_image_path = os.path.join("../image", "you_win_background.jpg")
            self.background_image = pygame.image.load(you_win_background_image_path)
            self.screen_result.blit(self.background_image, (0, 0))
        else:
            # if not, the background as a loss
            you_lost_background_image_path = os.path.join("../image", "you_lost_background.jpg")
            self.background_image = pygame.image.load(you_lost_background_image_path)
            self.screen_result.blit(self.background_image, (0, 0))

        # place the background image on the screen
        self.time_spent = round(time.time() - game.start_time, 2)  # calculate the game time
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
        self.save_to_csv(blocks_hit, difficulty, self.time_spent)


class HistoryResultsWindow:
    """
    responsible for displaying the game results history window
    """

    def __init__(self, csv_filename='game_history.csv'):
        self.results = []
        self.csv_filename = csv_filename
        self.load_results_from_csv()
        self.screen_history = pygame.display.set_mode((800, 600))
        self.window_height = self.screen_history.get_height()
        self.container_height = len(self.results) * 40  # calculates the height of the container to display
        # the results in the game history window
        self.scroll_pos = 0

    """
    метод що чатає файл з результатими і записує їх у список
    """

    def load_results_from_csv(self):
        try:
            with open(self.csv_filename, mode='r', newline='') as file:  # r  because mode read
                reader = csv.reader(file)
                header = next(reader, None)  # get the header
                if header is not None:  # check if there is a string
                    for row in reversed(list(reader)):
                        # the CSV file is read line by line, each line becomes a separate item in the self.results list
                        self.results.append(row)
        except FileNotFoundError as e:
            print(f"Error: CSV file not found. Details: {e}")

    """
    method to update the results with the last game
    """

    def update_results(self):
        self.results = []
        self.load_results_from_csv()

    def run(self):
        """
        method for displaying the game results history window
        """
        pygame.display.set_caption("History of results")
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if back_menu_button.is_clicked():
                        running = False
                    elif event.button == 4:  # scroll up
                        self.scroll_pos = max(0, self.scroll_pos - 20)
                    elif event.button == 5:  # scroll down
                        self.scroll_pos = min(max(0, self.container_height - self.window_height), self.scroll_pos + 20)

            self.screen_history.fill((162, 255, 240))
            self.update_results()
            self.display_results(self.screen_history)
            back_menu_button.draw()
            pygame.display.flip()

    def display_results(self, screen_history):
        """
        display the results
        :param screen_history:
        """
        result_label_font = pygame.font.SysFont(None, 32)
        label_surface = result_label_font.render("Results:", True, (70, 69, 69))
        screen_history.blit(label_surface, (20, 70 - self.scroll_pos))

        for i, result in enumerate(self.results):
            # create the text of the result
            result_text = f"Result #{len(self.results) - i}: Time Spent: {result[2]}, Blocks Broken: {result[3]}, Difficulty: {result[1]}"
            result_surface = result_label_font.render(result_text, True,
                                                      (70, 69, 69))  # create a surface with the result text
            text_height = result_surface.get_height()
            if 100 + i * 40 - self.scroll_pos + text_height > 70:  # check for intersection with a button
                if 100 + i * 40 - self.scroll_pos < self.window_height:
                    screen_history.blit(result_surface,
                                        (30, 100 + i * 40 - self.scroll_pos))  # display the result text on the window


class Button:
    """
    responsible for creating buttons
    """

    def __init__(self, screen, x, y, width, height, text, color):
        self.default_color = color
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.last_click_time = 0
        self.click_duration = 0.2

    def draw(self):
        """
        draw a button
        """
        self.update()
        pygame.draw.rect(self.screen, self.color, self.rect, border_radius=30)
        font = pygame.font.SysFont(None, 32)
        text = font.render(self.text, True, (32, 33, 33))
        text_rect = text.get_rect(center=self.rect.center)
        self.screen.blit(text, text_rect)

    def update(self):
        """
        updates the color of the button_
        :return: button_ color
        """
        if time.time() - self.last_click_time < self.click_duration:
            self.color = (245, 255, 230)
        else:
            self.color = self.default_color

    def is_clicked(self):
        """
        check if the mouse was clicked and if so, update the click time
        :return: clicked
        """
        mouse_pos = pygame.mouse.get_pos()
        clicked = self.rect.collidepoint(mouse_pos)
        if clicked:
            self.last_click_time = time.time()
        return clicked


class Game:
    """
    responsible for menu navigation
    """

    def __init__(self):
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.start_time = 0  # add a variable for the game start time
        background_image2_start = pygame.image.load(os.path.join("../image", "start_windon_background.jpg"))
        background_image_start = pygame.image.load(os.path.join("../image", "ARKANOID.png"))
        self.resized_image = pygame.transform.scale(background_image_start, (700, 200))
        self.resized_image2 = pygame.transform.scale(background_image2_start, (800, 600))

    def run(self):
        """
        method to run the game
        """
        clock = pygame.time.Clock()
        running = True
        game_window = None
        while running:
            game.screen.blit(self.resized_image2, (0, 0))
            game.screen.blit(self.resized_image, (55, 0))
            pygame.display.set_caption("Game")
            start_button.draw()
            history_results_button.draw()
            difficult1_button.draw()
            difficult2_button.draw()
            difficult3_button.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # choose the difficulty
                    if difficult1_button.is_clicked():
                        game_window = GameWindow(difficulty=1)

                    elif difficult2_button.is_clicked():
                        game_window = GameWindow(difficulty=2)

                    elif difficult3_button.is_clicked():
                        game_window = GameWindow(difficulty=3)

                    # switch to the game window
                    if start_button.is_clicked():
                        self.start_time = time.time()  # memorize the game start time
                        if game_window is not None:
                            game_window.run()

                    # switch to the results history window
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

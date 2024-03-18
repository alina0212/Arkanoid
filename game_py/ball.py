import pygame
import pygame.sprite
import random
from constants import ball_radius, speed_1, speed_2, speed_3, color


class Ball:
    """
    class responsible for the reflection and action of the ball
    """

    def __init__(self, screen, paddle, brick_sprites, difficulty):
        self.screen = screen
        self.paddle = paddle
        self.brick_sprites = brick_sprites  # block group
        self.difficulty = difficulty
        self.speed = None
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.dx = 0
        self.dy = 0
        self.speed = self.receive_speed()
        self.ball_rect = self.initial_position()
        self.rect = pygame.Rect(self.ball_rect)  # create a rectangle that bounds the ball
        self.blocks_hit = 0  # added to track the number of blocks a player has hit

    def draw_ball(self):
        """
        draw a ball
        :return: True
        """
        pygame.draw.circle(self.screen, color, self.ball_rect.center, ball_radius)
        return True

    def initial_position(self):
        """
        set the starting position of the ball
        create a rectangle for the location of the ball
        :return: location of the ball
        """
        ball_r = int(ball_radius * 2 ** 0.5)  # define the ball as a square

        # set (in the middle of the plate, the distance between the plate and ball - ball diameter, width, height)
        ball_rect = pygame.Rect(self.paddle.rect.centerx - ball_radius, self.paddle.rect.top - ball_r, ball_r,
                                ball_r)

        return ball_rect

    def start_move(self):
        """
        initial ball movement
        :return: x, y, speed
        """
        if self.dx == 0 and self.dy == 0:
            # generate a random direction of movement
            self.dx = random.choice([-1, 0, 1])
            self.dy = random.choice([-1, 1])
            self.speed = self.receive_speed()
            return self.dx, self.dy, self.speed

    def move(self):
        """
        ball movement
        :return: coordinates x, y
        """
        # updated ball coordinates
        self.ball_rect.x += self.speed * self.dx
        self.ball_rect.y += self.speed * self.dy

        # coordinates of the upper left corner of the rectangle bounding the ball
        # use for collision with blocks
        self.rect.x = self.ball_rect.x
        self.rect.y = self.ball_rect.y
        return self.ball_rect.x, self.ball_rect.y

    def receive_speed(self):
        """
        choose the speed of the ball
        :return: speed
        """
        if self.difficulty == 1:
            return speed_1
        elif self.difficulty == 2:
            return speed_2
        elif self.difficulty == 3:
            return speed_3

    def collision(self):
        """
        handle collisions
        """
        # collision with the right, left border
        if self.ball_rect.centerx < ball_radius or self.ball_rect.centerx > self.width - ball_radius:
            self.dx = -self.dx

        # collision with the upper boundary
        if self.ball_rect.centery < ball_radius:
            self.dy = -self.dy
            if self.dx == 0:
                self.dx = random.choice([-1, 1]) if self.dx > 0 else random.choice([-1, 1])

        # collision with a paddle
        if self.ball_rect.colliderect(self.paddle.rect) and self.dy > 0:
            self.dy = -self.dy

    def check_collision_brick(self):
        """
        check for collisions with blocks
        """
        hits = pygame.sprite.spritecollide(self, self.brick_sprites, True)
        for hit in hits:
            self.blocks_hit += 1  # added to track the number of blocks a player has hit
            if self.dx > 0:  # if the ball was moving to the right, change the direction to the left
                self.dx = -self.dx
            elif self.dx < 0:  # if the ball was moving to the left, change the direction to the right
                self.dx = -self.dx

            if self.dy > 0:  # if the ball was moving down, change the direction up
                self.dy = -self.dy
            elif self.dy < 0:  # if the ball was moving up, change the direction down
                self.dy = -self.dy

            # remove the block from the group
            self.brick_sprites.remove(hit)

    def all_bricks_broken(self):
        """
        check if all blocks are broken
        :return: True
        """
        return len(self.brick_sprites) == 0

    def check_collision_bottom(self):
        """
        check whether the ball has touched the bottom line
        :return: touched / not touched
        """
        if self.ball_rect.bottom >= self.height:
            return True
        return False

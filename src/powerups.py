from random import randint
import pygame
from abc import ABC, abstractmethod
from .constants import *

BLACK = (0, 0, 0)


class PowerUp(pygame.sprite.Sprite, ABC):  # sprite-Simple base class for visible game objects

    # Set the PowerUp visible time in seconds
    visible_time: int = GameSettings.POWERUP_VISIBLE_TIME

    def __init__(self, ball_owner, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        # Set PowerUp width and height
        self.width = width
        self.height = height
        self.owner = ball_owner

    @abstractmethod
    def affect_playerA(self, player_A):
        pass

    @abstractmethod
    def affect_playerB(self, player_B):
        pass

    @abstractmethod
    def run_powerup(self, paddleA, paddleB, ball):
        pass

    def draw(self, filename, ):
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        pygame.draw.rect(self.image, BLACK, [self.width, self.height, 0, 0])
        self.rect = self.image.get_rect()
        self.rect.y = randint(GameSettings.POWERUP_HEIGHT, GameSettings.POWERUP_FIELD_HEIGHT)
        self.rect.x = randint(GameSettings.POWERUP_WIDTH, GameSettings.POWERUP_FIELD_WIDTH)

    # TODO: Set timer for the powerups


# Mandatory PowerUps

# AntMan: The AntMan "Power-up" makes the player’s Paddle bigger
class ShrinkEnlarge(PowerUp):
    # Set the PowerUp probability
    probability: int = 50

    def __init__(self, ball_owner, width, height):
        super().__init__(ball_owner, width, height)

        # Set the PowerUp image
        super().draw('img/PowerUp_0.png')

    def affect_playerA(self, player_A):
        player_A.image = pygame.transform.scale(player_A.image, (player_A.rect.width * 1.5, player_A.rect.height * 2))
        player_A.height = player_A.image

    def affect_playerB(self, player_B):
        player_B.image = pygame.transform.scale(player_B.image, (player_B.rect.width * 1.5, player_B.rect.height * 2))
        player_B.height = player_B.image

    def run_powerup(self, paddleA, paddleB, ball):
        if self.owner == paddleA:
            self.affect_playerA(paddleA)
        elif self.owner == paddleB:
            self.affect_playerB(paddleB)
        else:
            pass


# Freeze: The Freeze "Power-up" freezes the position of the player’s paddle
class Freeze(PowerUp):
    # Set the PowerUp probability
    probability: int = 60

    def __init__(self, ball_owner, width, height):
        super().__init__(ball_owner, width, height)

        # Set the PowerUp image
        super().draw('img/PowerUp_1.png')

    def affect_playerA(self, player_A):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_A.moveUp(0)
        if keys[pygame.K_s]:
            player_A.moveDown(0, GameSettings.WINDOW_HEIGHT, PaddleSettings.PADDLE_HEIGHT)

    def affect_playerB(self, player_B):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player_B.moveUp(0)
        if keys[pygame.K_DOWN]:
            player_B.moveDown(0, GameSettings.WINDOW_HEIGHT, PaddleSettings.PADDLE_HEIGHT)

    def run_powerup(self, paddleA, paddleB, ball):
        self.affect_playerA(paddleA)
        self.affect_playerB(paddleB)


# MultipleBalls: The MultipleBalls "Power-up" creates a second ball that moves in the opposite direction
class MultipleBalls(PowerUp):
    # Set the PowerUp probability
    probability: int = 30

    def __init__(self, ball_owner, width, height):
        super().__init__(ball_owner, width, height)

        # Set the PowerUp image
        super().draw('img/PowerUp_2.png')

    def affect_playerA(self, player_A):
        pass

    def affect_playerB(self, player_B):
        pass

    def affect_ball(self):
        pass

    def run_powerup(self, paddleA, paddleB, ball):
        pass


# Optional PowerUps

# Quicksilver: The Quicksilver "Power-up" increases the speed of the player’s paddle
class FasterPaddle(PowerUp):
    # Set the PowerUp probability
    probability: int = 30

    def __init__(self, ball_owner, width, height):
        super().__init__(ball_owner, width, height)

        # Set the PowerUp image
        super().draw('img/PowerUp_3.png')

    def affect_playerA(self, player_A):
        pass

    def affect_playerB(self, player_B):
        pass

    def run_powerup(self, paddleA, paddleB, ball):
        pass


# DoubleScore: The DoubleScore "Power-up" doubles the score of the player that hits the ball
class DoubleScore(PowerUp):
    # Set the PowerUp probability
    probability: int = 70

    def __init__(self, ball_owner, width, height):
        super().__init__(ball_owner, width, height)

        # Set the PowerUp image
        super().draw('img/PowerUp_4.png')

    def affect_playerA(self, player_A):
        pass

    def affect_playerB(self, player_B):
        pass

    def run_powerup(self, paddleA, paddleB, ball):
        pass


# Shield: The Shield "Power-up" creates a shield that protects the player’s paddle from the ball
class Shield(PowerUp):
    # Set the PowerUp probability
    probability: int = 50

    def __init__(self, ball_owner, width, height):
        super().__init__(ball_owner, width, height)

        # Set the PowerUp image
        super().draw('img/PowerUp_5.png')

    def affect_playerA(self, player_A):
        pass

    def affect_playerB(self, player_B):
        pass

    def run_powerup(self, paddleA, paddleB, ball):
        pass


# Dictionary of PowerUps and their probabilities
PowerUps = {0: ShrinkEnlarge, 1: Freeze, 2: MultipleBalls, 3: FasterPaddle, 4: DoubleScore, 5: Shield}

# TODO: Implement the necessary visual modifications, so it is clear there is a "Power-up" in
#  play and who is benefiting or suffering from it and a text that says "Power-up" in the middle of the screen.

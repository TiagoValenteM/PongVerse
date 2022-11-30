from random import randint
import pygame
from abc import ABC, abstractmethod
from .constants import *

BLACK = (0, 0, 0)


class PowerUp(pygame.sprite.Sprite, ABC):  # sprite-Simple base class for visible game objects

    def __init__(self, ball_owner, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        # Set PowerUp width and height
        self.width = width
        self.height = height
        self.owner = ball_owner

    @abstractmethod
    def affect_playerA(self):
        pass

    @abstractmethod
    def affect_playerB(self):
        pass

    def draw(self, filename, ):
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        pygame.draw.rect(self.image, BLACK, [self.width, self.height, 0, 0])
        self.rect = self.image.get_rect()
        self.rect.y = randint(POWERUP_HEIGHT, POWERUP_FIELD_HEIGHT)
        self.rect.x = randint(POWERUP_WIDTH, POWERUP_FIELD_WIDTH)

    # TODO: Set timer for the powerups


# TODO: For the power ups, my idea is to set an interval of random numbers and set the powerups equal to some of
#  these???

# Mandatory PowerUps

class ShrinkEnlarge(PowerUp):
    # Set the PowerUp probability
    probability = 50

    # AntMan: The AntMan "Power-up" makes the player’s Paddle smaller while increasing others size
    def __init__(self, ball_owner, width, height):
        super().__init__(ball_owner, width, height)

        # Set the PowerUp image
        super().draw('img/ball_avengers.png')

    def affect_playerA(self):
        pass

    def affect_playerB(self):
        pass


class Freeze(PowerUp):
    # Set the PowerUp probability
    probability = 60

    # Freeze: The Freeze "Power-up" freezes the position of the player’s paddle
    def __init__(self, ball_owner, width, height):
        super().__init__(ball_owner, width, height)

        # Set the PowerUp image
        super().draw('img/ball_avengers.png')

    def affect_playerA(self):
        pass

    def affect_playerB(self):
        pass


class MultipleBalls(PowerUp):
    # Set the PowerUp probability
    probability = 30

    # MultipleBalls: The MultipleBalls "Power-up" creates a second ball that moves in the opposite direction
    def __init__(self, ball_owner, width, height):
        super().__init__(ball_owner, width, height)

        # Set the PowerUp image
        super().draw('img/ball_avengers.png')

    def affect_playerA(self):
        pass

    def affect_playerB(self):
        pass

    def affect_ball(self):
        pass


# Optional PowerUps

class FasterPaddle(PowerUp):
    # Set the PowerUp probability
    probability = 30

    # Quicksilver: The Quicksilver "Power-up" increases the speed of the player’s paddle
    def __init__(self, ball_owner, width, height):
        super().__init__(ball_owner, width, height)

        # Set the PowerUp image
        super().draw('img/ball_avengers.png')

    def affect_playerA(self):
        pass

    def affect_playerB(self):
        pass


class DoubleScore(PowerUp):
    # Set the PowerUp probability
    probability = 70

    # DoubleScore: The DoubleScore "Power-up" doubles the score of the player that hits the ball
    def __init__(self, ball_owner, width, height):
        super().__init__(ball_owner, width, height)

        # Set the PowerUp image
        super().draw('img/ball_avengers.png')

    def affect_playerA(self):
        pass

    def affect_playerB(self):
        pass


class Shield(PowerUp):
    # Set the PowerUp probability
    probability = 50

    # Shield: The Shield "Power-up" creates a shield that protects the player’s paddle from the ball
    def __init__(self, ball_owner, width, height):
        super().__init__(ball_owner, width, height)

        # Set the PowerUp image
        super().draw('img/ball_avengers.png')

    def affect_playerA(self):
        pass

    def affect_playerB(self):
        pass


# Dictionary of PowerUps and their probabilities
PowerUps = {0: ShrinkEnlarge, 1: Freeze, 2: MultipleBalls, 3: FasterPaddle, 4: DoubleScore, 5: Shield}

# TODO: Implement the necessary visual modifications, so it is clear there is a "Power-up" in
#  play and who is benefiting or suffering from it and a text that says "Power-up" in the middle of the screen.

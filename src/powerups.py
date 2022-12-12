from random import randint
from abc import ABC, abstractmethod
from .config import *


class PowerUp(pygame.sprite.Sprite, ABC):  # sprite-Simple base class for visible game objects

    # Set the PowerUp visible time in seconds
    visible_time: int = PowerUpSettings.POWERUP_VISIBLE_TIME

    def __init__(self, ball_owner, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        # Set PowerUp width and height
        self.width = width
        self.height = height
        # Set the ball owner to affect a certain player
        self.owner = ball_owner

    # Function that affects player A
    @abstractmethod
    def affect_playerA(self, player_A):
        pass

    # Function that affects player B
    @abstractmethod
    def affect_playerB(self, player_B):
        pass

    # Function that runs the powerup
    @abstractmethod
    def run_powerup(self, paddleA, paddleB):
        pass

    # Function that reverts the powerup
    @abstractmethod
    def revert_powerup(self, paddleA, paddleB):
        pass

    # Function that draws the powerup icon on the screen
    def draw(self, filename):
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        pygame.draw.rect(self.image, GameSettings.BLACK, [self.width, self.height, 0, 0])
        self.rect = self.image.get_rect()
        self.rect.y = randint(PowerUpSettings.POWERUP_FIELD_HEIGHT[0], PowerUpSettings.POWERUP_FIELD_HEIGHT[1])
        self.rect.x = randint(PowerUpSettings.POWERUP_FIELD_WIDTH[0], PowerUpSettings.POWERUP_FIELD_WIDTH[1])


# Mandatory PowerUps

# AntMan: The AntMan "Power-up" makes the player’s Paddle bigger
class ShrinkEnlarge(PowerUp):
    # Set PowerUp active time in seconds
    active_time: int = 5
    # Set the PowerUp probability
    probability: int = 50
    # Set the PowerUp name
    name: str = 'Ant-Man'

    def __init__(self, ball_owner, width, height):
        super().__init__(ball_owner, width, height)

        # Set the PowerUp image
        super().draw('img/icons/PowerUp_0.png')

    def affect_playerA(self, player_A):
        player_A.border_radius = 12
        player_A.image = pygame.transform.scale(player_A.image, (player_A.rect.width * 1.5, player_A.rect.height * 2))
        player_A.height = PaddleSettings.PADDLE_HEIGHT_A * 2

    def affect_playerB(self, player_B):
        player_B.border_radius = 12
        player_B.image = pygame.transform.scale(player_B.image, (player_B.rect.width * 1.5, player_B.rect.height * 2))
        player_B.height = PaddleSettings.PADDLE_HEIGHT_B * 2

    def run_powerup(self, paddleA, paddleB):
        if self.owner == 'paddleA':
            self.affect_playerA(paddleA)
        elif self.owner == 'paddleB':
            self.affect_playerB(paddleB)

    def revert_powerup(self, paddleA, paddleB):
        paddleA.border_radius, paddleB.border_radius = PaddleSettings.PADDLE_ROUND_CORNERS_A, \
            PaddleSettings.PADDLE_ROUND_CORNERS_B
        paddleA.image = pygame.transform.scale(paddleA.image, (paddleA.rect.width, paddleA.rect.height))
        paddleA.height = PaddleSettings.PADDLE_HEIGHT_A
        paddleB.image = pygame.transform.scale(paddleB.image, (paddleB.rect.width, paddleB.rect.height))
        paddleB.height = PaddleSettings.PADDLE_HEIGHT_B


# Freeze: The Freeze "Power-up" freezes the position of the player’s paddle
class Freeze(PowerUp):
    # Set PowerUp active time in seconds
    active_time: int = 3
    # Set the PowerUp probability
    probability: int = 60
    # Set the PowerUp name
    name: str = 'Freeze-Man'

    def __init__(self, ball_owner, width, height):
        super().__init__(ball_owner, width, height)

        # Set the PowerUp image
        super().draw('img/icons/PowerUp_1.png')

    def affect_playerA(self, player_A):
        PaddleSettings.PADDLE_SPEED_A = 0

    def affect_playerB(self, player_B):
        PaddleSettings.PADDLE_SPEED_B = 0

    def run_powerup(self, paddleA, paddleB):
        # If the ball is owned by player A
        if self.owner == 'paddleA':
            # Freeze player B
            self.affect_playerB(paddleB)
            # If the ball is owned by player B
        elif self.owner == 'paddleB':
            # Freeze player A
            self.affect_playerA(paddleA)

    def revert_powerup(self, paddleA, paddleB):
        PaddleSettings.PADDLE_SPEED_A = 5
        PaddleSettings.PADDLE_SPEED_B = 5


# MultipleBalls: The MultipleBalls "Power-up" creates a second ball that moves in the opposite direction
class MultipleBalls(PowerUp):
    # Set PowerUp active time in seconds
    active_time: int = 30
    # Set the PowerUp probability
    probability: int = 30
    # Set the PowerUp name
    name: str = 'Multiple-Man'

    def __init__(self, ball_owner, width, height):
        super().__init__(ball_owner, width, height)

        # Set the PowerUp image
        super().draw('img/icons/PowerUp_2.png')

    def affect_playerA(self, player_A):
        pass

    def affect_playerB(self, player_B):
        pass

    def run_powerup(self, paddleA, paddleB):
        pass

    def revert_powerup(self, paddleA, paddleB):
        pass


# Optional PowerUps

# Quicksilver: The Quicksilver "Power-up" increases the speed of the player’s paddle
class FasterPaddle(PowerUp):
    # Set PowerUp active time in seconds
    active_time: int = 6
    # Set the PowerUp probability
    probability: int = 30
    # Set the PowerUp name
    name: str = 'Quicksilver'

    def __init__(self, ball_owner, width, height):
        super().__init__(ball_owner, width, height)

        # Set the PowerUp image
        super().draw('img/icons/PowerUp_3.png')

    def affect_playerA(self, player_A):
        PaddleSettings.PADDLE_SPEED_A = PaddleSettings.FASTER_PADDLE_SPEED

    def affect_playerB(self, player_B):
        PaddleSettings.PADDLE_SPEED_B = PaddleSettings.FASTER_PADDLE_SPEED

    def run_powerup(self, paddleA, paddleB):
        if self.owner == 'paddleA':
            self.affect_playerA(paddleA)
        elif self.owner == 'paddleB':
            self.affect_playerB(paddleB)

    def revert_powerup(self, paddleA, paddleB):
        PaddleSettings.PADDLE_SPEED_A = PaddleSettings.DEFAULT_PADDLE_SPEED
        PaddleSettings.PADDLE_SPEED_B = PaddleSettings.DEFAULT_PADDLE_SPEED


# DoubleScore: The DoubleScore "Power-up" doubles the score of the player that hits the ball
class DoubleScore(PowerUp):
    # Set PowerUp active time in seconds
    active_time: int = 10
    # Set the PowerUp probability
    probability: int = 70
    # Set the PowerUp name
    name: str = 'Double-Man'

    def __init__(self, ball_owner, width, height):
        super().__init__(ball_owner, width, height)

        # Set the PowerUp image
        super().draw('img/icons/PowerUp_4.png')

    def affect_playerA(self, player_A):
        GameSettings.SCORE_ADDER_A = 2

    def affect_playerB(self, player_B):
        GameSettings.SCORE_ADDER_B = 2

    def run_powerup(self, paddleA, paddleB):
        if self.owner == 'paddleA':
            self.affect_playerA(paddleA)
        elif self.owner == 'paddleB':
            self.affect_playerB(paddleB)

    def revert_powerup(self, paddleA, paddleB):
        GameSettings.SCORE_ADDER_A, GameSettings.SCORE_ADDER_B = 1, 1


# Shield: The Shield "Power-up" creates a shield that protects the player’s paddle from the ball
class Shield(PowerUp):
    # Set PowerUp active time in seconds
    active_time: int = 6
    # Set the PowerUp probability
    probability: int = 50
    # Set the PowerUp name
    name: str = 'Iron-Man'

    def __init__(self, ball_owner, width, height):
        super().__init__(ball_owner, width, height)

        # Set the PowerUp image
        super().draw('img/icons/PowerUp_5.png')

    def affect_playerA(self, player_A):
        player_A.border_radius = 0
        player_A.image = pygame.transform.scale(player_A.image,
                                                (player_A.rect.width * 1.15, InterfaceSettings.WINDOW_HEIGHT))
        player_A.height = InterfaceSettings.WINDOW_HEIGHT

    def affect_playerB(self, player_B):
        player_B.border_radius = 0
        player_B.image = pygame.transform.scale(player_B.image,
                                                (player_B.rect.width * 1.15, InterfaceSettings.WINDOW_HEIGHT))
        player_B.height = InterfaceSettings.WINDOW_HEIGHT

    def run_powerup(self, paddleA, paddleB):
        if self.owner == 'paddleA':
            self.affect_playerA(paddleA)
        elif self.owner == 'paddleB':
            self.affect_playerB(paddleB)

    def revert_powerup(self, paddleA, paddleB):
        paddleA.border_radius, paddleB.border_radius = PaddleSettings.PADDLE_ROUND_CORNERS_A, \
            PaddleSettings.PADDLE_ROUND_CORNERS_B
        paddleA.image = pygame.transform.scale(paddleA.image, (paddleA.rect.width, paddleA.rect.height))
        paddleB.image = pygame.transform.scale(paddleB.image, (paddleB.rect.width, paddleB.rect.height))
        paddleA.height, paddleB.height = PaddleSettings.PADDLE_HEIGHT_A, PaddleSettings.PADDLE_HEIGHT_B


# Dictionary of PowerUps and their probabilities
PowerUps = {0: ShrinkEnlarge, 1: Freeze, 2: MultipleBalls, 3: FasterPaddle, 4: DoubleScore, 5: Shield}

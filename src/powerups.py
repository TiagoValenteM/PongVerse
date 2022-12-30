import pygame
from abc import ABC, abstractmethod
from random import randint
from src.config import GlobalSettings


# Class Parent for Powerups
class PowerUp(pygame.sprite.Sprite, ABC):  # sprite-Simple base class for visible game objects

    # Set the PowerUp visible time in seconds
    visible_time: int = GlobalSettings.POWERUP_VISIBLE_TIME

    def __init__(self, ball_owner, width, height, settings: GlobalSettings):
        # Call the parent class (Sprite) constructor
        super().__init__()
        # Pass PowerUp settings
        self.settings = settings
        # Set PowerUp width and height
        self.width, self.height = width, height
        # Set the ball owner to affect a certain player
        self.owner = ball_owner

    # Abstract Method that affects player A
    @abstractmethod
    def affect_playerA(self, player_A):
        pass

    # Abstract Method that affects player B
    @abstractmethod
    def affect_playerB(self, player_B):
        pass

    # Abstract Method that runs the powerup
    @abstractmethod
    def run_powerup(self, paddleA, paddleB):
        pass

    # Abstract Methods that reverts the powerup
    @abstractmethod
    def revert_powerup(self, paddleA, paddleB):
        pass

    # Draw the powerup icon on the screen
    def draw(self, filename):
        # Load and scale the image
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        # Draw and get the rect object
        pygame.draw.rect(self.image, self.settings.BLACK, [self.width, self.height, 0, 0])
        self.rect = self.image.get_rect()
        # Set the position of the powerup on the field
        self.rect.y = randint(self.settings.powerup_field_height[0], self.settings.powerup_field_height[1])
        self.rect.x = randint(self.settings.powerup_field_width[0], self.settings.powerup_field_width[1])


# === Mandatory PowerUps ===

# AntMan: The AntMan "Power-up" makes the player’s Paddle bigger
class ShrinkEnlarge(PowerUp):
    active_time: int = 5  # PowerUp active time in seconds
    probability: int = 15  # PowerUp probability
    name: str = 'Ant-Man'  # PowerUp name
    description: str = 'Enlarges your paddle size'  # Powerup Description
    icon: str = 'img/icons/powerup5.png'  # Icon path

    def __init__(self, ball_owner, width, height, settings: GlobalSettings):
        # Call the parent class (Powerup)
        super().__init__(ball_owner, width, height, settings)
        super().draw(self.icon)  # Call the draw method

    def affect_playerA(self, player_A):
        # Change the paddle A size and border radius
        player_A.border_radius = 12
        player_A.image = pygame.transform.scale(player_A.image, (player_A.rect.width * 1.5, player_A.rect.height * 2))
        player_A.height = self.settings.paddle_height_a * 2

    def affect_playerB(self, player_B):
        # Change the paddle B size and border radius
        player_B.border_radius = 12
        player_B.image = pygame.transform.scale(player_B.image, (player_B.rect.width * 1.5, player_B.rect.height * 2))
        player_B.height = self.settings.paddle_height_b * 2

    def run_powerup(self, paddleA, paddleB):  # Affects the ball owner
        if self.owner == 'paddleA':
            self.affect_playerA(paddleA)
        elif self.owner == 'paddleB':
            self.affect_playerB(paddleB)

    def revert_powerup(self, paddleA, paddleB):
        # Revert the paddle size and border radius
        paddleA.border_radius, paddleB.border_radius = self.settings.PADDLE_ROUND_CORNERS_A, \
            self.settings.PADDLE_ROUND_CORNERS_B
        paddleA.image = pygame.transform.scale(paddleA.image, (paddleA.rect.width, paddleA.rect.height))
        paddleA.height = self.settings.paddle_height_a
        paddleB.image = pygame.transform.scale(paddleB.image, (paddleB.rect.width, paddleB.rect.height))
        paddleB.height = self.settings.paddle_height_b


# Black Widow: The Black Widow "Power-up" freezes the position of the player’s paddle
class Freeze(PowerUp):
    active_time: int = 3  # PowerUp active time in seconds
    probability: int = 20  # PowerUp probability
    name: str = 'Black Widow'  # PowerUp name
    description: str = 'Freezes your opponent paddle'  # Powerup Description
    icon: str = 'img/icons/powerup3.png'  # Icon path

    def __init__(self, ball_owner, width, height, settings: GlobalSettings):
        # Call the parent class (Powerup)
        super().__init__(ball_owner, width, height, settings)
        super().draw(self.icon)  # Call the draw method

    def affect_playerA(self, player_A):
        # Freeze player A
        self.settings.PADDLE_SPEED_A = 0

    def affect_playerB(self, player_B):
        # Freeze player B
        self.settings.PADDLE_SPEED_B = 0

    def run_powerup(self, paddleA, paddleB):  # Does not affect the ball owner
        # If the ball is owned by player A
        if self.owner == 'paddleA':
            # Freeze player B
            self.affect_playerB(paddleB)
            # If the ball is owned by player B
        elif self.owner == 'paddleB':
            # Freeze player A
            self.affect_playerA(paddleA)

    def revert_powerup(self, paddleA, paddleB):
        # Revert the paddle speed
        self.settings.PADDLE_SPEED_A = 5
        self.settings.PADDLE_SPEED_B = 5


# Scarlet Witch: The Scarlet Witch "Power-up" creates multiple balls that move in the different directions
class MultipleBalls(PowerUp):
    active_time: int = 30  # PowerUp active time in seconds
    probability: int = 10  # PowerUp probability
    name: str = 'Scarlet Witch'  # PowerUp name
    description: str = 'Multiple balls that score for you'  # Powerup Description
    icon: str = 'img/icons/powerup6.png'  # Icon path

    def __init__(self, ball_owner, width, height, settings: GlobalSettings):
        # Call the parent class (Powerup)
        super().__init__(ball_owner, width, height, settings)
        super().draw(self.icon)  # Call the draw method

    # -- Powerup controlled on PongGame class --

    def affect_playerA(self, player_A):
        pass

    def affect_playerB(self, player_B):
        pass

    def run_powerup(self, paddleA, paddleB):  # Does not affect the ball owner
        pass

    def revert_powerup(self, paddleA, paddleB):
        pass


# === Optional PowerUps ===

# Quicksilver: The Quicksilver "Power-up" increases the speed of the player’s paddle
class FasterPaddle(PowerUp):
    active_time: int = 6  # PowerUp active time in seconds
    probability: int = 15  # PowerUp probability
    name: str = 'Quicksilver'  # PowerUp name
    description: str = 'Increases your paddle speed'  # Powerup Description
    icon: str = 'img/icons/powerup1.png'  # Icon path

    def __init__(self, ball_owner, width, height, settings: GlobalSettings):
        # Call the parent class (Powerup)
        super().__init__(ball_owner, width, height, settings)
        super().draw(self.icon)  # Call the draw method

    def affect_playerA(self, player_A):
        # Increase player A paddle speed
        self.settings.PADDLE_SPEED_A = self.settings.FASTER_PADDLE_SPEED

    def affect_playerB(self, player_B):
        # Increase player B paddle speed
        self.settings.PADDLE_SPEED_B = self.settings.FASTER_PADDLE_SPEED

    def run_powerup(self, paddleA, paddleB):  # Affects the ball owner
        if self.owner == 'paddleA':
            self.affect_playerA(paddleA)
        elif self.owner == 'paddleB':
            self.affect_playerB(paddleB)

    def revert_powerup(self, paddleA, paddleB):
        # Revert player A and player B paddle speed
        self.settings.PADDLE_SPEED_A = self.settings.DEFAULT_PADDLE_SPEED
        self.settings.PADDLE_SPEED_B = self.settings.DEFAULT_PADDLE_SPEED


# Iron Man: The Iron Man "Power-up" doubles the score of the player that hits the ball
class DoubleScore(PowerUp):
    active_time: int = 10  # PowerUp active time in seconds
    probability: int = 25  # PowerUp probability
    name: str = 'Iron Man'  # PowerUp name
    description: str = 'Doubles your score'  # Powerup Description
    icon: str = 'img/icons/powerup4.png'  # Icon path

    def __init__(self, ball_owner, width, height, settings: GlobalSettings):
        # Call the parent class (Powerup)
        super().__init__(ball_owner, width, height, settings)
        super().draw(self.icon)  # Call the draw method

    def affect_playerA(self, player_A):
        # Double the score of player A
        self.settings.SCORE_ADDER_A = 2

    def affect_playerB(self, player_B):
        # Double the score of player B
        self.settings.SCORE_ADDER_B = 2

    def run_powerup(self, paddleA, paddleB):  # Affects the ball owner
        if self.owner == 'paddleA':
            self.affect_playerA(paddleA)
        elif self.owner == 'paddleB':
            self.affect_playerB(paddleB)

    def revert_powerup(self, paddleA, paddleB):
        # Revert the score adder to 1
        self.settings.SCORE_ADDER_A, self.settings.SCORE_ADDER_B = 1, 1


# Captain America: The Captain America "Power-up" creates a shield that protects the player’s paddle from the ball
class Shield(PowerUp):
    active_time: int = 6  # PowerUp active time in seconds
    probability: int = 15  # PowerUp probability
    name: str = 'Captain America'  # PowerUp name
    description: str = 'Creates a shield on your paddle'  # Powerup Description
    icon: str = 'img/icons/powerup2.png'  # Icon path

    def __init__(self, ball_owner, width, height, settings: GlobalSettings):
        # Call the parent class (Powerup)
        super().__init__(ball_owner, width, height, settings)
        super().draw(self.icon)  # Call the draw method

    def affect_playerA(self, player_A):
        # Create a shield on the paddle A (Height = 100%)
        player_A.image = pygame.transform.scale(player_A.image,
                                                (player_A.rect.width * 1.15, self.settings.height))
        player_A.height = self.settings.height

    def affect_playerB(self, player_B):
        # Create a shield on the paddle B (Height = 100%)
        player_B.image = pygame.transform.scale(player_B.image,
                                                (player_B.rect.width * 1.15, self.settings.height))
        player_B.height = self.settings.height

    def run_powerup(self, paddleA, paddleB):  # Affects the ball owner
        if self.owner == 'paddleA':
            self.affect_playerA(paddleA)
        elif self.owner == 'paddleB':
            self.affect_playerB(paddleB)

    def revert_powerup(self, paddleA, paddleB):
        # Revert paddle A and paddle B to their original size
        paddleA.image = pygame.transform.scale(paddleA.image, (paddleA.rect.width, paddleA.rect.height))
        paddleB.image = pygame.transform.scale(paddleB.image, (paddleB.rect.width, paddleB.rect.height))
        paddleA.height, paddleB.height = self.settings.paddle_height_a, self.settings.paddle_height_b


# Dictionary of PowerUps and their probabilities
PowerUps = {0: ShrinkEnlarge, 1: Freeze, 2: MultipleBalls, 3: FasterPaddle, 4: DoubleScore, 5: Shield}

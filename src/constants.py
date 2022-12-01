import pygame
from .ball import Ball


# Static Class for the Game Settings
class GameSettings:
    # Set the game Icon displayed in the dock
    GAME_ICON: any = pygame.image.load("img/ball_avengers.png")

    # Set the game title
    GAME_TITLE: str = "The PongVerse"

    # Set Colors
    BLACK: tuple = (0, 0, 0)
    WHITE: tuple = (255, 255, 255)
    BLUE: tuple = (37, 150, 190)
    MAGENTA: tuple = (204, 51, 139)

    # Set Font Size
    FONT_SIZE: int = 70

    # Set window size
    WINDOW_WIDTH: int = 700
    WINDOW_HEIGHT: int = 500
    WINDOW_SIZE: tuple = (WINDOW_WIDTH, WINDOW_HEIGHT)

    # Set PowerUp size
    POWERUP_WIDTH: int = 60
    POWERUP_HEIGHT: int = 60

    # Set PowerUp field of view size
    POWERUP_FIELD_WIDTH: int = WINDOW_WIDTH - POWERUP_WIDTH * 2
    POWERUP_FIELD_HEIGHT: int = WINDOW_HEIGHT - POWERUP_HEIGHT * 2

    # Set PowerUp visible time in seconds
    POWERUP_VISIBLE_TIME: int = 5

    # Set score to win the game
    WIN_SCORE: int = 10

    # Set score Position
    POS_SCORE_B: float = (WINDOW_WIDTH / 2 + FONT_SIZE / 1.7, 15)
    POS_SCORE_A: float = (WINDOW_WIDTH / 2 - FONT_SIZE, 15)


# Static Class for the Ball Settings
class BallSettings:
    # Set ball size
    BALL_WIDTH: int = 40
    BALL_HEIGHT: int = 40

    # Set ball initial position
    INITIAL_POS_X: int = GameSettings.WINDOW_WIDTH / 2 - BALL_WIDTH / 2
    INITIAL_POS_Y: int = GameSettings.WINDOW_HEIGHT / 2 - BALL_HEIGHT / 2


# Static Class for the Paddle Settings
class PaddleSettings:
    # Set Paddle A size
    PADDLE_WIDTH_A: int = 10
    PADDLE_HEIGHT_A: float = GameSettings.WINDOW_HEIGHT / 5

    # Set Paddle B size
    PADDLE_WIDTH_B: int = 10
    PADDLE_HEIGHT_B: float = GameSettings.WINDOW_HEIGHT / 5

    # Set PaddleA initial position
    INITIAL_POS_X_A: int = 0 + PADDLE_WIDTH_A * 2
    INITIAL_POS_Y_A: int = GameSettings.WINDOW_HEIGHT / 2 - PADDLE_HEIGHT_A / 2

    # Set PaddleB initial position
    INITIAL_POS_X_B: int = GameSettings.WINDOW_WIDTH - PADDLE_WIDTH_B * 2
    INITIAL_POS_Y_B: int = GameSettings.WINDOW_HEIGHT / 2 - PADDLE_HEIGHT_B / 2

# TODO: Create a dictionary for window sizes

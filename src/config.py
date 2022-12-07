import pygame


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

    # Set Font Size and Type
    FONT_SIZE: int = 70
    FONT_TYPE: str = "font/default_font.ttf"

    # Set window size
    WINDOW_WIDTH: int = 1280
    WINDOW_HEIGHT: int = 720
    WINDOW_SIZE: tuple = (WINDOW_WIDTH, WINDOW_HEIGHT)

    # Set background Image
    BACKGROUND_IMG_LOAD: any = pygame.image.load("img/background.jpg")
    BACKGROUND_IMG: any = pygame.transform.scale(BACKGROUND_IMG_LOAD, (WINDOW_WIDTH, WINDOW_HEIGHT))

    # Set PowerUp size
    POWERUP_WIDTH: int = WINDOW_HEIGHT / 10
    POWERUP_HEIGHT: int = WINDOW_HEIGHT / 10

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
    BALL_WIDTH: int = GameSettings.WINDOW_WIDTH / 20
    BALL_HEIGHT: int = GameSettings.WINDOW_WIDTH / 20

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

    # Set Paddle speed
    PADDLE_SPEED_A: int = 5
    PADDLE_SPEED_B: int = 5


# Create a Dictionary of all the screen resolutions
Screen_Resolution = {1: (640, 360), 2: (854, 480), 3: (960, 540), 4: (1280, 720),
                     5: (1920, 1080), 6: (2560, 1440), 7: (3840, 2160)}

import pygame

# Create a Dictionary of all the screen resolutions
Screen_Resolution = {'360p': (640, 360), '480p': (854, 480), '540p': (960, 540), '720p': (1280, 720),
                     '1080p': (1920, 1080), '1440p': (2560, 1440), '2160p': (3840, 2160)}


# Static Class for the Game Settings
class GameSettings:
    # Set the game Icon displayed in the dock
    GAME_ICON: any = pygame.image.load("img/ball_avengers.png")

    # Set the game title
    GAME_TITLE: str = "The PongVerse"

    # Set window size
    WINDOW_WIDTH: int = Screen_Resolution['720p'][0]
    WINDOW_HEIGHT: int = Screen_Resolution['720p'][1]
    WINDOW_SIZE: tuple = (WINDOW_WIDTH, WINDOW_HEIGHT)

    # Set Players Icons size
    PLAYER_ICON_SIZE: tuple = (WINDOW_WIDTH / 17, WINDOW_WIDTH / 17)

    # Set Players Icons
    PLAYER_A_ICON: any = pygame.transform.smoothscale(pygame.image.load("img/playerA_icon.png"), PLAYER_ICON_SIZE)
    PLAYER_B_ICON: any = pygame.transform.smoothscale(pygame.image.load("img/playerB_icon.png"), PLAYER_ICON_SIZE)

    # Set PLayers Icons Position
    PLAYER_A_ICON_POS: tuple = (WINDOW_WIDTH / 12, 20)
    PLAYER_B_ICON_POS: tuple = (WINDOW_WIDTH - (WINDOW_WIDTH / 12 + PLAYER_ICON_SIZE[0]), 20)

    # Set Colors
    BLACK: tuple = (0, 0, 0)
    WHITE: tuple = (255, 255, 255)
    BLUE: tuple = (71, 94, 126)
    GOLDEN: tuple = (209, 165, 91)
    RED: tuple = (183, 39, 30)

    # Set Font Size and Type
    FONT_TYPE: str = "font/default_font_pong.ttf"
    FONT_SIZE_DEFAULT: int = int(WINDOW_WIDTH / 17)
    FONT_SIZE_POWERUP: int = int(WINDOW_WIDTH / 23)

    # Set background Image
    BACKGROUND_IMG_LOAD: any = pygame.image.load("img/background.jpg")
    BACKGROUND_IMG: any = pygame.transform.scale(BACKGROUND_IMG_LOAD, (WINDOW_WIDTH, WINDOW_HEIGHT))

    # Set score to win the game
    WIN_SCORE: int = 10

    # Set score Position
    POS_SCORE_B: float = (WINDOW_WIDTH / 2 + FONT_SIZE_DEFAULT / 1.7, 15)
    POS_SCORE_A: float = (WINDOW_WIDTH / 2 - FONT_SIZE_DEFAULT, 15)

    # Set score adder
    SCORE_ADDER_A: int = 1
    SCORE_ADDER_B: int = 1

    # Set the Field Divider Height
    FIELD_DIVIDER_INITIAL_POS: tuple = (WINDOW_WIDTH / 2, WINDOW_HEIGHT * 0.03)
    FIELD_DIVIDER_MAX_POS: tuple = (WINDOW_WIDTH / 2, WINDOW_HEIGHT - WINDOW_HEIGHT * 0.03)


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
    PADDLE_WIDTH_A: int = GameSettings.WINDOW_HEIGHT / 50
    PADDLE_HEIGHT_A: float = GameSettings.WINDOW_HEIGHT / 5

    # Set Paddle B size
    PADDLE_WIDTH_B: int = GameSettings.WINDOW_HEIGHT / 50
    PADDLE_HEIGHT_B: float = GameSettings.WINDOW_HEIGHT / 5

    # Set PaddleA initial position
    INITIAL_POS_X_A: int = 0 + PADDLE_WIDTH_A * 2
    INITIAL_POS_Y_A: int = GameSettings.WINDOW_HEIGHT / 2 - PADDLE_HEIGHT_A / 2

    # Set PaddleB initial position
    INITIAL_POS_X_B: int = GameSettings.WINDOW_WIDTH - PADDLE_WIDTH_B * 3
    INITIAL_POS_Y_B: int = GameSettings.WINDOW_HEIGHT / 2 - PADDLE_HEIGHT_B / 2

    # Set Paddle speed
    PADDLE_SPEED_A: int = 5
    PADDLE_SPEED_B: int = 5

    # Set Rounder Corners of the Paddle
    PADDLE_ROUND_CORNERS_A: int = 7
    PADDLE_ROUND_CORNERS_B: int = 7


class PowerUpSettings:
    # Set PowerUp size
    POWERUP_WIDTH: int = GameSettings.WINDOW_HEIGHT / 10
    POWERUP_HEIGHT: int = GameSettings.WINDOW_HEIGHT / 10

    # Set PowerUp field of view size
    POWERUP_FIELD_WIDTH: tuple = (
        int(GameSettings.WINDOW_WIDTH * 0.17), int(GameSettings.WINDOW_WIDTH - GameSettings.WINDOW_WIDTH * 0.17))
    POWERUP_FIELD_HEIGHT: tuple = (
        int(GameSettings.WINDOW_HEIGHT * 0.17), int(GameSettings.WINDOW_HEIGHT - GameSettings.WINDOW_HEIGHT * 0.17))

    # Set PowerUp visible time in seconds
    POWERUP_VISIBLE_TIME: int = 5

    # Set PowerUp active time in seconds
    POWERUP_ACTIVE_TIME: int = 5

    # Set PowerUp Name visible time in seconds
    POWERUP_NAME_VISIBLE_TIME: int = 2

import pygame

# Create a Dictionary of all the screen resolutions
Screen_Resolution = {'360p': (640, 360), '480p': (854, 480), '540p': (960, 540), '720p': (1280, 720),
                     '1080p': (1920, 1080), '1440p': (2560, 1440), '2160p': (3840, 2160)}


# Static Class for the Interface Settings
class InterfaceSettings:
    # Set the game Icon displayed in the dock
    ICON: any = pygame.image.load("img/icons/main_icon.png")

    # Set interface titles
    MENU_TITLE: str = "Main Menu"
    SETTINGS_TITLE: str = "Settings"
    CREDITS_TITLE: str = "Credits"

    # Set window size
    WINDOW_WIDTH: int = Screen_Resolution['720p'][0]
    WINDOW_HEIGHT: int = Screen_Resolution['720p'][1]
    WINDOW_SIZE: tuple = (WINDOW_WIDTH, WINDOW_HEIGHT)


# Static Class for the Game Settings
class GameSettings:
    # Set the game title
    GAME_TITLE: str = "The PongVerse"
    GAME_TITLE_VANILLA: str = "The PongVerse (Vanilla Edition)"

    # Set Players Icons size
    PLAYER_ICON_SIZE: tuple = (InterfaceSettings.WINDOW_WIDTH / 17, InterfaceSettings.WINDOW_WIDTH / 17)

    # Set Players Icons
    PLAYER_A_ICON: any = pygame.transform.smoothscale(pygame.image.load("img/icons/playerA_icon.png"), PLAYER_ICON_SIZE)
    PLAYER_B_ICON: any = pygame.transform.smoothscale(pygame.image.load("img/icons/playerB_icon.png"), PLAYER_ICON_SIZE)

    # Set PLayers Icons Position
    PLAYER_A_ICON_POS: tuple = (InterfaceSettings.WINDOW_WIDTH / 12, 20)
    PLAYER_B_ICON_POS: tuple = (
        InterfaceSettings.WINDOW_WIDTH - (InterfaceSettings.WINDOW_WIDTH / 12 + PLAYER_ICON_SIZE[0]), 20)

    # Set Colors
    BLACK: tuple = (0, 0, 0)
    WHITE: tuple = (255, 255, 255)
    BLUE: tuple = (71, 94, 126)
    GOLDEN: tuple = (209, 165, 91)
    RED: tuple = (183, 39, 30)
    GREEN: tuple = (175, 225, 175)

    # Set Font Size and Type
    FONT_TYPE_DEFAULT: str = "font/default_font_pong.ttf"
    FONT_TYPE_MENU: str = "font/menu_font.ttf"
    FONT_SIZE_DEFAULT: int = int(InterfaceSettings.WINDOW_WIDTH / 17)
    FONT_SIZE_POWERUP: int = int(InterfaceSettings.WINDOW_WIDTH / 23)
    FONT_SIZE_MENU: int = int(InterfaceSettings.WINDOW_WIDTH / 40)

    # Set background Image
    BACKGROUND_IMG: any = pygame.transform.scale(pygame.image.load("img/background/background.jpg"),
                                                 (InterfaceSettings.WINDOW_WIDTH, InterfaceSettings.WINDOW_HEIGHT))

    # Set Background Image for Win Screen
    WIN_SCREEN_A_IMG: any = pygame.transform.scale(pygame.image.load("img/background/background_winA.jpg"),
                                                   (InterfaceSettings.WINDOW_WIDTH, InterfaceSettings.WINDOW_HEIGHT))
    WIN_SCREEN_B_IMG: any = pygame.transform.scale(pygame.image.load("img/background/background_winB.jpg"),
                                                   (InterfaceSettings.WINDOW_WIDTH, InterfaceSettings.WINDOW_HEIGHT))

    # Set Winner Icon
    WINNER_ICON_SIZE: tuple = (InterfaceSettings.WINDOW_WIDTH / 6, InterfaceSettings.WINDOW_WIDTH / 6)
    WINNER_ICON_A: any = pygame.transform.smoothscale(pygame.image.load("img/icons/winner_iconA.png"), WINNER_ICON_SIZE)
    WINNER_ICON_B: any = pygame.transform.smoothscale(pygame.image.load("img/icons/winner_iconB.png"), WINNER_ICON_SIZE)

    # Set score to win the game
    WIN_SCORE: int = 10

    # Set score Position
    POS_SCORE_B: float = (InterfaceSettings.WINDOW_WIDTH / 2 + FONT_SIZE_DEFAULT / 1.7, 15)
    POS_SCORE_A: float = (InterfaceSettings.WINDOW_WIDTH / 2 - FONT_SIZE_DEFAULT, 15)

    # Set score adder
    SCORE_ADDER_A: int = 1
    SCORE_ADDER_B: int = 1

    # Set the Field Divider Height
    FIELD_DIVIDER_INITIAL_POS: tuple = (InterfaceSettings.WINDOW_WIDTH / 2, InterfaceSettings.WINDOW_HEIGHT * 0.03)
    FIELD_DIVIDER_MAX_POS: tuple = (
        InterfaceSettings.WINDOW_WIDTH / 2, InterfaceSettings.WINDOW_HEIGHT - InterfaceSettings.WINDOW_HEIGHT * 0.03)


# Static Class for Instructions Settings
class InstructionsSettings:
    # Set background Image

    BACKGROUND_IMG_LOAD: any = pygame.image.load("img/background/instructions_background.jpg")
    BACKGROUND_IMG: any = pygame.transform.scale(BACKGROUND_IMG_LOAD, (InterfaceSettings.WINDOW_WIDTH,
                                                                       InterfaceSettings.WINDOW_HEIGHT))

    # Set the game title
    INSTRUCTIONS_TITLE: str = "Instructions"
    INSTRUCTIONS_TITLE_VANILLA: str = "Instructions (Vanilla Edition)"


# Static Class for the Ball Settings
class BallSettings:
    # Set ball size
    BALL_WIDTH: int = InterfaceSettings.WINDOW_WIDTH / 20
    BALL_HEIGHT: int = InterfaceSettings.WINDOW_WIDTH / 20

    # Set ball initial position
    INITIAL_POS_X: int = InterfaceSettings.WINDOW_WIDTH / 2 - BALL_WIDTH / 2
    INITIAL_POS_Y: int = InterfaceSettings.WINDOW_HEIGHT / 2 - BALL_HEIGHT / 2

    MIN_ADDITIONAL_BALLS: int = 2
    MAX_ADDITIONAL_BALLS: int = 4


# Static Class for the Paddle Settings
class PaddleSettings:
    # Set Paddle A size
    PADDLE_WIDTH_A: int = InterfaceSettings.WINDOW_HEIGHT / 50
    PADDLE_HEIGHT_A: float = InterfaceSettings.WINDOW_HEIGHT / 5

    # Set Paddle B size
    PADDLE_WIDTH_B: int = InterfaceSettings.WINDOW_HEIGHT / 50
    PADDLE_HEIGHT_B: float = InterfaceSettings.WINDOW_HEIGHT / 5

    # Set PaddleA initial position
    INITIAL_POS_X_A: int = 0 + PADDLE_WIDTH_A * 2
    INITIAL_POS_Y_A: int = InterfaceSettings.WINDOW_HEIGHT / 2 - PADDLE_HEIGHT_A / 2

    # Set PaddleB initial position
    INITIAL_POS_X_B: int = InterfaceSettings.WINDOW_WIDTH - PADDLE_WIDTH_B * 3
    INITIAL_POS_Y_B: int = InterfaceSettings.WINDOW_HEIGHT / 2 - PADDLE_HEIGHT_B / 2

    # Set Paddle speed
    PADDLE_SPEED_A: float = 5
    PADDLE_SPEED_B: float = 5
    DEFAULT_PADDLE_SPEED: int = 5
    FASTER_PADDLE_SPEED: float = 6.3

    # Set Rounder Corners of the Paddle
    PADDLE_ROUND_CORNERS_A: int = 7
    PADDLE_ROUND_CORNERS_B: int = 7


class PowerUpSettings:
    # Set PowerUp size
    POWERUP_WIDTH: int = InterfaceSettings.WINDOW_HEIGHT / 10
    POWERUP_HEIGHT: int = InterfaceSettings.WINDOW_HEIGHT / 10

    # Set PowerUp field of view size
    POWERUP_FIELD_WIDTH: tuple = (
        int(InterfaceSettings.WINDOW_WIDTH * 0.17),
        int(InterfaceSettings.WINDOW_WIDTH - InterfaceSettings.WINDOW_WIDTH * 0.17))
    POWERUP_FIELD_HEIGHT: tuple = (
        int(InterfaceSettings.WINDOW_HEIGHT * 0.17),
        int(InterfaceSettings.WINDOW_HEIGHT - InterfaceSettings.WINDOW_HEIGHT * 0.17))

    # Set PowerUp visible time in seconds
    POWERUP_VISIBLE_TIME: int = 5

    # Set PowerUp Name visible time in seconds
    POWERUP_NAME_VISIBLE_TIME: int = 2

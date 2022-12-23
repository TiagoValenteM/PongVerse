import pygame

# Create a Dictionary of all the screen resolutions
Screen_Resolution = {'360p': (640, 360), '480p': (854, 480), '540p': (960, 540), '720p': (1280, 720),
                     '1080p': (1920, 1080), '1440p': (2560, 1440), '2160p': (3840, 2160)}


# Static Class for the Interface Settings
class InterfaceSettings:
    # Set interface titles
    MENU_TITLE: str = "Main Menu"
    SETTINGS_TITLE: str = "Settings"
    CREDITS_TITLE: str = "Creators"

    # Set window size
    WINDOW_WIDTH: int = Screen_Resolution['720p'][0]
    WINDOW_HEIGHT: int = Screen_Resolution['720p'][1]
    WINDOW_SIZE: tuple = (WINDOW_WIDTH, WINDOW_HEIGHT)

    # Set Menu Buttons size
    BUTTON_WIDTH: int = int(WINDOW_WIDTH * 0.3)
    BUTTON_HEIGHT: int = int(WINDOW_HEIGHT * 0.06)
    SMALL_BUTTON_WIDTH: int = int(WINDOW_WIDTH * 0.1)
    SMALL_BUTTON_HEIGHT: int = int(WINDOW_HEIGHT * 0.06)
    BUTTON_GAP: int = int(BUTTON_HEIGHT * 2)

    # Set NovaIMS icon size and load
    NOVAIMS_ICON_SIZE: tuple = (WINDOW_WIDTH * 0.07, WINDOW_WIDTH * 0.07)
    NOVAIMS_IMG_LOAD: pygame.image = pygame.transform.smoothscale(pygame.image.load("img/creators/novaims_logo.png"),
                                                                  NOVAIMS_ICON_SIZE)


# Static Class for the Game Settings
class GameSettings:
    # Set the game title
    GAME_TITLE: str = "The PongVerse"
    GAME_TITLE_VANILLA: str = "The PongVerse (Vanilla Edition)"

    # Set Players Icons size
    PLAYER_ICON_SIZE: tuple = (InterfaceSettings.WINDOW_WIDTH / 17, InterfaceSettings.WINDOW_WIDTH / 17)

    # Set PLayers Icons Position
    PLAYER_A_ICON_POS: tuple = (InterfaceSettings.WINDOW_WIDTH / 12, 20)
    PLAYER_B_ICON_POS: tuple = (
        InterfaceSettings.WINDOW_WIDTH - (InterfaceSettings.WINDOW_WIDTH / 12 + PLAYER_ICON_SIZE[0]), 20)

    # Set Colors
    BLACK: tuple = (0, 0, 0)
    WHITE: tuple = (255, 255, 255)
    BLUE: tuple = (71, 94, 126)
    LIGHT_BLUE: tuple = (202, 230, 250)
    GOLDEN: tuple = (209, 165, 91)
    RED: tuple = (183, 39, 30)
    GREEN: tuple = (175, 225, 175)
    PURPLE: tuple = (87, 18, 199)
    GRAY: tuple = (44, 44, 44)

    # Set Font Size and Type
    FONT_TYPE_DEFAULT: str = "font/default_font_pong.ttf"
    FONT_TYPE_MENU: str = "font/menu_font.ttf"
    FONT_SIZE_DEFAULT: int = int(InterfaceSettings.WINDOW_WIDTH / 17)
    FONT_SIZE_POWERUP: int = int(InterfaceSettings.WINDOW_WIDTH / 23)
    FONT_SIZE_SMALL_POWERUP: int = int(InterfaceSettings.WINDOW_WIDTH / 70)
    FONT_SIZE_MENU: int = int(InterfaceSettings.WINDOW_WIDTH / 40)

    # Set Winner Icon Size
    WINNER_ICON_SIZE: tuple = (InterfaceSettings.WINDOW_WIDTH / 6, InterfaceSettings.WINDOW_WIDTH / 6)

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
    BACKGROUND_IMG: any = pygame.transform.scale(pygame.image.load("img/background/background_instructions.jpg"),
                                                 (InterfaceSettings.WINDOW_WIDTH,
                                                  InterfaceSettings.WINDOW_HEIGHT))

    # Set the game title
    INSTRUCTIONS_TITLE: str = "Instructions"
    INSTRUCTIONS_TITLE_VANILLA: str = "Instructions (Vanilla Edition)"

    # Set Font Size
    TITLE_SIZE: int = int(InterfaceSettings.WINDOW_WIDTH / 28)
    SUBTITLE_SIZE: int = int(InterfaceSettings.WINDOW_WIDTH / 46)
    BODY_SIZE: int = int(InterfaceSettings.WINDOW_WIDTH / 78)
    SMALL_BODY_SIZE: int = int(InterfaceSettings.WINDOW_WIDTH / 90)

    # Set PowerUp icon Instructions size
    POWERUP_WIDTH: float = InterfaceSettings.WINDOW_HEIGHT / 11
    POWERUP_HEIGHT: float = InterfaceSettings.WINDOW_HEIGHT / 11

    # Set Screen Alignments
    RIGHT_X_ALIGNMENT: float = (InterfaceSettings.WINDOW_WIDTH * 0.07)
    SECOND_RIGHT_X_ALIGNMENT: float = (InterfaceSettings.WINDOW_WIDTH * 0.37)
    LEFT_X_ALIGNMENT: float = (InterfaceSettings.WINDOW_WIDTH * 0.75)

    # Set Player keys icon size
    PLAYER_KEYS_WIDTH: float = InterfaceSettings.WINDOW_HEIGHT / 20
    PLAYER_KEYS_HEIGHT: float = InterfaceSettings.WINDOW_HEIGHT / 20

    # Set Player keys icon and position
    PLAYER_A_UP: pygame.transform = (
        pygame.transform.smoothscale(pygame.image.load("img/icons/playerA_up.png"),
                                     (PLAYER_KEYS_WIDTH,
                                      PLAYER_KEYS_HEIGHT)))
    PLAYER_A_DOWN: pygame.transform = (
        pygame.transform.smoothscale(pygame.image.load("img/icons/playerA_down.png"),
                                     (PLAYER_KEYS_WIDTH,
                                      PLAYER_KEYS_HEIGHT)))
    PLAYER_B_UP: pygame.transform = (
        pygame.transform.smoothscale(pygame.image.load("img/icons/playerB_up.png"),
                                     (PLAYER_KEYS_WIDTH,
                                      PLAYER_KEYS_HEIGHT)))
    PLAYER_B_DOWN: pygame.transform = (
        pygame.transform.smoothscale(pygame.image.load("img/icons/playerB_down.png"),
                                     (PLAYER_KEYS_WIDTH,
                                      PLAYER_KEYS_HEIGHT)))

    # Set Escape key icon size
    ESCAPE_KEY_WIDTH: float = InterfaceSettings.WINDOW_HEIGHT / 23
    ESCAPE_KEY_HEIGHT: float = InterfaceSettings.WINDOW_HEIGHT / 23

    # Set Escape key icon and position
    ESCAPE_KEY: tuple = (pygame.transform.smoothscale(pygame.image.load("img/icons/esc_key.png"),
                                                      (ESCAPE_KEY_WIDTH,
                                                       ESCAPE_KEY_HEIGHT)),
                         (InterfaceSettings.WINDOW_WIDTH * 0.96, InterfaceSettings.WINDOW_HEIGHT * 0.04))


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
    PADDLE_ROUND_CORNERS_A: int = 5
    PADDLE_ROUND_CORNERS_B: int = 5
    PADDLE_ROUND_CORNERS_SHIELD: int = 0


class PowerUpSettings:
    # Set PowerUp icon size
    POWERUP_WIDTH: int = InterfaceSettings.WINDOW_HEIGHT / 8
    POWERUP_HEIGHT: int = InterfaceSettings.WINDOW_HEIGHT / 8

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

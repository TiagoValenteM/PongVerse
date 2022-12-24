import pygame

# Create a Dictionary of all the screen resolutions
Screen_Resolution = {'480p': (854, 480), '720p': (1280, 720), '1080p': (1920, 1080), '1440p': (2560, 1440),
                     '2160p': (3840, 2160)}


class GlobalSettings:
    # == Static Attributes ==
    # Titles
    MENU_TITLE: str = "Main Menu"
    SETTINGS_TITLE: str = "Settings"
    CREDITS_TITLE: str = "Creators"
    GAME_TITLE: str = "The PongVerse"
    GAME_TITLE_VANILLA: str = "The PongVerse (Vanilla Edition)"
    INSTRUCTIONS_TITLE: str = "Instructions"
    INSTRUCTIONS_TITLE_VANILLA: str = "Instructions (Vanilla Edition)"

    # Colors
    BLACK: tuple = (0, 0, 0)
    WHITE: tuple = (255, 255, 255)
    BLUE: tuple = (71, 94, 126)
    LIGHT_BLUE: tuple = (202, 230, 250)
    GOLDEN: tuple = (209, 165, 91)
    RED: tuple = (183, 39, 30)
    GREEN: tuple = (175, 225, 175)
    PURPLE: tuple = (87, 18, 199)
    GRAY: tuple = (44, 44, 44)

    # Font Types
    FONT_TYPE_DEFAULT: str = "font/default_font_pong.ttf"
    FONT_TYPE_MENU: str = "font/menu_font.ttf"

    # Score to Win the Game
    WIN_SCORE: int = 10

    # Score Adder
    SCORE_ADDER_A: int = 1
    SCORE_ADDER_B: int = 1

    # Min and Max of Additional Balls
    MIN_ADDITIONAL_BALLS: int = 2
    MAX_ADDITIONAL_BALLS: int = 4

    # Paddle Speeds
    PADDLE_SPEED_A: float = 5
    PADDLE_SPEED_B: float = 5
    DEFAULT_PADDLE_SPEED: int = 5
    FASTER_PADDLE_SPEED: float = 6.3

    # Paddle Round Corners
    PADDLE_ROUND_CORNERS_A: int = 5
    PADDLE_ROUND_CORNERS_B: int = 5
    PADDLE_ROUND_CORNERS_SHIELD: int = 0

    # Powerup Visible Time
    POWERUP_VISIBLE_TIME: int = 5

    # Powerup Name Visible Time
    POWERUP_NAME_VISIBLE_TIME: int = 2

    # == Constructor ==
    def __init__(self, initial_resolution=Screen_Resolution['720p'], initial_music_on=True):
        # Set window size
        self.resolution = initial_resolution
        self.width = initial_resolution[0]
        self.height = initial_resolution[1]

        # Set Font Sizes
        self.FONT_SIZE_DEFAULT: int = int(self.width / 17)
        self.FONT_SIZE_POWERUP: int = int(self.width / 23)
        self.FONT_SIZE_SMALL_POWERUP: int = int(self.width / 70)
        self.FONT_SIZE_MENU: int = int(self.width / 40)
        self.TITLE_SIZE: int = int(self.width / 28)
        self.SUBTITLE_SIZE: int = int(self.width / 46)
        self.BODY_SIZE: int = int(self.width / 78)
        self.SMALL_BODY_SIZE: int = int(self.width / 90)

        # Music On/Off
        self.MUSIC_ON: bool = initial_music_on

        # ---- Interface ----

        # Set Menu Buttons size
        self.BUTTON_WIDTH: int = int(self.width * 0.3)
        self.BUTTON_HEIGHT: int = int(self.height * 0.06)
        self.SMALL_BUTTON_WIDTH: int = int(self.width * 0.1)
        self.SMALL_BUTTON_HEIGHT: int = int(self.height * 0.06)
        self.BUTTON_GAP: int = int(self.BUTTON_HEIGHT * 2)

        # Set NovaIMS icon size and load in Creators screen
        self.NOVAIMS_ICON_SIZE: tuple = (self.width * 0.07, self.width * 0.07)
        self.NOVAIMS_IMG_LOAD: pygame.image = pygame.transform.smoothscale(
            pygame.image.load("img/creators/novaims_logo.png"),
            self.NOVAIMS_ICON_SIZE)

        # Set Creators icon size and load
        self.CREATOR_ICON_SIZE: tuple = (self.width * 0.1, self.width * 0.1)
        self.CREATOR_1_IMG_LOAD: pygame.image = pygame.transform.smoothscale(
            pygame.image.load("img/creators/creator_1.png"),
            self.CREATOR_ICON_SIZE)
        self.CREATOR_2_IMG_LOAD: pygame.image = pygame.transform.smoothscale(
            pygame.image.load("img/creators/creator_2.png"),
            self.CREATOR_ICON_SIZE)
        self.CREATOR_3_IMG_LOAD: pygame.image = pygame.transform.smoothscale(
            pygame.image.load("img/creators/creator_3.png"),
            self.CREATOR_ICON_SIZE)
        self.CREATOR_4_IMG_LOAD: pygame.image = pygame.transform.smoothscale(
            pygame.image.load("img/creators/creator_4.png"),
            self.CREATOR_ICON_SIZE)

        # ---- Game ----

        # Set Player Team Icon size
        self.PLAYER_ICON_SIZE: tuple = (self.width / 17, self.width / 17)

        # Set PLayer Team Icon Position
        self.PLAYER_A_ICON_POS: tuple = (self.width / 12, 20)
        self.PLAYER_B_ICON_POS: tuple = (
            self.width - (self.width / 12 + self.PLAYER_ICON_SIZE[0]), 20)

        # Set Score Position
        self.POS_SCORE_B: tuple = (self.width / 2 + self.FONT_SIZE_DEFAULT / 1.7, 15)
        self.POS_SCORE_A: tuple = (self.width / 2 - self.FONT_SIZE_DEFAULT, 15)

        # Set the Field Divider Height
        self.FIELD_DIVIDER_INITIAL_POS: tuple = (self.width / 2, self.height * 0.03)
        self.FIELD_DIVIDER_MAX_POS: tuple = (
            self.width / 2,
            self.height - self.height * 0.03)

        # ---- Win Screen ----

        # Set Winner Icon Size
        self.WINNER_ICON_SIZE: tuple = (self.width / 6, self.width / 6)

        # ---- Instructions ----

        # Set background Image
        self.BACKGROUND_IMG: any = pygame.transform.scale(
            pygame.image.load("img/background/background_instructions.jpg"),
            (self.width,
             self.height))

        # Set PowerUp icon Instructions size
        self.POWERUP_WIDTH: float = self.height / 11
        self.POWERUP_HEIGHT: float = self.height / 11

        # Set Screen Alignments
        self.RIGHT_X_ALIGNMENT: float = (self.width * 0.07)
        self.SECOND_RIGHT_X_ALIGNMENT: float = (self.width * 0.37)
        self.LEFT_X_ALIGNMENT: float = (self.width * 0.75)

        # Set Player keys icon size
        self.PLAYER_KEYS_WIDTH: float = self.height / 20
        self.PLAYER_KEYS_HEIGHT: float = self.height / 20

        # Set Player keys icon and position
        self.PLAYER_A_UP: pygame.transform = (
            pygame.transform.smoothscale(pygame.image.load("img/icons/playerA_up.png"),
                                         (self.PLAYER_KEYS_WIDTH,
                                          self.PLAYER_KEYS_HEIGHT)))
        self.PLAYER_A_DOWN: pygame.transform = (
            pygame.transform.smoothscale(pygame.image.load("img/icons/playerA_down.png"),
                                         (self.PLAYER_KEYS_WIDTH,
                                          self.PLAYER_KEYS_HEIGHT)))
        self.PLAYER_B_UP: pygame.transform = (
            pygame.transform.smoothscale(pygame.image.load("img/icons/playerB_up.png"),
                                         (self.PLAYER_KEYS_WIDTH,
                                          self.PLAYER_KEYS_HEIGHT)))
        self.PLAYER_B_DOWN: pygame.transform = (
            pygame.transform.smoothscale(pygame.image.load("img/icons/playerB_down.png"),
                                         (self.PLAYER_KEYS_WIDTH,
                                          self.PLAYER_KEYS_HEIGHT)))

        # Set the position of a powerup icon in instructions
        self.POWERUP_ICON_POS_LIST: dict = {'Ant-Man': (self.RIGHT_X_ALIGNMENT, self.height * 0.3),
                                            'Black Widow': (self.RIGHT_X_ALIGNMENT, self.height * 0.5),
                                            'Scarlet Witch': (self.RIGHT_X_ALIGNMENT, self.height * 0.7),
                                            'Quicksilver': (self.SECOND_RIGHT_X_ALIGNMENT, self.height * 0.3),
                                            'Iron Man': (self.SECOND_RIGHT_X_ALIGNMENT, self.height * 0.5),
                                            'Captain America': (self.SECOND_RIGHT_X_ALIGNMENT, self.height * 0.7)}

        # Set Escape key icon size
        self.ESCAPE_KEY_WIDTH: float = self.height / 23
        self.ESCAPE_KEY_HEIGHT: float = self.height / 23

        # Set Escape key icon and position
        self.ESCAPE_KEY: tuple = (pygame.transform.smoothscale(pygame.image.load("img/icons/esc_key.png"),
                                                               (self.ESCAPE_KEY_WIDTH,
                                                                self.ESCAPE_KEY_HEIGHT)),
                                  (self.width * 0.96, self.height * 0.04))

        # ---- Ball ----

        # Set ball size
        self.BALL_WIDTH: float = self.width / 20
        self.BALL_HEIGHT: float = self.width / 20

        # Set ball initial position
        self.INITIAL_POS_X: float = self.width / 2 - self.BALL_WIDTH / 2
        self.INITIAL_POS_Y: float = self.height / 2 - self.BALL_HEIGHT / 2

        # ---- Paddles ----

        # Set Paddle A size
        self.PADDLE_WIDTH_A: float = self.height / 50
        self.PADDLE_HEIGHT_A: float = self.height / 5

        # Set Paddle B size
        self.PADDLE_WIDTH_B: float = self.height / 50
        self.PADDLE_HEIGHT_B: float = self.height / 5

        # Set PaddleA initial position
        self.INITIAL_POS_X_A: float = 0 + self.PADDLE_WIDTH_A * 2
        self.INITIAL_POS_Y_A: float = self.height / 2 - self.PADDLE_HEIGHT_A / 2

        # Set PaddleB initial position
        self.INITIAL_POS_X_B: float = self.width - self.PADDLE_WIDTH_B * 3
        self.INITIAL_POS_Y_B: float = self.height / 2 - self.PADDLE_HEIGHT_B / 2

        # ---- Powerups ----

        # Set PowerUp icon size
        self.POWERUP_WIDTH: float = self.height / 8
        self.POWERUP_HEIGHT: float = self.height / 8

        # Set PowerUp field of view size
        self.POWERUP_FIELD_WIDTH: tuple = (int(self.width * 0.17), int(self.width - self.width * 0.17))
        self.POWERUP_FIELD_HEIGHT: tuple = (int(self.height * 0.17), int(self.height - self.height * 0.17))

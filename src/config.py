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
    WIN_SCORE: int = 12

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
        self.font_size_default: int = int(self.width / 17)
        self.font_size_powerup: int = int(self.width / 23)
        self.font_size_small_powerup: int = int(self.width / 70)
        self.font_size_menu: int = int(self.width / 40)
        self.title_size: int = int(self.width / 28)
        self.subtitle_size: int = int(self.width / 46)
        self.body_size: int = int(self.width / 78)
        self.small_body_size: int = int(self.width / 90)

        # Music On/Off
        self.music_on: bool = initial_music_on

        # ---- Interface ----

        # Set Menu Buttons size
        self.button_width: int = int(self.width * 0.3)
        self.button_height: int = int(self.height * 0.06)
        self.small_button_width: int = int(self.width * 0.1)
        self.small_button_height: int = int(self.height * 0.06)
        self.button_gap: int = int(self.button_height * 2)

        # Set NovaIMS icon size and load in Creators screen
        self.novaims_icon_size: tuple = (self.width * 0.07, self.width * 0.07)
        self.novaims_img_load: pygame.transform = pygame.transform.smoothscale(
            pygame.image.load("img/creators/novaims_logo.png"), self.novaims_icon_size)

        # Set Sound On/Off icon size and load in Settings screen
        self.sound_on_icon_size: tuple = (self.width * 0.03, self.width * 0.03)
        self.sound_on_img_load: pygame.transform = pygame.transform.smoothscale(
            pygame.image.load('img/icons/sound_icon.png'), self.sound_on_icon_size)

        # Set Creators icon size and load
        self.creator_icon_size: tuple = (self.width * 0.1, self.width * 0.1)
        self.creator_1_img_load: pygame.image = pygame.transform.smoothscale(
            pygame.image.load("img/creators/creator_1.png"),
            self.creator_icon_size)
        self.creator_2_img_load: pygame.image = pygame.transform.smoothscale(
            pygame.image.load("img/creators/creator_2.png"),
            self.creator_icon_size)
        self.creator_3_img_load: pygame.image = pygame.transform.smoothscale(
            pygame.image.load("img/creators/creator_3.png"),
            self.creator_icon_size)
        self.creator_4_img_load: pygame.image = pygame.transform.smoothscale(
            pygame.image.load("img/creators/creator_4.png"),
            self.creator_icon_size)

        # ---- Game ----

        # Set Player Team Icon size
        self.player_icon_size: tuple = (self.width / 17, self.width / 17)

        # Set PLayer Team Icon Position
        self.player_a_icon_pos: tuple = (self.width / 12, 20)
        self.player_b_icon_pos: tuple = (
            self.width - (self.width / 12 + self.player_icon_size[0]), 20)

        # Set Score Position
        self.pos_score_a: tuple = (self.width / 2 - self.font_size_default, 15)
        self.pos_score_b: tuple = (self.width / 2 + self.font_size_default / 1.7, 15)

        # Set the Field Divider Height
        self.field_divider_initial_pos: tuple = (self.width / 2, self.height * 0.03)
        self.field_divider_max_pos: tuple = (self.width / 2, self.height - self.height * 0.03)

        # ---- Win Screen ----

        # Set Winner Icon Size
        self.winner_icon_size: tuple = (self.width / 6, self.width / 6)

        # ---- Instructions ----

        # Set background Image
        self.background_img: any = pygame.transform.scale(
            pygame.image.load("img/background/background_instructions.jpg"), (self.width, self.height))

        # Set PowerUp icon Instructions size
        self.powerup_width: float = self.height / 11
        self.powerup_height: float = self.height / 11

        # Set Screen Alignments
        self.right_x_alignment: float = (self.width * 0.07)
        self.second_right_x_alignment: float = (self.width * 0.37)
        self.left_x_alignment: float = (self.width * 0.75)

        # Set Player keys icon size
        self.player_keys_width: float = self.height / 20
        self.player_keys_height: float = self.height / 20

        # Set Player keys icon and position
        self.player_a_up: pygame.transform = (
            pygame.transform.smoothscale(pygame.image.load("img/icons/playerA_up.png"),
                                         (self.player_keys_width,
                                          self.player_keys_height)))
        self.player_a_down: pygame.transform = (
            pygame.transform.smoothscale(pygame.image.load("img/icons/playerA_down.png"),
                                         (self.player_keys_width,
                                          self.player_keys_height)))
        self.player_b_up: pygame.transform = (
            pygame.transform.smoothscale(pygame.image.load("img/icons/playerB_up.png"),
                                         (self.player_keys_width,
                                          self.player_keys_height)))
        self.player_b_down: pygame.transform = (
            pygame.transform.smoothscale(pygame.image.load("img/icons/playerB_down.png"),
                                         (self.player_keys_width,
                                          self.player_keys_height)))

        # Set the position of a powerup icon in instructions
        self.powerup_icon_pos_list: dict = {'Ant-Man': (self.right_x_alignment, self.height * 0.3),
                                            'Black Widow': (self.right_x_alignment, self.height * 0.5),
                                            'Scarlet Witch': (self.right_x_alignment, self.height * 0.7),
                                            'Quicksilver': (self.second_right_x_alignment, self.height * 0.3),
                                            'Iron Man': (self.second_right_x_alignment, self.height * 0.5),
                                            'Captain America': (self.second_right_x_alignment, self.height * 0.7)}

        # Set Escape key icon size
        self.escape_key_width: float = self.height / 23
        self.escape_key_height: float = self.height / 23

        # Set Escape key icon and position
        self.escape_key: tuple = (pygame.transform.smoothscale(pygame.image.load("img/icons/esc_key.png"),
                                                               (self.escape_key_width,
                                                                self.escape_key_height)),
                                  (self.width * 0.96, self.height * 0.04))

        # ---- Ball ----

        # Set ball size
        self.ball_width: float = self.width / 20
        self.ball_height: float = self.width / 20

        # Set ball initial position
        self.initial_pos_x: float = self.width / 2 - self.ball_width / 2
        self.initial_pos_y: float = self.height / 2 - self.ball_height / 2

        # ---- Paddles ----

        # Set Paddle A size
        self.paddle_width_a: float = self.height / 50
        self.paddle_height_a: float = self.height / 5

        # Set Paddle B size
        self.paddle_width_b: float = self.height / 50
        self.paddle_height_b: float = self.height / 5

        # Set PaddleA initial position
        self.initial_pos_x_a: float = 0 + self.paddle_width_a * 2
        self.initial_pos_y_a: float = self.height / 2 - self.paddle_height_a / 2

        # Set PaddleB initial position
        self.initial_pos_x_b: float = self.width - self.paddle_width_b * 3
        self.initial_pos_y_b: float = self.height / 2 - self.paddle_height_b / 2

        # ---- Powerups ----

        # Set PowerUp icon size
        self.powerup_width: float = self.height / 8
        self.powerup_height: float = self.height / 8

        # Set PowerUp field of view size
        self.powerup_field_width: tuple = (int(self.width * 0.17), int(self.width - self.width * 0.17))
        self.powerup_field_height: tuple = (int(self.height * 0.17), int(self.height - self.height * 0.17))

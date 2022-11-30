import pygame

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

# Set Ball size
BALL_WIDTH: int = 40
BALL_HEIGHT: int = 40

# Set PowerUp size
POWERUP_WIDTH: int = 60
POWERUP_HEIGHT: int = 60

# Set PowerUp field of view size
POWERUP_FIELD_WIDTH: int = WINDOW_WIDTH-POWERUP_WIDTH
POWERUP_FIELD_HEIGHT: int = WINDOW_HEIGHT-POWERUP_HEIGHT

# Set Paddles size
Paddle_WIDTH: int = 10
Paddle_HEIGHT: float = WINDOW_HEIGHT / 5

# Set score to win the game
WIN_SCORE: int = 10

# Set score Position
POS_SCORE_B = (WINDOW_WIDTH / 2 + FONT_SIZE / 1.7, 15)
POS_SCORE_A = (WINDOW_WIDTH/2 - FONT_SIZE, 15)
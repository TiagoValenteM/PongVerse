from .config import *


# Class Paddle represents the paddles that bounce the ball
class Paddle(pygame.sprite.Sprite):  # Inherit from Pygame Sprite class
    """
    A class representing a paddle in the game.

    The paddle is a rectangular object that bounces the ball. It has a specified color and dimensions, and can be moved
    up or down within the game window.

    Attributes:
        settings: An instance of the `GlobalSettings` class that stores the game settings.
        height: An integer representing the height of the paddle.
        border_radius: An integer representing the radius of the rounded corners of the paddle.
        image: A Pygame surface representing the image of the paddle.
        rect: A Pygame rectangle representing the dimensions of the paddle.

    Methods:
        moveUp(self, pixels: int) -> None: Move the paddle up by a specified number of pixels.
        moveDown(self, pixels: int, window_height: int) -> None: Move the paddle down by a specified number of pixels.
    """

    def __init__(self, color: tuple, width: float, height: float, border_radius: int):
        """
                Initialize the paddle.

                Args:
                    color: A tuple representing the RGB values of the color of the paddle.
                    width: An float representing the width of the paddle.
                    height: An float representing the height of the paddle.
                    border_radius: An integer representing the radius of the rounded corners of the paddle.
        """
        super().__init__()  # Call the parent class (Sprite) constructor
        self.settings: GlobalSettings = GlobalSettings()  # Pass Paddle settings
        self.height: float = height  # Set the height
        self.border_radius: int = border_radius  # Set the border radius
        self.image: pygame.surface = pygame.Surface([width, height])  # Create the surface
        self.image.fill(GlobalSettings.BLACK)  # Fill the background color
        self.image.set_colorkey(GlobalSettings.BLACK)  # Set the background color to be transparent
        pygame.draw.rect(self.image, color, [0, 0, width, height], border_radius=border_radius)  # Draw the paddle
        self.rect: pygame.rect = self.image.get_rect()  # Get the rectangle of the paddle

    # Methods that update the position of the paddle

    def moveUp(self, pixels: int) -> None:  # Method to move paddle up
        """
                Move the paddle up by a specified number of pixels.

                Args:
                    pixels: An integer representing the number of pixels to move the paddle.
                """
        self.rect.y -= pixels
        if self.rect.y < 0:  # Preventing going too far
            self.rect.y = 0
            pass

    def moveDown(self, pixels: int, window_height: int) -> None:  # Method to move paddle down
        """
                Move the paddle down by a specified number of pixels.

                Args:
                    pixels: An integer representing the number of pixels to move the paddle.
                    window_height: An integer representing the height of the game window.
                """
        self.rect.y += pixels
        if self.rect.y > window_height - self.height:  # Preventing going too far
            self.rect.y = window_height - self.height
            pass

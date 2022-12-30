from .config import *


# Class Paddle represents the paddles that bounce the ball
class Paddle(pygame.sprite.Sprite):  # Inherit from Pygame Sprite class
    def __init__(self, color, width, height, border_radius):
        # Call the parent class (Sprite) constructor
        super().__init__()
        # Pass Paddle settings
        self.settings: GlobalSettings = GlobalSettings()
        # Set the height and border radius
        self.height: int = height
        self.border_radius: int = border_radius
        # Set the background color and set it to be transparent
        self.image: pygame.surface = pygame.Surface([width, height])
        self.image.fill(GlobalSettings.BLACK)
        self.image.set_colorkey(GlobalSettings.BLACK)
        # Draw the paddle
        pygame.draw.rect(self.image, color, [0, 0, width, height], border_radius=border_radius)
        # Get the rectangle dimensions
        self.rect: pygame.rect = self.image.get_rect()

    # Methods that update the position of the paddle

    def moveUp(self, pixels):  # Method to move paddle up
        self.rect.y -= pixels
        if self.rect.y < 0:  # Preventing going too far
            self.rect.y = 0
            pass

    def moveDown(self, pixels, window_height):  # Method to move paddle down
        self.rect.y += pixels
        if self.rect.y > window_height - self.height:  # Preventing going too far
            self.rect.y = window_height - self.height
            pass

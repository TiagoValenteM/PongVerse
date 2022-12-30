from .config import *


# Class Paddle represents the paddles that bounce the ball
class Paddle(pygame.sprite.Sprite):  # Inherit from Pygame Sprite class
    def __init__(self, color, width, height, border_radius):
        super().__init__()  # Call the parent class (Sprite) constructor
        self.settings: GlobalSettings = GlobalSettings()  # Pass Paddle settings
        self.height: int = height  # Set the height
        self.border_radius: int = border_radius  # Set the border radius
        self.image: pygame.surface = pygame.Surface([width, height])  # Create the surface
        self.image.fill(GlobalSettings.BLACK)  # Fill the background color
        self.image.set_colorkey(GlobalSettings.BLACK)  # Set the background color to be transparent
        pygame.draw.rect(self.image, color, [0, 0, width, height], border_radius=border_radius)  # Draw the paddle
        self.rect: pygame.rect = self.image.get_rect()  # Get the rectangle of the paddle

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

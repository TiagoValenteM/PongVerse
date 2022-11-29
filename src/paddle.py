import pygame

# 1
# color black, rgb scale
BLACK = (0, 0, 0)


# let's create the paddle class
class Paddle(pygame.sprite.Sprite):
    # SARA : sprites are visible game objects. they have appearance measures/ characteristics
    # This class represents a paddle. It derives from the "Sprite" class in Pygame.
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        # Pass in the color of the Paddle, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        # Draw the paddle (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

        # ADD TWO METHODS, ONE THAT MOVES THE PADDLE UP

    def moveUp(self, pixels):
        self.rect.y -= pixels
        # preventing going too far
        if self.rect.y < 0:
            self.rect.y = 0
            pass

        # ONE THAT MOVES IT DOWN

    def moveDown(self, pixels, window_height, paddle_height):
        self.rect.y += pixels
        # preventing going too far
        if self.rect.y > window_height - paddle_height:
            self.rect.y = window_height - paddle_height
            pass

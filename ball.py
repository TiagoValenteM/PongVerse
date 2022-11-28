import pygame
from random import randint

BLACK = (0, 0, 0)


# lets create the ball class
class Ball(pygame.sprite.Sprite):
    # This class represents a ball. It derives from the "Sprite" class in Pygame.
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        # Pass in the color of the ball, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        # Draw the ball (a rectangle!)
        # WE NEED TO USE A PYGAME BUILT IN METHOD
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()

        # LETS SET THE BALL SPEED ATTRIBUTE, IT WILL HAVE TWO COMPONENTS, Y-SPEED, X-SPEED, BOTH RANDOM,
        # CHOOSE CAREFULLY THE INTERVAL
        # setting the ball velocity in the form of [x velocity, y velocity]
        self.velocity = [randint(4, 8), randint(-8, 8)]
        ## Fetch the rectangle object that has the dimensions of the image.

    # CREATE THE UPDATE METHOD, THAT MODIFIES THE POSITION OF THE BALL ACCORDING TO THE SPEED
    # method that updates the position of the ball
    def update(self, move: False):
        if move:
            self.rect.x += self.velocity[0]
            self.rect.y += self.velocity[1]

    # CREATE THE BOUNCE METHOD, THAT MODIFIES THE SPEED OF THE BALL AFTER IT TOUCHES A PADDLE
    # method that updates the position of the ball once it hits an obstacle
    def bounce(self):
        # x will need to change to the opposite direction
        self.velocity[0] = -self.velocity[0]
        # y can still randomly either go up or down
        self.velocity[1] = randint(-8, 8)

    def bounce_up_down(self):
        # x will not be affected
        # y will need to change to the opposite direction
        self.velocity[1] = -self.velocity[1]

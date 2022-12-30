import pygame
from random import randint
from .config import GlobalSettings


# Class Ball represents the ball that bounces around the screen
class Ball(pygame.sprite.Sprite):  # Inherit from Pygame Sprite class
    def __init__(self, filename, width, height, settings: GlobalSettings):
        # Call the parent class (Sprite) constructor
        super().__init__()
        # Pass Ball settings
        self.settings: GlobalSettings = settings
        # Load and scale the image
        self.image: pygame.image = pygame.image.load(filename)
        self.image: pygame.transform = pygame.transform.smoothscale(self.image, (width, height))
        # Draw the ball
        pygame.draw.rect(self.image, self.settings.BLACK, [width, height, 0, 0])
        # Get the ball rectangle dimensions
        self.rect: pygame.image = self.image.get_rect()
        # X and Y velocity
        self.x_velocity: randint = randint(int(-self.settings.height / 70), int(-self.settings.height / 120))
        self.y_velocity: randint = randint(int(self.settings.height / 120), int(self.settings.height / 70))
        # Ball velocity adapted to screen resolution (X, Y)
        self.velocity: list = [self.x_velocity, self.y_velocity]

    # Method that updates the position of the ball
    def update(self, move: False):
        if move:
            self.rect.x += self.velocity[0]
            self.rect.y += self.velocity[1]

    # Methods that update the position of the ball once it hits an obstacle
    # Bounce the ball off a horizontal surface (paddle)
    def bounce(self):
        # X changes to opposite direction
        self.velocity[0] = - self.velocity[0]
        # Y Goes up or down randomly
        self.velocity[1] = randint(-8, 8)

    # Bounce the ball off a vertical surface (wall)
    def bounceUpDown(self):
        # X not affected
        # Y changes to opposite direction
        self.velocity[1] = - self.velocity[1]

    # Detect collision between the ball and the paddles and change its speed accordingly
    def handleBallCollision(self, ball_owner, paddleA, paddleB):
        # Detect collision with paddleA
        if pygame.sprite.collide_mask(self, paddleA):
            ball_owner: str = 'paddleA'
            self.bounce()
        # Detect collision with paddleB
        if pygame.sprite.collide_mask(self, paddleB):
            ball_owner: str = 'paddleB'
            self.bounce()
        # Return the ball owner
        return ball_owner

    # Reset Ball position
    def resetBall(self):
        # Initial position of the ball (center of the screen)
        self.rect.x, self.rect.y = (self.settings.initial_pos_x, self.settings.initial_pos_y)

    # Handle the ball motion in the screen
    def handleBallMotion(self, scoreA, scoreB, ball_owner, triggered):
        # If the ball goes off the right of the screen
        if self.rect.x >= self.settings.width + self.settings.ball_width:
            # Add score to player A
            scoreA += self.settings.SCORE_ADDER_A
            # Reset the ball
            self.resetBall()
            ball_owner = None  # Reset the ball owner
            triggered: bool = False  # Reset the trigger
            # Ball direction turns to the left
            self.velocity[0] = - self.velocity[0]
        # If the ball goes off the left side of the screen
        if self.rect.x <= 0 - self.settings.ball_width:
            # Add score to player B
            scoreB += self.settings.SCORE_ADDER_B
            # Reset the ball
            self.resetBall()
            ball_owner = None  # Reset the ball owner
            triggered: bool = False  # Reset the trigger
            # Ball direction turns to the right
            self.velocity[0] = - self.velocity[0]
        # if the ball hits the bottom of the screen, bounce it
        if self.rect.y >= self.settings.height - self.settings.ball_height:
            self.bounceUpDown()
        # If the ball hits the top of the screen, bounce it
        if self.rect.y <= 0:
            self.bounceUpDown()
        return scoreA, scoreB, ball_owner, triggered

    # Handle multiple balls motion in the screen
    def handleMultipleBallsMotion(self, powerup_owner, scoreA, scoreB):
        # Boolean to check if the ball is out of the screen
        should_kill: bool = False
        # If the ball goes off the right of the screen
        if self.rect.x >= self.settings.width + self.settings.ball_width:
            if powerup_owner == 'paddleA':  # If the ball is owned by player A
                # Add score to player A
                scoreA += self.settings.SCORE_ADDER_A
            # Ball out of the screen --> kill the ball
            should_kill: bool = True
            self.kill()  # kill the ball
        # If the ball goes off the left of the screen
        if self.rect.x <= 0 - self.settings.ball_width:
            if powerup_owner == 'paddleB':  # If the ball is owned by player B
                # Add score to player B
                scoreB += self.settings.SCORE_ADDER_B
            # Ball out of the screen --> kill the ball
            should_kill: bool = True
            self.kill()  # kill the ball
        # If the ball hits the bottom of the screen, bounce it
        if self.rect.y >= self.settings.height - self.settings.ball_height:
            self.bounceUpDown()
        # If the ball hits the top of the screen, bounce it
        if self.rect.y <= 0:
            self.bounceUpDown()
        return scoreA, scoreB, should_kill

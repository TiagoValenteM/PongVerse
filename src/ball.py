import pygame
from random import randint
from src.config import GlobalSettings


# let's create the ball class
class Ball(pygame.sprite.Sprite):
    # This class represents a ball. It derives from the "Sprite" class in Pygame.
    def __init__(self, filename, width, height, settings: GlobalSettings):
        # Call the parent class (Sprite) constructor
        super().__init__()
        # Store game settings
        self.settings = settings
        # Pass in the color of the ball, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.smoothscale(self.image, (width, height))
        # Draw the ball (a rectangle!)
        # WE NEED TO USE A PYGAME BUILT IN METHOD
        pygame.draw.rect(self.image, self.settings.BLACK, [width, height, 0, 0])
        self.rect = self.image.get_rect()
        # LET'S SET THE BALL SPEED ATTRIBUTE, IT WILL HAVE TWO COMPONENTS, Y-SPEED, X-SPEED, BOTH RANDOM,
        # CHOOSE CAREFULLY THE INTERVAL
        # setting the ball velocity in the form of [x velocity, y velocity]
        self.velocity = [randint(6, 10), randint(-10, 10)]
        # Fetch the rectangle object that has the dimensions of the image.

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

    # Detect collisions between the ball and the paddles and change its speed accordingly
    def handle_ball_collision(self, ball_owner, paddleA, paddleB):
        if pygame.sprite.collide_mask(self, paddleA):
            ball_owner = 'paddleA'
            self.bounce()
        if pygame.sprite.collide_mask(self, paddleB):
            ball_owner = 'paddleB'
            self.bounce()
        return ball_owner

    # Resets Ball position
    def reset_ball(self):
        # Initial position of the ball
        self.rect.x, self.rect.y = (self.settings.INITIAL_POS_X, self.settings.INITIAL_POS_Y)

    # Handles the ball motion in the screen
    def handle_ball_motion(self, scoreA, scoreB, ball_owner, triggered):
        if self.rect.x >= self.settings.width + self.settings.BALL_WIDTH:
            scoreA += self.settings.SCORE_ADDER_A
            self.reset_ball()
            ball_owner = None
            triggered = False
            self.velocity[0] = - self.velocity[0]
        if self.rect.x <= 0 - self.settings.BALL_WIDTH:
            scoreB += self.settings.SCORE_ADDER_B
            self.reset_ball()
            ball_owner = None
            triggered = False
            self.velocity[0] = - self.velocity[0]
        if self.rect.y >= self.settings.height - self.settings.BALL_HEIGHT:
            self.bounce_up_down()
        if self.rect.y <= 0:
            self.bounce_up_down()
        return scoreA, scoreB, ball_owner, triggered

    # Handles multiple balls motion in the screen
    def handle_multiple_balls_motion(self, powerup_owner, scoreA, scoreB):
        should_kill = False
        if self.rect.x >= self.settings.width + self.settings.BALL_WIDTH:
            if powerup_owner == 'paddleA':
                scoreA += self.settings.SCORE_ADDER_A
            should_kill = True
            self.kill()
        if self.rect.x <= 0 - self.settings.BALL_WIDTH:
            if powerup_owner == 'paddleB':
                scoreB += self.settings.SCORE_ADDER_B
            should_kill = True
            self.kill()
        if self.rect.y >= self.settings.height - self.settings.BALL_HEIGHT:
            self.bounce_up_down()
        if self.rect.y <= 0:
            self.bounce_up_down()
        return scoreA, scoreB, should_kill

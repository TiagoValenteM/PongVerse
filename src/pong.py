# Import the pygame library and initialise the game engine
import pygame
from .config import *
from random import choices
from .paddle import Paddle
from .ball import Ball
from .powerups import *


class PongVerse:
    def __init__(self):
        # Set if a powerup is visible
        self.powerup_visible: any = None
        # Set if a powerup is active
        self.powerup_active: any = None
        # Set the time for the powerup icon to be visible
        self.powerup_visible_time: any = None
        # Set the time a powerup affects a player
        self.powerup_active_time: any = None
        # Opens a new window
        self.screen = pygame.display.set_mode(GameSettings.WINDOW_SIZE)
        # Set the Default Font
        self.default_font = pygame.font.Font(GameSettings.FONT_TYPE, GameSettings.FONT_SIZE)

    # Define when a PowerUp appears, and it appears every 3 goals
    def set_powerup_visible(self, scoreA, scoreB, ball_owner, all_sprites_list):
        # Gets the powerup probability
        PowerUps_Probabilities = [val.probability for val in PowerUps.values()]

        # It checks if the sum of the scores is divisible by 3
        if (scoreA + scoreB) % 3 == 0 and (scoreA + scoreB) != 0:
            # It chooses the first chosen random powerup
            chosen_powerup = choices(PowerUps, PowerUps_Probabilities)[0]
            # It creates the powerup
            powerup = ShrinkEnlarge(ball_owner, PowerUpSettings.POWERUP_WIDTH, PowerUpSettings.POWERUP_HEIGHT)
            # It adds the powerup to the list of objects
            all_sprites_list.add(powerup)
            # It sets the powerup as active
            self.powerup_visible = powerup
            # It sets the powerup timer
            self.powerup_visible_time = pygame.time.get_ticks()

    # Define when a PowerUp icon disappears
    def set_powerup_invisible(self):
        self.powerup_visible.kill()
        self.powerup_visible = None
        self.powerup_visible_time = None

    # Define when a PowerUp becomes active
    def set_powerup_active(self, paddleA, paddleB, ball):
        self.powerup_active = self.powerup_visible
        self.powerup_visible.kill()
        # It activates the powerup
        self.powerup_active.run_powerup(paddleA, paddleB, ball)
        self.powerup_active_time = pygame.time.get_ticks()

    # Define when a PowerUp becomes inactive and is effect revert
    def set_powerup_inactive(self, paddleA, paddleB, ball):
        # It reverts the powerup effect
        self.powerup_active.revert_powerup(paddleA, paddleB, ball)
        # It sets the powerup as inactive
        self.powerup_active = None
        self.powerup_active_time = None

    # Resets Ball position
    @staticmethod
    def reset_ball(ball):
        # Initial position of the ball
        ball.rect.x, ball.rect.y = (BallSettings.INITIAL_POS_X, BallSettings.INITIAL_POS_Y)

    # Function to manage who is winning
    def display_scores(self, score_A, score_B):
        color_A = GameSettings.WHITE
        color_B = GameSettings.WHITE

        if score_A > score_B:
            color_A = GameSettings.BLUE
        elif score_A < score_B:
            color_B = GameSettings.GOLDEN

        text_A = self.default_font.render(str(score_A), True, color_A)
        text_B = self.default_font.render(str(score_B), True, color_B)
        self.screen.blit(text_A, GameSettings.POS_SCORE_A)
        self.screen.blit(text_B, GameSettings.POS_SCORE_B)

    def play(self):
        # Initialize pygame
        pygame.init()
        # Set the title of the window/game
        pygame.display.set_caption(GameSettings.GAME_TITLE)
        # Set the game icon
        pygame.display.set_icon(GameSettings.GAME_ICON)
        triggered = False
        ball_owner = None

        # Set the title of the window/game
        pygame.display.set_caption(GameSettings.GAME_TITLE)

        # Let's create two paddles
        # Player A paddle
        paddleA = Paddle(GameSettings.BLUE, PaddleSettings.PADDLE_WIDTH_A, PaddleSettings.PADDLE_HEIGHT_A,
                         PaddleSettings.PADDLE_ROUND_CORNERS_A)
        paddleA.rect.x, paddleA.rect.y = (PaddleSettings.INITIAL_POS_X_A, PaddleSettings.INITIAL_POS_Y_A)
        # Player B paddle
        paddleB = Paddle(GameSettings.GOLDEN, PaddleSettings.PADDLE_WIDTH_B, PaddleSettings.PADDLE_HEIGHT_B,
                         PaddleSettings.PADDLE_ROUND_CORNERS_B)
        paddleB.rect.x, paddleB.rect.y = (PaddleSettings.INITIAL_POS_X_B, PaddleSettings.INITIAL_POS_Y_B)

        # Let's create a ball
        # Set the ball and its initial position
        ball = Ball("img/ball.png", BallSettings.BALL_WIDTH, BallSettings.BALL_HEIGHT)
        ball.rect.x, ball.rect.y = (BallSettings.INITIAL_POS_X, BallSettings.INITIAL_POS_Y)

        # This will be a list that will contain all the sprites we intend to use in our game.
        all_sprites_list = pygame.sprite.Group()

        # Add the 2 paddles and the ball to the list of objects
        all_sprites_list.add(paddleA)
        all_sprites_list.add(paddleB)
        all_sprites_list.add(ball)
        # The loop will carry on until the user exits the game (e.g. clicks the close button).
        carryOn = True

        # The clock will be used to control how fast the screen updates
        clock = pygame.time.Clock()

        # Initialise player scores
        scoreA = 0
        scoreB = 0

        def show_go_screen():
            self.screen.fill(GameSettings.BLUE)
            font = pygame.font.SysFont(GameSettings.FONT_TYPE, 25)  # creates a font object
            lastScore = font.render('Best Score: ' + str(scoreA), True, (255, 255, 255))
            self.screen.blit(lastScore, (700 / 2, 500 / 2))
            pygame.display.flip()

        # -------- Main Program Loop -----------
        while carryOn:
            # --- Main event loop
            # User did something
            for event in pygame.event.get():

                # If user clicked close
                if event.type == pygame.QUIT:
                    # Flag that we are done so we exit this loop
                    carryOn = False

                    # Or he used the keyboard
                elif event.type == pygame.KEYDOWN:
                    # Pressing the Escape Key will quit the game
                    if event.key == pygame.K_ESCAPE:
                        # quit the loop
                        carryOn = False
            # Moving the paddles when the user uses the keys
            keys = pygame.key.get_pressed()  # this built-in method saves the user input from the keyboard

            # moving the paddles when the user hits W/S (player A) or up/down (player B)
            if keys[pygame.K_w]:
                paddleA.moveUp(PaddleSettings.PADDLE_SPEED_A)
                triggered = True
            if keys[pygame.K_s]:
                paddleA.moveDown(PaddleSettings.PADDLE_SPEED_A, GameSettings.WINDOW_HEIGHT)
                triggered = True
            if keys[pygame.K_UP]:
                paddleB.moveUp(PaddleSettings.PADDLE_SPEED_B)
                triggered = True
            if keys[pygame.K_DOWN]:
                paddleB.moveDown(PaddleSettings.PADDLE_SPEED_B, GameSettings.WINDOW_HEIGHT)
                triggered = True

                # --- Game logic should go here
            all_sprites_list.update(move=triggered)

            # Checking if the ball was scored and changing speed accordingly
            if ball.rect.x >= GameSettings.WINDOW_WIDTH + BallSettings.BALL_WIDTH:
                scoreA += GameSettings.SCORE_ADDER_A
                self.reset_ball(ball)
                ball_owner = None
                triggered = False
                ball.velocity[0] = -ball.velocity[0]
            if ball.rect.x <= 0 - BallSettings.BALL_WIDTH:
                scoreB += GameSettings.SCORE_ADDER_B
                self.reset_ball(ball)
                ball_owner = None
                triggered = False
                ball.velocity[0] = -ball.velocity[0]
            if ball.rect.y >= GameSettings.WINDOW_HEIGHT - BallSettings.BALL_HEIGHT:
                ball.bounce_up_down()
            if ball.rect.y <= 0:
                ball.bounce_up_down()

            # Detects if a player hits a win score
            if scoreA >= GameSettings.WIN_SCORE or scoreB >= GameSettings.WIN_SCORE:
                show_go_screen()
                break

            # Detect collisions between the ball and the paddles and change its speed accordingly
            if pygame.sprite.collide_mask(ball, paddleA):
                ball_owner = 'paddleA'
                ball.bounce()
            if pygame.sprite.collide_mask(ball, paddleB):
                ball_owner = 'paddleB'
                ball.bounce()

            # Set the screen background image
            self.screen.blit(GameSettings.BACKGROUND_IMG, (0, 0))

            # Set the players icons:
            # Player A icon
            self.screen.blit(GameSettings.PLAYER_A_ICON, GameSettings.PLAYER_A_ICON_POS)
            # Player B icon
            self.screen.blit(GameSettings.PLAYER_B_ICON, GameSettings.PLAYER_B_ICON_POS)

            # Draw the net A WHITE LINE FROM TOP TO BOTTOM (USE PYGAME BUILT-IN METHOD)
            pygame.draw.line(self.screen, GameSettings.WHITE, [GameSettings.WINDOW_WIDTH / 2, 0],
                             [GameSettings.WINDOW_WIDTH / 2, GameSettings.WINDOW_HEIGHT], 5)

            # Set all the game objects (sprites) to be drawn on the screen
            all_sprites_list.draw(self.screen)

            # Display scores:
            # Calls display_scores function to manage colors according to who is winning
            self.display_scores(scoreA, scoreB)

            # Checks if a powerup is invisible and inactive and if there is a ball owner
            if self.powerup_visible is None and self.powerup_active is None and ball_owner is not None:
                # Sets a random powerup to be visible
                self.set_powerup_visible(scoreA, scoreB, ball_owner, all_sprites_list)

            # Checks if a powerup is visible
            if self.powerup_visible_time is not None:
                visible = (pygame.time.get_ticks() - self.powerup_visible_time) / 1000
                if int(visible) < self.powerup_visible.visible_time:
                    # If it is visible, it checks if it collides with the ball
                    if pygame.sprite.collide_mask(ball, self.powerup_visible) and ball_owner is not None:
                        self.set_powerup_active(paddleA, paddleB, ball)
                else:
                    self.set_powerup_invisible()

            # Checks if a powerup is active
            if self.powerup_active_time is not None:
                # Creates a variable that stores the time the powerup has been active
                activated = (pygame.time.get_ticks() - self.powerup_active_time) / 1000
                # It checks if the active time is over
                if int(activated) == self.powerup_active.active_time:
                    self.set_powerup_inactive(paddleA, paddleB, ball)

            # USE PY-GAME BUILT IN METHODS,  SELECT THE POSITION THAT YOU PREFER

            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # --- Limit to 60 frames per second
            clock.tick(60)

        # Once we have exited the main program loop we can stop the game engine:
        pygame.quit()

# TODO: the game starts with white paddle and colors change for the last one that scored
# TODO: get back to the main menu from the game when it starts
# TODO: Choose between Vanilla Pong or PowerUps Pong - MUST HAVE INSTRUCTIONS FOR EVERYTHING


# powerup_name = self.default_font.render(str(self.powerup_active.name), True, GameSettings.WHITE)
# self.screen.blit(powerup_name, GameSettings.POS_SCORE_A)
